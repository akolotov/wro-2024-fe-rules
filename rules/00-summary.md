# WRO Future Engineers Challenge 2024 Summary

## Core Challenge Overview
The WRO Future Engineers category features autonomous vehicle challenges where teams must build and program a self-driving car to navigate a track autonomously. The challenge consists of two main parts:

### 1. Open Challenge
- Vehicle must complete 3 laps on a track with random inner wall placements
- Track width varies between 600mm and 1000mm
- No traffic signs present

### 2. Obstacle Challenge
- Vehicle must complete 3 laps while following traffic sign rules
- Track width is fixed at 1000mm
- Features red and green traffic signs (pillars) that dictate lane positioning
- Red pillars must be passed on the right side
- Green pillars must be passed on the left side
- After second lap, vehicle determines direction for third lap based on last traffic sign color:
 - Green sign: continue in same direction
 - Red sign: perform U-turn and complete lap in opposite direction
- After completing laps, vehicle must perform parallel parking

## Game Field Elements

### 1. Basic Layout
- Inner racetrack size: 3000 x 3000 mm
- Main track color: White

### 2. Walls
- Exterior walls: 100mm height, black interior
- Interior walls: 100mm height, black color
- Wall configurations change based on randomization (Open Challenge only)

### 3. Track Sections
- 4 corner sections
- 4 straightforward sections
- 1 central section (non-functional)
- Each straightforward section divided into 6 zones

### 4. Traffic Signs
- Red and green pillars (50x50x100mm)
- Placed at designated intersections (T-intersections and X-intersections) at the corners of the central zones of the straightforward sections
- Must remain within 85mm diameter circles

### 5. Parking Zone (New for 2024)
- Width: 200mm
- Length: 1.25 times vehicle length
- Marked by magenta barriers (200x20x100mm)
- Positioned in straightforward sections

## Key Elements for Judging
- Vehicle size limits: 300x200x300mm
- Track randomization between rounds
- Driving direction randomly determined
- Specific rules for traffic sign placement
- Clear criteria for successful parking
- Points awarded for successful navigation, proper traffic sign handling, and parking

This challenge tests teams' abilities in computer vision, sensor fusion, autonomous navigation, and precise vehicle control while emphasizing engineering documentation and teamwork.