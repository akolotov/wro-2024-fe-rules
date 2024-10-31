# WRO Future Engineers Challenge 2024 Summary

## Competition Overview

The WRO Future Engineers category challenges teams to build and program autonomous vehicles that can navigate a track without any human intervention during rounds. The competition tests teams' abilities in computer vision, sensor fusion, autonomous navigation, and precise vehicle control while emphasizing engineering documentation and teamwork.

## Glossary

- **WRO:** WRO stands for World Robot Olympiad Association Ltd., the non-profit organization running WRO worldwide and that prepares all the game and rule documents.
- **Competition Organizer:** The competition organizer is the entity that hosts the competition a team is visiting. This can be a local school, the National Organizer of a country that runs the National Final, or a WRO Host Country together with WRO Association running the International WRO Final.
- **Competition:** The competition consists of several rounds. It is recommended to have two rounds for Open Challenge and two rounds for Obstacle Challenge. The number of rounds in the competition is determined by the competition organizer.
- **Judge:** A person who is responsible for overseeing the competition and ensuring that the rules are followed. Judges are also responsible for measuring the round time and score of the vehicles.
- **Autonomous Vehicle:** A four-wheeled vehicle that navigates through the game field independently after being started, with no remote control or human intervention during the round. The vehicle must comply with specific technical requirements (e.g., drive system) and may only use onboard sensors and processors for navigation, reflecting real-world autonomous vehicle principles of perception, decision-making, and control.
- **Round:** A team runs an autonomous vehicle to complete the task of the challenge. The challenge score is based on the amount of laps the vehicle drives on the game field and the ability of the vehicle to avoid obstacles and to park in the parking zone.
- **Round Time:** Judges measure the amount of time the vehicle drives on the game field to partially or fully complete the challenge.
- **Check Time:** During the check time, the judge will look at the vehicle and check the measurements (e.g., with a cube or a folding rule) and other technical requirements. A check needs to be done before every round.
- **Practice Time:** During the practice time, the team can test the vehicle on the field and the team can change mechanical aspects or the coding of the vehicle. The practice needs to be done before every round and before the check time.
- **Open Challenge:** The challenge where the vehicle must complete 3 laps on a track with random inner wall placements. The challenge is made relatively easy by intent, to allow teams to be scored even if they do not have a perfect autonomous navigation system.
- **Obstacle Challenge:** The challenge where the vehicle must complete 3 laps avoiding obstacles. After completion of three laps, the vehicle navigates to the parking zone and performs parking.
- **Game Field:** The square area which the vehicle must navigate within. The area may contain objects the vehicle must interact with as per the competition requirements. The game field models a racetrack which consists of corner sections and straightforward sections forming a continuous circuit. Outer and inner walls are used to bound the racetrack.
- **Outer Wall:** The wall that bounds the game field.
- **Inner Wall:** The wall surrounding the internal (non-functional) section of the track.
- **Corner Section:** One of four sections located at the corners of the game field where the vehicle must turn to continue its path.
- **Straightforward Section:** One of four sections connecting corner sections where the vehicle drives in a straight line and where traffic signs and parking barriers may be placed as per randomization.
- **Randomization:** The official process, performed by judges after check time, of determining various game elements' positions and configurations for each round. This ensures unpredictability and tests vehicles' true autonomy.
- **Driving Direction:** The direction in which the vehicle must move during the challenges. This is determined through the randomization. Also known as _Challenge Driving Direction_.
- **Traffic Sign:** A colored pillar used in the Obstacle Challenge to check the vehicle's ability to avoid obstacles. One or two traffic signs are placed in designated seats of the straightforward sections as per randomization.
- **Parking Barrier:** Two colored barriers used in the Obstacle Challenge to specify the start and end of the parking lot. Two barriers are also known as _Parking Limitations_.
- **Parking Lot:** The area in the game field where the vehicle must park after completion of three laps. Positioned in the straightforward sections as per randomization. Also known as _Parking Zone_.
- **Starting Section:** The section where the vehicle starts the challenge. Determined through the randomization.
- **Starting Zone:** The zone of the starting section where the vehicle must start the challenge. Determined through the randomization.
- **Lap:** Passing eight sections successfully in the challenge driving direction, starting from and returning to the starting section. Applicable for both Open and Obstacle Challenges.
- **Full Circuit:** A complete path around the track where the vehicle has passed all traffic signs it encounters, which may extend beyond the completion of a discrete lap. Applicable in the Obstacle Challenge.
- **Moved Traffic Sign:** A traffic sign whose projection on the game field extends beyond the 85mm diameter circle surrounding its designated traffic sign seat (50x50mm).
- **Traffic Sign Passing Rule:** The requirement that during the Obstacle Challenge, the vehicle must completely pass each traffic sign on a specific side depending on the sign's color. A red pillar must be passed on the vehicle's right side, while a green pillar must be passed on the vehicle's left side.

### Competition Structure
- Multiple rounds divided between Open Challenge and Obstacle Challenge
- Each round includes:
  - Practice time for testing and adjustments
  - Check time for vehicle inspection
  - Challenge attempt with scored performance
- Random elements (driving direction, starting position, obstacle placement) determined after check time

## Technical Requirements

### Vehicle Specifications
- Size: Maximum 300x200x300mm
- Weight: Maximum 1.5kg
- Must be four-wheeled with one driving axle and one steering actuator
- Fully autonomous operation (no remote control)
- On-board sensors and processing only

## Game Field

### Basic Layout
- Inner racetrack: 3000x3000mm
- Track surface: White
- Four corner sections for turning
- Four straightforward sections for linear movement
- One non-functional central section

### Field Elements
- Exterior walls: 100mm height, black interior
- Interior walls: 100mm height, black color
- Traffic sign seats: 50x50mm marked areas in straightforward sections
- Evaluation circles: 85mm diameter around traffic sign seats
- Parking zone: 200mm width, length = 1.25 × vehicle length

## Challenges

### Open Challenge
- Complete 3 laps autonomously
- Random inner wall placements
- Track width varies (600-1000mm)
- Points awarded for:
  - Successful section navigation
  - Lap completion
  - Final positioning

### Obstacle Challenge
- Complete 3 laps while following traffic sign rules
- Fixed track width (1000mm)
- Traffic signs:
  - Red pillars: Must pass on right side
  - Green pillars: Must pass on left side
- Direction change after second lap based on last sign:
  - Green: Continue same direction
  - Red: U-turn and reverse direction
- Parking required after lap completion
- Points awarded for:
  - Successful navigation
  - Proper traffic sign handling
  - Maintaining traffic signs in position
  - Parking execution

### Key Scoring Elements
- Lap completion requires passing 8 sections in challenge driving direction
- Traffic signs considered "moved" if extending beyond 85mm evaluation circle
- Parking assessed based on vehicle position relative to barriers
- Documentation and engineering process evaluated separately

## Additional Requirements
- Teams must maintain public GitHub repository
- Engineering documentation required
- Video demonstrations of vehicle performance
- Team photos and technical descriptions
