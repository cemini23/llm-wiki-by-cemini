---
title: "OpenJaws: open 3D-printed UMI gripper with stereo localization"
type: source
tags: [source, arxiv, 3d-printed-gripper, umi, stereo-localization]
related: []
maturity: draft
read_status: skimmed
created: 2026-11-01
updated: 2026-11-01
---

## Raw Concept

| Field | Value |
|-------|-------|
| Title | OpenJaws: An Open Hardware UMI Framework with Stereo Localization for Generalist Manipulation |
| Authors | Adithyavairavan Murali et al. |
| arXiv | 2610.36598 |
| File | `arxiv-2610.36598-openjaws-an-open-hardware-umi-framework-with-ste.pdf` |
| Retrieved | 2026-11-01 |
| URL | https://arxiv.org/abs/2610.36598 |
| Read status | skimmed (abstract + intro) |

## Narrative

Handheld tools such as the Universal Manipulation Interface (UMI) collect manipulation demonstrations without a robot in the loop. The accuracy of vision-based localization bounds the quality of the action labels. The abstract says monocular visual-inertial odometry has scale ambiguity and drift. The abstract says closed-source tracking modules and external infrastructure add cost and setup burden.

OpenJaws is an open hardware and software framework for a sensorized UMI. A modular 3D-printed gripper carries a standardized ISO adapter and a low-cost stereo camera. The stereo camera recovers metric camera trajectories. The system overview shows robot-free collection on an actuated stereo gripper, then zero-shot transfer across robot bodies through a standardized mount.

The authors introduce UMI-Loc-Bench-v1. The benchmark measures real-world localization accuracy for handheld data-collection devices. The abstract states that stereo localization substantially outperforms monocular alternatives. That comparison is a single-source claim, and the abstract gives no error, drift, or success-rate number. The abstract also states that policies trained on OpenJaws data run on a real robot across multiple tasks. It gives no task count and no success count.

The overview figure labels wrench rotation, USB insertion, and kitting. It names the Flexiv Rizon 4s, YAM, and UR10, a Dynamixel actuator, and a Fin Ray finger. A second figure shows the recovered end-effector path and rectified stereo frames with SIFT matches. The caption says the fiducial cube serves OpenJaws and stays out of policy data collection. Hardware, software, and data ship under a commercially permissive license. The project site is https://open-jaws.github.io/.

For an FDM practitioner, the printed part is the modular gripper. The ISO adapter is the mount the paper uses to place that gripper on more than one robot arm. The Fin Ray finger is the printed compliant finger in the hardware overview. The supplied text states no filament, printer, or print settings. The introduction says leader-follower teleoperation, such as ALOHA and GELLO, needs a kinematic copy of the robot, and that UMI records relative end-effector motion so one dataset can serve more than one arm.

## Snippets

> "We present OpenJaws, a fully open hardware and software framework for sensorized UMI that improves localization and simplifies deployment across robot platforms. OpenJaws pairs a modular, 3D-printed gripper exposing a standardized ISO adapter with a low-cost stereo camera to recover metric camera trajectories." [Source: `arxiv-2610.36598-openjaws-an-open-hardware-umi-framework-with-ste.pdf` p.1 (arXiv 2610.36598), retrieved 2026-11-01]
