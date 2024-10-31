# Questions and answers

This section contains questions and answers related to the World Robot Olympiad Future Engineers competition rules for the 2024 season. The Q&As provide additional clarification and interpretation of the official rules to assist in resolving ambiguities or edge cases that may arise during competition preparation or execution. While not part of the official game rules, these Q&As reflect the intent behind the rules and should be considered authoritative guidance for teams, judges, and other stakeholders involved in the competition. The information here supplements the main game rules and should be used in conjunction with the official rules to ensure consistent application and understanding across all competition events.

## Vehicle Design

### Use of Electronic Differentials in Vehicle Design

Q: Is it permissible to use an electronic differential in our vehicle design for the WRO Future Engineers competition? An electronic differential would allow independent control of motor torque for each driving wheel based on steering input and desired overall torque.

A: No, the use of electronic differentials is not permitted in the WRO Future Engineers competition. This decision is based on several factors:

- The competition rules require a physical connection between the driving wheels, which an electronic differential does not provide.
- The rules specify "one driving axle," implying a mechanical linkage between wheels rather than independent electronic control.
- There are concerns about verifying whether an electronic differential is being used solely for steering compensation or as a differential drive system, which could potentially violate the rule against differential wheeled robots.
- To ensure fairness and clarity in judging, especially at the International Final level, such systems are not allowed.

## Before the round starts

### Vehicle Starting Positions in Open and Obstacle Challenges

Q: What are the allowed starting positions for vehicles in the Open and Obstacle challenges?

A: The starting positions differ between challenges:

- Open Challenge: Vehicle can start from any of the 6 positions in the starting section (outside the inner wall)
- Obstacle Challenge: Vehicle must start from one of the 2 middle positions, determined by traffic sign placement to avoid direct frontal obstruction

### Maximum Number of Traffic Signs

Q: What is the maximum number of traffic signs (pillars) allowed in a round?

A: While rule 13.20 mentions up to 7 red and 7 green pillars, the practical implementation limits this to a maximum of 7 pillars total per round, with no more than 2 pillars per straightforward section.

### Clear Path at Vehicle Start

Q: Can traffic signs be placed directly in front of a vehicle's starting position?

A: No, traffic signs will not be placed directly in front of a vehicle's starting position in the direction of movement.

This rule is designed to help teams avoid immediate failures at the start of their run and to ensure a fair beginning for all participants. It allows each vehicle to have a clear initial path as it begins its movement.

Key points to note:

1. While traffic signs may be present in various parts of the starting section, they will not obstruct the vehicle's initial path.
2. The challenge of navigating around traffic signs begins after the vehicle starts moving, not at the moment of initialization.
3. For the International Final, specific procedures will be in place to guarantee that vehicles start from zones without traffic signs directly in front of them.

### Parking Lot Placement in Start Section

Q: Can the parking lot be located in the same section as the starting position?

A: Yes, there are no rules prohibiting the parking lot from being in the same section as the starting position.

### Parking Lot Alignment

Q: Should the alignment of the parking lot (left/right) within its sec  tion be randomized?

A: According to the rules, the parking lot should always be aligned with its right element next to the dotted line of the section. The randomization process is only used to determine in which sections the parking lot will be placed, not its alignment within the section.

## During the round

### Obstacle Challenge: Scoring Time vs Round Time

Q: How is time measured in the Obstacle Challenge round?

A: For the Obstacle Challenge rounds, two separate time measurements will be used:

**Scoring Time:** This is the time that will be recorded for scoring purposes and used for tiebreaking as per rule 10.8.3. The scoring time starts when the round begins and stops when:

- The vehicle completes three laps and comes to a complete stop in the finish section (the straightforward section where the vehicle started)
- The vehicle remains completely stationary for 5 consecutive seconds
- The vehicle's projection is completely within the finish section as defined in Appendix A, section 2

**Round Time:** This is the overall time limit for the entire challenge attempt, including parking. The round time:

- Starts when the round begins
- Must not exceed 3 minutes as per rule 9.1
- Continues running during the 5-second stop period
- Continues during the parking attempt
- Stops when any of the conditions in rule 9.24 are met

If the vehicle moves during the required 5-second stop period, the 3 points for stopping in the finish section (rule 1.3) will not be awarded. After the 5-second stop period, the vehicle must proceed to attempt parking in the designated parking lot while still respecting the overall 3-minute round time limit.

### The Last Traffic Sign in a Lap

Q: How to identify which traffic sign should be considered the last one in a lap when there are multiple signs on the track, particularly when signs are placed in different sections including the starting section?

A: The last traffic sign in a lap is defined as the final traffic sign that the vehicle must react to (by passing it on the correct side) before completing its full circuit around the track. This may not coincide with the technical completion of the lap, as the vehicle might need to pass a traffic sign in the starting section that was initially behind its starting position. The key is that while a lap may be considered complete when crossing certain boundaries, the last traffic sign is determined by the final sign the vehicle must properly respond to in its path around the circuit.

### Direction Change Rules After Red Sign on Second Lap

Q: What are the direction change rules when a vehicle encounters a red traffic sign as the last sign of the second lap?

A: When a vehicle encounters a red traffic sign as the last sign of the second lap:
Required Behavior:

1. The vehicle must first complete the second lap by fully crossing into the starting section
2. After completing the second lap, the vehicle should change its driving direction to the opposite of its current direction:

- If driving clockwise, should switch to counterclockwise
- If driving counterclockwise, should switch to clockwise

If Error Occurs:

- The round will continue without interruption
- The vehicle may detect and correct its direction at any point during the third lap
- Points are awarded based on the direction at lap completion:
  - 15 points awarded if the final lap is completed in the correct direction
  - 0 points awarded if the final lap is completed in the wrong direction

The vehicle has the entire third lap to detect and correct any direction errors to earn the direction points.

### Points Scoring for Incorrect Final Lap Direction

Q: In the Obstacle Challenge, if a vehicle completes three laps but drives the final lap in the wrong direction, does it earn any points or should it be stopped?

A: The vehicle should not be stopped and can still earn points even when driving the final lap in the wrong direction. Available points include:

- Points for completing the first two laps
- Up to 8 points for sections visited during the third lap
- 1 point for completing the third lap
- Points for correct handling of traffic signs throughout all laps
- Points for successful parking

The only penalty is not receiving the 15 points awarded for completing the final lap in the correct direction.

### Scoring Interpretation for Moved Pillars

Q: In the scoring section, items 1.4-1.7 refer to whether traffic signs were "moved" or "not moved". At the same time, Appendix A shows different situations of traffic sign displacement. How should judges evaluate if a traffic sign is considered "moved" for scoring purposes, and how does this relate to the round stopping conditions described in Appendix A?

A: The rules distinguish between different levels of traffic sign displacement:

1. If a traffic sign remains exactly in its original position (not touched by the vehicle), this is considered "not moved" and receives maximum points (items 1.5 or 1.7 in scoring).
2. If a traffic sign is touched or slightly displaced by the vehicle, but its projection on the game mat still touches the evaluation circle (85mm diameter), this is considered "moved" for scoring purposes and receives reduced points (items 1.4 or 1.6 in scoring), but the round continues. This includes cases where the sign is off its original seat but its projection still touches the circle.
3. If a traffic sign is pushed so that its projection on the game mat is completely outside its evaluation circle, this is considered a significant displacement and causes the round to stop immediately (as per rule 9.24.6).

### Traffic Sign Movement After Completing Laps

Q: Does moving an obstacle outside its designated circle after completing three laps, while en route to the parking area, stop the round and prevent the awarding of points for completing the third lap in the correct direction?

A: Moving a traffic sign outside its designated circle during the route to parking will stop the Round Time and end the attempt immediately as per rule 9.24.6. However, since this occurs after the Scoring Time has already stopped (which happened when the vehicle completed three laps and came to a complete stop), it will not affect the points already earned for completing the three laps in the correct direction.

Since a traffic sign was moved after the completion of three laps, the team will receive 8 points according to scoring item 1.6 instead of 10 points from item 1.7. The points for completing the final lap in the correct direction (15 points) remain secured, but no parking points will be awarded due to the round ending before successful parking.

## Parking Lot

### Touching Parking Barriers: Round Stopping Conditions

Q: In the Obstacle Challenge, if the vehicle touches the parking barriers during the first three laps, does this immediately stop the round?

A: If the vehicle touches the parking barriers at any point during the round, including during the first three laps, the round will be stopped immediately. According to the rules (9.24.7), touching the parking lot limitations is listed as one of the conditions that ends the round. This applies throughout the entire round, not just during the parking attempt.

### Last Traffic Sign in a Lap Passing Before Parking

Q: After completing three laps, if there is a traffic sign in the Start Section behind the vehicle's starting zone, must the vehicle pass this traffic sign before proceeding to the parking lot?

A: According to Appendix A, sections 2 and 3, a vehicle is considered to have finished within the starting section when its projection is completely within the section. Therefore, the vehicle:

- Must enter Start Section completely after three laps
- Must stop for 5 seconds anywhere within Start Section
- Can then proceed directly to the parking lot without passing the last traffic sign in a lap

### Path to Parking After Three Laps Completion

Q: In the Obstacle Challenge, after completing three laps, can the vehicle take any path to reach the parking lot, or must it continue in the same driving direction as the third lap?

A: After completing three laps correctly, the vehicle may choose any path to reach the parking lot.

### Parking Points and Touching Limitations

Q: Do teams get any parking points if their robot touches the parking lot limitations during the parking process?

A: According to section 6 of Appendix A in the rules, if the robot touches any of the parking lot limitations (the magenta barriers), the round will be stopped and no points for parking can be scored, regardless of whether the robot was fully or partly in the parking area before touching the limitations. The robot must complete its parking maneuver without making contact with these barriers to earn either the full 15 points (for being completely in the parking area) or 7 points (for being partly in the parking area).
