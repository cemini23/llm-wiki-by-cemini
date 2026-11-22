---
title: Printed Robot Arm Platforms — Open Hardware, Mass, and Modification
type: concept
related:
  - sources/arxiv-anthropomorphic-arm-charmie-2611.08013.md
  - entities/tools/rebot-devarm.md
  - entities/materials/pla.md
  - concepts/open-source-legged-robotics.md
  - sources/arxiv-2610.36598-openjaws-an-open-hardware-umi-framework-with-ste-2026-11-01.md
  - sources/arxiv-mobile-manipulator-robot-2611.22852.md
maturity: draft
updated: 2026-11-22
---

## Raw Concept

Opened on the 2026-11-10 ingest of @sources/arxiv-anthropomorphic-arm-charmie-2611.08013.md. Extends the printed-robotics material in @concepts/open-source-legged-robotics.md from legs to arms.

## Narrative

Two open printed arm designs now anchor this page. They sit at opposite ends of the same trade: how much of the load path do you print, and how much do you buy.

### Two designs

| Design | Load path | Printed parts | Material | Bought parts |
|---|---|---|---|---|
| Inmoov left arm (CHARMIE) | Servo brackets, linkages, hand | Whole arm and hand | PLA | 10 servos, Arduino Mega |
| reBot-DevArm | Bisected: metal where the load is, print elsewhere | Joint bases and covers | ABS and TPU 95+ | CNC aluminium 5052 for load-bearing links |

The Inmoov route prints everything and carries the load through PLA and servo horns. The reBot route splits the part: CNC aluminium in the load path, printed ABS in the structure. The reBot page carries the stricter methodology; this page adds the all-printed datapoint.

### The mass figure

The CHARMIE arm gives a whole-assembly mass that most papers omit.

| Item | Mass |
|---|---|
| Printed PLA parts | 1864 g |
| Ten servos | 804 g |
| Total arm | about 2700 g |

So the print is about 69% of the arm mass. At roughly 1.9 kg of PLA for one arm, a P1S print farm has a concrete capacity number: one arm is a multi-day build at a normal profile, and the mass is the reason.

### The modification loop

The most useful content in the CHARMIE paper is the four changes the authors made after the first print. Each one is a standard open-hardware experience:

1. The single-track servo pulley left the tendons slack, so the fingers moved imprecisely. A dual-track pulley fixed it.
2. Two small brackets were too small for the pot. The fix was a reprint at 100% larger.
3. The stock servo was too large. A smaller servo with similar torque replaced it, which forced new mounts.
4. A platform bracket was needed, so two new plates were designed and printed.

The lesson for a print farm is the cost of the second print. An open printed robot is a design-plus-iteration job, not a one-pass build. Budget two or three print cycles per part that touches a bought component.

### A third point: the printed part is only the end effector

The Auriga @Work robot adds a third shape of the same trade. Its chassis is aluminium profile and its arm uses worm-gear DC joints. Only the gripper and some brackets are printed. The arm reaches 65 cm and lifts about 450 g, so the printed part sits at the low-load end of the chain. [Source: arxiv-mobile-manipulator-robot-2611.22852.md p.4]

The paper gives no filament, printer, or process setting. Treat it as a structural datapoint only.

### Limits

Neither the arm paper nor the reBot page reports repeated-payload or fatigue testing of the printed links. The CHARMIE sensitivity check is a static FEA with a safety factor of 15 on the modified parts. PLA creeps under a sustained load and softens near its heat-deflection point. A printed arm that holds a pose for hours is not covered by that static number. [TENTATIVE]

## Snippets

> "This dissertation presents an open source 3D printed arm" [Source: arxiv-2611.08013-development-of-anthropomorphic-arm-for-collabora.pdf p.1]
