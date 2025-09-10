# FIRA Air Autonomous Race U19

This repository contains my implementation for the **FIRA Air Autonomous Race (U19 category)**. The project uses a real **DJI Tello drone** equipped with external image processing to autonomously detect gates and complete the race track.

## Competition Goals

The objective of the FIRA Air Autonomous Race is to develop drones capable of completing a race track without human intervention. The main requirements include:

- Autonomous detection of gates using computer vision  
- Navigation through each gate in the correct sequence  
- Completion of the track without faults  
- Achieving the fastest possible time compared to competitors  

This challenge emphasizes the integration of programming, robotics, and vision-based navigation.

## Technical Approach

The implementation in this repository focuses on:

- **Image Processing with AprilTags**: Using a camera feed to detect AprilTags placed on race gates  
- **Drone Control with DJI Tello**: Sending movement commands (yaw, pitch, roll, throttle) to the Tello drone based on vision input  
- **Gate Navigation**: Aligning with each gate and passing through in the correct order  
- **Autonomous Flight Sequence**: Coordinating detection, decision-making, and control to complete the race track  

## Code Overview

The main script, [`fira_air.py`](./fira_air.py), connects to the Tello drone, streams video, and processes each frame to detect AprilTags marking the race gates. Based on the tag’s position and orientation, the code computes alignment and distance adjustments, then issues control commands to the drone.  
It works as a simple state machine: searching for tags, aligning with the gate, and flying through it. A live video feed with visualized detections is displayed for debugging, and the program ensures the drone lands safely when stopped.

## Future Work

Potential improvements include:

- Enhancing vision algorithms for faster and more reliable gate detection  
- Implementing adaptive control strategies for smoother navigation  
- Optimizing the system for reduced latency between perception and control  

---

This repository documents my work in the FIRA Air U19 competition, where the goal is to demonstrate reliable and efficient autonomous drone racing.
