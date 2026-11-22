---
title: Auriga @Work — industrial mobile manipulator with a 3D-printed gripper
type: source
related:
  - concepts/printed-robot-arm-platforms.md
read_status: read
source_type: arxiv-paper
source_url: https://arxiv.org/abs/2611.22852
maturity: draft
created: 2026-11-22
updated: 2026-11-22
---

## Raw Concept

| Field | Value |
|-------|-------|
| Title | Technical Report of Mobile Manipulator Robot for Industrial Environments |
| Authors | Aria Dadnavi, Matin Jamshidi, Kian Khatibi, Shahriar Karimi Makhsous, Saina Najafi Shabestari, Seyed Sobhan Hosseini Hajibekandeh, Zahra Mahaam, Reyhane Mohasseli, Ghazal Ghoreishi, Amirhossein Gholizadeh Behbahani, Mohammad Hossein Moaiyeri |
| Affiliation | Team Auriga, Faculty of Electrical Engineering, Shahid Beheshti University, Tehran, Iran |
| Type | arXiv:2611.22852v1 [cs.RO], 17 November 2026, 25 pages |
| Location | `research to be indexed/3d-printing/arxiv-2611.22852-technical-report-of-mobile-manipulator-robot-for.pdf` |
| Retrieved | 2026-11-22 |
| Read status | read |

## Narrative

### What the paper is

The paper is a system report for the Auriga Robotics **@Work Robot**. The team built the robot for the RoboCup @Work league. The report covers mechanical design, electronics, firmware, ROS software, vision, and task execution.

The robot moves on four Mecanum wheels. It carries a 5-DOF arm with three links and a 3D-printed gripper. Custom ESP32 boards control the motors and sensors. An NVIDIA Jetson Orin NX runs the high-level software. [Source: arxiv-2611.22852-technical-report-of-mobile-manipulator-robot-for.pdf p.1]

### Where 3D printing appears

The chassis is aluminium profile. It measures 65 × 42 × 56 cm and weighs about 17 kg. The report says "several 3D-printed components and plates" were added to integrate the design. The gripper is the only part the abstract names as printed. [Source: arxiv-2611.22852-technical-report-of-mobile-manipulator-robot-for.pdf p.4]

The paper does not state the filament, the printer, the layer height, the infill, or the print orientation. It also gives no print time or part count. This ingest therefore records no FDM process data. [Source: arxiv-2611.22852-technical-report-of-mobile-manipulator-robot-for.pdf p.4]

### Arm and gripper numbers

| Item | Value |
|------|-------|
| Arm joints | 5 (three worm-gear DC joints, two servo joints) |
| Reach | 65 cm |
| Payload | about 450 g |
| Max joint speed | 40 deg/s; capped at 15 to 20 deg/s in the lab |
| Gripper actuation | two servo motors |
| Grip force sensing | load cell, 0.5 g resolution, 10 g threshold |

[Source: arxiv-2611.22852-technical-report-of-mobile-manipulator-robot-for.pdf p.4, p.7]

### Grasping results

The team ran 20 trials per object. A trial passed when the robot grasped, lifted, and placed the object without a drop.

| Object | Mass | Success rate |
|--------|------|--------------|
| Small aluminium profile | 50 g | 95% |
| Large aluminium profile | 185 g | 90% |
| M20 screw | 295 g | 80% |
| Steel axis | 160 g | 75% |
| Motor 755 | 320 g | 75% |
| Large nut M30 | 215 g | 55% |
| Drill | — | 50% |
| Small nut M20 | 55 g | 45% |
| Wrench | — | 45% |
| Bearing | 180 g | 40% |

[Source: arxiv-2611.22852-technical-report-of-mobile-manipulator-robot-for.pdf p.23] [TENTATIVE — one team, 20 trials per object, no confidence interval]

Long, straight profiles score high. Small round parts and thin bearings score low. The report does not separate gripper geometry from perception error as the cause.

### Software stack

The stack runs on ROS Noetic. Mapping and localization use Hector SLAM. Global path planning uses A*. Object detection uses YOLOv11s-Seg, fine-tuned on about 65,000 synthetic images plus about 6,000 real images. The report gives mAP50 near 0.995 and mAP50-95 of about 0.98 for boxes and 0.93 for masks. [Source: arxiv-2611.22852-technical-report-of-mobile-manipulator-robot-for.pdf p.14, p.17]

### Relevance to this wiki

The fit is weak. The paper is a robotics integration report. 3D printing is a small part of the build: a gripper and some brackets. No FFF process claim can be taken from it.

The one usable datapoint is structural. This arm follows the bisected trade that @concepts/printed-robot-arm-platforms.md records. The load path is bought metal and worm gearboxes. The printed part is the end effector, where geometry matters and load is low. A printed arm at this payload would need a different design.

## Snippets

> "It uses a 4-wheel Mecanum drive for omnidirectional movement and a 5-degree-of-freedom manipulator arm with a 3D-printed gripper for object handling and navigation." [Source: arxiv-2611.22852-technical-report-of-mobile-manipulator-robot-for.pdf p.1]

> "The chassis and base structure are built mainly from aluminum profiles … Several 3D-printed components and plates were also added to the structure for a more integrated, customized design." [Source: arxiv-2611.22852-technical-report-of-mobile-manipulator-robot-for.pdf p.4]

## Dead Ends

- Do not cite this paper as an FDM capability source. It states no material and no process settings.
- Do not compare its grasp rates with printed-gripper benchmarks. The perception stack is not separated from the gripper.
