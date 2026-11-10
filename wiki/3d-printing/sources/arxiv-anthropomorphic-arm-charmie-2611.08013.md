---
title: "Development of Anthropomorphic Arm for Collaborative and Home Service Robot CHARMIE (arXiv:2611.08013)"
type: source
related:
  - concepts/printed-robot-arm-platforms.md
  - entities/tools/rebot-devarm.md
  - entities/materials/pla.md
  - concepts/open-source-legged-robotics.md
maturity: draft
read_status: read
updated: 2026-11-10
---

## Raw Concept

| Field | Value |
|-------|-------|
| Title | Development of Anthropomorphic Arm for collaborative and Home Service Robot CHARMIE |
| Author | Hafiz Syed Fawad Adil, Tiago Ribeiro, Antonio Ribeiro, Carolina Lopes, Joana Coelho, Gil Lopes, Fernando Ribeiro (University of Minho, ISEP Porto) |
| Type | arXiv preprint (robotics dissertation) |
| Location | `research to be indexed/3d-printing/arxiv-2611.08013-development-of-anthropomorphic-arm-for-collabora.pdf` |
| Retrieved | 2026-11-10 |
| File | `arxiv-2611.08013-development-of-anthropomorphic-arm-for-collabora.pdf` |
| Read status | read |

## Narrative

The authors build and program a printed arm for CHARMIE, a home-service robot project. They start from the open-source **Inmoov** design, print the left arm and hand, and then modify the parts that failed.

### Print data

| Item | Value |
|---|---|
| Printer | Makerbot Replicator 2 |
| Material | PLA |
| Printed mass | **1864 g** |
| Motor mass | 804 g |
| Total arm mass | about **2700 g** |
| Degrees of freedom | 5 (Grubler's rule, 6 links, 5 joints) |

This is one of the few sources in the wiki that gives a **whole-assembly printed mass**. For a print farm, the number is directly useful: about 1.9 kg of PLA for one arm at full infill in the original part set.

### Four modifications, and why each was needed

| Change | Cause | Fix |
|---|---|---|
| Servo pulley | The single-track pulley left the finger tendons slack, so the fingers moved imprecisely | Replace with a **dual-track pulley**; rotate the tendon motors to keep the tendons taut |
| GearHolder and gearpotentio | Parts were too small for the elbow potentiometer | Reprint at **100% larger** scale |
| Elbow and arm-rotate servo | The Hitec HS-805BB was too large | Swap to the **TD-8125MG**, with similar torque in a smaller body; redesign the mounts |
| Mounting | New servos and a platform mount were needed | Two new plates designed in Autodesk Inventor, plus a new bracket that carries the arm, lift piston, and position potentiometer |

An FEA check on the parts returned a safety factor of **15**. The electronics use an Arduino Mega, chosen for its PWM pin count. Ten servos drive the arm: six MG996R for fingers and wrist, two TD-8125MG for elbow and arm rotation, two HS-805BB for shoulder lift and rotation.

### Control

Two control paths were built.

1. **Kinematics.** Denavit-Hartenberg parameters define the arm. The table was checked in MRPT before the Python controller ran.
2. **Vision teleoperation of the hand.** Google MediaPipe estimates the hand pose. A detection confidence of **0.7** was the usable setting: 0.5 shifted the pose at random, and values above 0.7 lost the hand in some lighting. Frame rate was **16 to 25 fps**. Finger angle comes from the dot product of two vectors. Wrist angle comes from the gradient between thumb and index landmarks. A three-sample averaging filter smooths the result.

### Honest limit

The paper reports assembly, kinematics, and a working teleoperation demo. It does not report pose accuracy, repeatability, or payload tests for the arm. The safety factor of 15 is a static FEA result on the modified parts, not a fatigue or impact result. Treat the printed PLA arm as a working demonstrator, not a validated service-robot manipulator.

## Snippets

> "The total mass of 3D print came out to be 1864 grams. The mass of the motors altogether is 804 grams. The total mass of the arm is about 2700 grams." [Source: arxiv-2611.08013-development-of-anthropomorphic-arm-for-collabora.pdf p.3]

> "Original pulley is a single-track pulley and as per assembly instructions, the tension in the tendons is not strictly taut which leads to loose tendons and imprecise movements." [Source: arxiv-2611.08013-development-of-anthropomorphic-arm-for-collabora.pdf p.2]
