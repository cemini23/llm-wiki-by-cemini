import datetime as dt
import unittest

from scripts.intel.monitors.jobs import (
    annotate_jobs,
    baseline_by_source,
    classify_roles,
    cluster_summaries,
    delta_from_state,
    haversine_miles,
    normalize_corecivic_job,
    role_score,
)


def sample_config():
    return {
        "settings": {
            "recent_days": 45,
            "default_radius_miles": 40,
            "excluded_context_keywords": {"geo": ["BI Boulder", "corporate", "ISAP"]},
        },
        "role_weights": {
            "security": 3,
            "intake_admin": 3,
            "transport": 4,
            "leadership": 4,
            "maintenance": 2,
            "food": 2,
            "case_programs": 2,
            "health": 1,
            "other": 0,
        },
        "role_keywords": {
            "security": ["officer", "detention", "security", "case processing"],
            "intake_admin": ["records", "clerk", "case processing"],
            "transport": ["transport", "flight"],
            "leadership": ["supervisor", "administrator"],
            "maintenance": ["maintenance", "locksmith"],
            "food": ["food", "cook"],
            "case_programs": ["case manager", "recreation"],
            "health": ["nurse", "medical", "psych"],
        },
        "clusters": [
            {
                "id": "geo_conroe",
                "label": "GEO Conroe",
                "operator_source": "geo",
                "anchor": {"lat": 30.304, "lon": -95.458},
                "radius_miles": 40,
                "target_facilities": ["270TX - MONTGOMERY ICE PROCESSING CENTER"],
                "signal_category": "operating_stack",
                "acquisition_relevance": "high",
                "thesis_read": "test read",
            }
        ],
    }


def job(job_id, title, facility, lat, lon, source="geo", posted_date="2026-07-01"):
    return {
        "source": source,
        "operator": "GEO Group" if source == "geo" else "CoreCivic",
        "ticker": "GEO" if source == "geo" else "CXW",
        "job_id": job_id,
        "title": title,
        "category": "",
        "facility": facility,
        "city": "Conroe",
        "state": "Texas",
        "location": "Conroe, Texas",
        "lat": lat,
        "lon": lon,
        "posted_date": posted_date,
        "created_date": posted_date,
        "employment_type": "FULL_TIME",
        "url": f"https://example.test/{job_id}",
        "apply_url": "",
    }


class IceFacilityJobsMonitorTests(unittest.TestCase):
    def test_classify_roles_and_score_multi_signal_job(self):
        cfg = sample_config()
        roles = classify_roles(
            "Supervisor, Case Processing Specialist",
            "",
            cfg["role_keywords"],
        )

        self.assertEqual(set(roles), {"security", "intake_admin", "leadership"})
        self.assertEqual(role_score(roles, cfg["role_weights"]), 10)

    def test_haversine_and_cluster_assignment(self):
        cfg = sample_config()
        jobs = [
            job("1", "Detention Officer", "270TX - MONTGOMERY ICE PROCESSING CENTER", 30.304, -95.458),
            job("2", "Detention Officer", "Far Away", 35.0, -95.0),
        ]

        annotated = annotate_jobs(cfg, jobs)

        self.assertLess(haversine_miles(30.304, -95.458, 30.304, -95.458), 0.1)
        self.assertEqual(annotated[0]["clusters"][0]["id"], "geo_conroe")
        self.assertEqual(annotated[0]["clusters"][0]["match_type"], "target")
        self.assertEqual(annotated[1]["clusters"], [])

    def test_corecivic_normalization_preserves_lifecycle_and_raw_payload(self):
        normalized = normalize_corecivic_job(
            {
                "jobId": "req33600",
                "title": "Licensed Psychologist",
                "category": "Health Services",
                "facility": "California City",
                "city": "california city",
                "state": "CA",
                "location": "California City, CA",
                "latitude": "35.127",
                "longitude": "-117.985",
                "postedDate": "2026-07-04T00:00:00.000Z",
                "dateCreated": "2026-07-04T00:59:00.000Z",
                "openDateLocal": "2026-06-29",
                "expirationDate": "2026-08-27",
                "type": "Full-Time",
            }
        )

        self.assertIsNotNone(normalized)
        assert normalized is not None
        self.assertEqual(normalized["open_date"], "2026-06-29")
        self.assertEqual(normalized["expiration_date"], "2026-08-27")
        self.assertEqual(normalized["lifecycle_dates"]["openDateLocal"], "2026-06-29")
        self.assertEqual(normalized["raw_ats"]["jobId"], "req33600")

    def test_excluded_radius_context_does_not_drive_anomaly(self):
        cfg = sample_config()
        raw_jobs = [
            job("corp", "Product Manager", "BI Boulder Corporate", 30.304, -95.458),
            job("base", "Nurse", "Baseline A", 40.0, -95.0),
        ]
        annotated = annotate_jobs(cfg, raw_jobs)
        baselines = baseline_by_source(cfg, annotated)
        summaries = cluster_summaries(cfg, annotated, baselines, dt.date(2026, 7, 4))

        self.assertEqual(annotated[0]["clusters"][0]["match_type"], "excluded_context")
        self.assertEqual(summaries[0]["target_jobs"], 0)
        self.assertEqual(summaries[0]["excluded_context_jobs"], 1)
        self.assertEqual(summaries[0]["anomaly"], "low")

    def test_delta_first_run_and_new_jobs(self):
        cfg = sample_config()
        annotated = annotate_jobs(
            cfg,
            [job("1", "Detention Officer", "270TX - MONTGOMERY ICE PROCESSING CENTER", 30.304, -95.458)],
        )

        first = delta_from_state({}, annotated)
        second = delta_from_state({"active_job_keys": []}, annotated)
        later = delta_from_state({"active_job_keys": ["geo:old"]}, annotated)

        self.assertTrue(first["first_run"])
        self.assertTrue(second["first_run"])
        self.assertFalse(later["first_run"])
        self.assertEqual([j["key"] for j in later["new_jobs"]], ["geo:1"])
        self.assertEqual(later["gone_job_keys"], ["geo:old"])

    def test_cluster_summary_marks_broad_high_count_cluster(self):
        cfg = sample_config()
        raw_jobs = [
            job("1", "Detention Officer", "270TX - MONTGOMERY ICE PROCESSING CENTER", 30.304, -95.458),
            job("2", "Transportation Officer", "270TX - MONTGOMERY ICE PROCESSING CENTER", 30.304, -95.458),
            job("3", "Mailroom Clerk", "270TX - MONTGOMERY ICE PROCESSING CENTER", 30.304, -95.458),
            job("4", "Cook Supervisor", "270TX - MONTGOMERY ICE PROCESSING CENTER", 30.304, -95.458),
            job("5", "Registered Nurse", "270TX - MONTGOMERY ICE PROCESSING CENTER", 30.304, -95.458),
            job("6", "Maintenance Technician", "270TX - MONTGOMERY ICE PROCESSING CENTER", 30.304, -95.458),
            job("b1", "Nurse", "Baseline A", 40.0, -95.0),
            job("b2", "Nurse", "Baseline B", 41.0, -95.0),
        ]
        annotated = annotate_jobs(cfg, raw_jobs)
        baselines = baseline_by_source(cfg, annotated)
        summaries = cluster_summaries(cfg, annotated, baselines, dt.date(2026, 7, 4))

        self.assertEqual(summaries[0]["jobs"], 6)
        self.assertGreaterEqual(summaries[0]["role_breadth"], 5)
        self.assertEqual(summaries[0]["anomaly"], "high")


if __name__ == "__main__":
    unittest.main()
