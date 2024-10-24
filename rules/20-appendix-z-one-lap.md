# Appendix Z. **Clarification on Traffic Sign Passing Order and Last Sign Identification in a Lap**

*This is unofficial part of the rules. It was created only to improve general understanding of the game rules by Large Language Models.*

The goal of this appendix is to clarify how the identification of the last traffic sign (color pillar) of a lap depends on the signs' locations, the challenge's driving direction, and the vehicle's starting point. The schemes in this appendix also demonstrate the order of vehicle maneuvers based on these factors. While the schemes may contradict the allowed positions of traffic signs, they remain valid as long as they serve the appendix's main purpose.

## **Introduction**

The lap completion criteria are clearly defined in the game rules:

*8 sections were passed successfully in the challenge driving direction. The starting section is included in the eight sections for the first lap. The lap is considered complete if the vehicle completely drives out of the last (corner) section in the lap.*

However, the definition of the last traffic sign is missing. Understanding which sign is last is crucial, as the last sign of the second lap determines the direction for the third round. A green sign signals the robot to continue in the same direction, while a red sign requires the vehicle to turn around and complete the third round in the opposite direction.

Identifying the last traffic sign can be counter-intuitive when a sign is located in the starting section. Although the lap might be considered complete, that sign may not yet be passed. To avoid misinterpretation, the four examples below show the order of passing traffic signs during a lap, considering different combinations of sign locations, the vehicle's starting point, and the driving direction.

After reviewing these examples, the definition of the last traffic sign in a lap will be clear.

## **Game Field Description and Labeling**

Before examining the vehicle's behavior during the Obstacle Challenge with various traffic sign positions, it's essential to describe the game field and introduce labels. These labels will be used to encode the positions of traffic signs and the vehicle's starting point in the following schemes.

### General Game Field Description

The game field is is a square with dimensions of 3 meters by 3 meters, divided into 9 equal sections, each sized 1 meter by 1 meter. The sections are organized as follows:

1. **Corner Sections**:
    - There are 4 corner sections, located in the four outer corners of the mat. These sections are referred to as "C" in the schematic below.
2. **Straightforward Sections**:
    - There are 4 straightforward sections, which are linear and connect opposite corners. These sections are positioned as:
        - 2 horizontal straightforward sections (one above and one below the central section).
        - 2 vertical straightforward sections (one to the left and one to the right of the central section).
    - These sections are referred to as "S" in the schematic.
3. **Central Section**:
    - The middle section is non-functional and serves as the **central section**. This area is referred to as "###" in the schematic and remains unused during gameplay.

**Pseudographic Representation of the Game Mat**

To visually aid the understanding of the layout, here’s a pseudographic representation of the game mat:

```
+---+---+---+
|   |   |   |
| C | S | C |
|   |   |   |
+---+---+---+
| S |###| S |
|   |###|   |  Central Section (###)
|   |###|   |  (Unused during gameplay)
+---+---+---+
|   |   |   |
| C | S | C |
|   |   |   |
+---+---+---+
```

The vehicle moves in a **ring-shaped lane** around the central section, which forms a continuous loop, though the lane is not circular. The vehicle needs to make four right turns if the driving direction of the round is clockwise and four left turns if the driving direction is counterclockwise, one at each corner, to complete a full lap around the track.

**Labels for the straightforward sections**

- The section at the top is labeled "Section N"
- The section at the bottom is labeled "Section S"
- The section on the left is labeled "Section W"
- The section on the right is labeled "Section E"

```
+---+---+---+
|   |   |   |
|   | N |   |
|   |   |   |
+---+---+---+
| W |###| E |
|   |###|   |
|   |###|   |
+---+---+---+
|   |   |   |
|   | S |   |
|   |   |   |
+---+---+---+
```

### Straightforward Section Layout Description

Throughout the lane, there are **traffic pillars** placed at various points of the straightforward sections as obstacles.

Each straightforward section on the game mat has a structured layout, featuring the following elements:

1. **Radiuses**:
    - There are **three radiuses** within each straightforward section:
        - **Two radiuses** run vertically along the **left and right edges** of the section. They extend from the central section (top) toward the outer part of the field (bottom).
        - **One central radius** is positioned in the **middle** of the section, running vertically from the top to the bottom of the section.
    - These radiuses divide the section into two columns of zones.
2. **Arcs**:
    - There are **two arcs** that run horizontally across the section:
        - The arcs are positioned at two levels, creating divisions across the section horizontally.
        - These arcs do not connect the corner sections but instead divide the section into multiple zones horizontally.
3. **Intersections**:
    - The layout of radiuses and arcs forms multiple intersections, which can be used to place obstacles such as traffic signs:
        - **4 T-intersections**: These occur where the arcs meet the radiuses.
        - **2 X-intersections**: These occur where the central radius intersects with the arcs.
    - Each intersection is a potential location for placing obstacles that vehicles must navigate during the game.
4. **Zones**:
    - The combination of the two arcs and three radiuses divides the straightforward section into **6 zones**:
        - **Top and bottom zones** are taller and provide more space.
        - **Middle zones** are shorter, as they are compressed by the arcs.
    - These zones serve as key areas for gameplay, where obstacles can be placed or specific actions may occur.

**Pseudographic Representation of the Straightforward Section:**

```
radius  radius
v       v
+---+---+
|   |   |
|   |   |
|   |   |
+---+---+ - arc
|   |   |
|   |   |
+---+---+ - arc
|   |   |
|   |   |
|   |   |
+---+---+
    ^
    radius
```

In this schematic:

- The three radiuses (left, right, and middle) run vertically from the central section (at the top) to the outer part of the game field (at the bottom).
- The two arcs divide the section horizontally into three rows of zones, with the middle row being shorter than the top and bottom rows.
- The intersections formed by the radiuses and arcs serve as key locations for obstacle placement.

**Labels for the Intersection Points**

- Intersection points in the top row are labeled "T1", "X1", and "T2" from left to right.
- Intersection points in the bottom row are labeled "T3", "X2", and "T4" from left to right.

**Labels for the zones**

- Zones in the top row are labeled "Z1" and "Z2"
- Zones in the middle row are labeled "Z3" and "Z4"
- Zones in the bottom row are labeled "Z5" and "Z6"

```
+----+----+
|    |    |
| Z1 | Z2 |
|    |    |
T1---X1---T2
| Z3 | Z4 |
|    |    |
T3---X2---T4
|    |    |
| Z5 | Z6 |
|    |    |
+----+----+
```

## Example 1

![The image depicts a square track with a central platform. The track consists of 4 straightforward sections and 4 corner sections. The driving direction is clockwise. The vehicle's starting position is in Section W, Zone Z4. Traffic signs are positioned as follows: Section N has a green sign at T2, Section E has a green sign at X2, Section S has red signs at T3 and T4, and Section W has a green sign at T1 and a red sign at T4.](https://prod-files-secure.s3.us-west-2.amazonaws.com/bcc84f75-a08e-44e5-94e8-8418e8377ebf/c0c9aa90-ee00-4345-b39a-f4d17024cf96/image.png)

**Figure 35. The vehicle position and the game elements layout for the example 1**

**Starting Position of the Vehicle**

The vehicle starts in one of the straightforward sections of the track, facing clockwise (the direction of movement).

- The intersections immediately in front of the vehicle's starting zone are empty. This is intentional to avoid blocking or affecting the vehicle's initial movement.
- A green pillar is positioned in the intersection of the zone following the starting zone. From the vehicle's perspective, it's still ahead but the gap of one zone allows the robot to maneuver and pass the obstacle on the left.
- Behind the vehicle, in the intersection closest to the starting zone, there's a red pillar. This red pillar is positioned behind the starting point and will only be passed later in the lap when the robot returns to this section after completing its circuit around the track.

With this combination of starting zone and obstacle placement, lap completion and passing the last traffic sign occur simultaneously: as soon as the vehicle enters the straightforward section where it started, it will pass the red pillar.

**Robot’s Movement in One Successful Lap**

1. **First Pillar (Green)**: The robot starts moving forward in the straightforward section and encounters the first **green pillar** at the end of the section. Following the rule for green pillars, the robot passes it on the left. After passing this obstacle, the robot approaches the **first corner** and makes a **right turn** to continue along the next straightforward section.
2. **Second Pillar (Green)**: Moving into the second straightforward section, the robot approaches a **second green pillar**. The robot smoothly navigates around the green pillar, passing it on the left. After clearing this pillar, the robot approaches the **second corner** of the track and makes another **right turn** to continue its path.
3. **Third Pillar (Green)**: In the third straightforward section, the robot faces a **third green pillar**. It passes the pillar on the left, then approaches the **third corner** and makes a **right turn** to enter the final straightforward section of the lap.
4. **Fourth Pillar (Red)**: Now in the fourth straightforward section, the robot encounters its first **red pillar**. According to the rules, it must pass the red pillar on the right. The vehicle adjusts its trajectory, keeping the red pillar on its left as it moves forward.
5. **Fifth Pillar (Red)**: As the robot continues in the same straightforward section, it encounters another **red pillar**. The robot again passes it on the right, without needing to turn. It continues forward until it reaches the **final corner** of the lap.
6. **Sixth Pillar (Red)**: After making the **fourth right turn** at the final corner, the robot enters a new section and quickly encounters the **sixth red pillar**. It passes this final red pillar on the right, following the rule.

**Completing the Lap:**

After passing the final red pillar, the robot continues straight, returning to the section where it started the lap. As soon as the red pillar passed the lap is completed as well.

**The last traffic sign in the lap:**

The red pillar positioned in the starting section behind the vehicle is considered the last traffic sign of the lap. This is because the vehicle can only react to it (pass on the proper side) after completing the entire circuit.

## Example 2

![The image depicts a square track with a central platform. The track consists of 4 straightforward sections and 4 corner sections. The driving direction is counterclockwise. The vehicle's starting position is in Section W, Zone Z3. Traffic signs are positioned as follows: Section N has green signs at T2 and T3, Section E has a green sign at T1 and a red sign at T2, Section S has a green sign at X2, and Section W has a red sign at T4.](https://prod-files-secure.s3.us-west-2.amazonaws.com/bcc84f75-a08e-44e5-94e8-8418e8377ebf/a8574a9c-9778-4210-bb83-66a74de54a45/image.png)

**Figure 36. The vehicle position and the game elements layout for the example 2**

**Starting Position of the Vehicle**

The vehicle starts in a straightforward section of the track, facing counterclockwise around the inner square platform.

- The intersections directly in front of the vehicle's starting zone are empty, allowing unobstructed initial movement.
- A red pillar is positioned in the intersection of the zone ahead of the starting zone. This gap of one zone enables the robot to maneuver and pass the obstacle on the right.
- There are no obstacles behind the vehicle in the starting section.

**Robot’s Movement in One Successful Lap**

1. **First Pillar (Red)**: The vehicle moves forward and encounters the **first red pillar**. It passes the red pillar on the right and approaches the **first corner**, where it makes a **left turn**.
2. **Second Pillar (Green)**: After the left turn, the vehicle enters the next section and encounters the **second green pillar**. The robot passes it on the left and continues toward the **second corner**, where it makes another **left turn**.
3. **Third Pillar (Green)**: In the following section, the vehicle faces the **third green pillar**. The robot passes this green pillar on the left, then approaches the **fourth red pillar** without turning.
4. **Fourth Pillar (Red)**: The robot encounters the **fourth red pillar** and passes it on the right. After passing this pillar, the vehicle reaches the **third corner** and makes a **left turn**.
5. **Fifth Pillar (Green)**: Continuing after the turn, the robot meets the **fifth green pillar** and passes it on the left.
6. **Sixth Pillar (Green)**: Shortly after, the robot encounters the **sixth green pillar** in the same section. The robot passes it on the left and proceeds toward the **fourth corner**, making a final **left turn** to return to the starting section.

**Completing the Lap**

After completing the final left turn and crossing the boundary between the corner section and the straightforward section, the vehicle finishes the lap.

**The last traffic sign in the lap:**

The green pillar positioned at the end of the fourth straightforward section - considering the vehicle's counterclockwise movement - is the last traffic sign of the lap. The vehicle will pass this pillar on the proper side and then continue through the corner section to complete the lap.

## Example 3

![The image depicts a square track with a central platform. The track consists of 4 straightforward sections and 4 corner sections. The driving direction is counterclockwise. The vehicle's starting position is in Section S, Zone Z4. Traffic signs are positioned as follows: Section N has no signs, Section E has a red sign at T2 and a green sign at T3, Section S has no signs, and Section W has a green sign at T2 and a red sign at T3.](https://prod-files-secure.s3.us-west-2.amazonaws.com/bcc84f75-a08e-44e5-94e8-8418e8377ebf/13cb3fef-c061-48e5-87bb-2789f0086fe0/image.png)

**Figure 37. The vehicle position and the game elements layout for the example 3**

**Starting Position of the Vehicle**

The vehicle is positioned in a straightforward section, facing counterclockwise around the inner square platform. The intersections directly in front of the vehicle's starting zone are clear of obstacles. There are no obstacles behind the vehicle in the starting section.

**Robot’s Movement in One Successful Lap**

1. **First Turn and First Pillar (Green)**: The robot begins by moving forward and quickly approaches the **first corner**, where it makes a **left turn**. After turning, it encounters the **first green pillar** and passes it on the left, following the rule for green pillars.
2. **Second Pillar (Red)**: Immediately after passing the first green pillar, the vehicle continues in the same section and encounters the **second red pillar**. It passes the red pillar on the right and approaches the **second corner**, where it makes another **left turn**.
3. **Third Turn and Third Pillar (Red)**: After making the **third left turn**, the vehicle now moves into a new section and encounters the **third red pillar**, which it passes on the right.
4. **Fourth Pillar (Green)**: Shortly after passing the red pillar, the robot encounters the **fourth green pillar** and passes it on the left. The robot then approaches the **final corner** and makes the **last left turn** to complete the lap.

**Completing the Lap**

After completing the final left turn and crossing the boundary between the corner section and the straightforward section, the vehicle finishes the lap.

**The last traffic sign in the lap:**

The green pillar positioned at the end of the fourth straightforward section - considering the vehicle's counterclockwise movement - is the last traffic sign of the lap. The vehicle will pass this pillar on the proper side and then continue through the corner section to complete the lap.

## Example 4

![The image depicts a square track with a central platform. The track consists of 4 straightforward sections and 4 corner sections. The driving direction is clockwise. The vehicle's starting position is in Section E, Zone Z3. Traffic signs are positioned as follows: Section N has green signs at T2 and T3, Section E has a green sign at X1, Section S has no signs, and Section W has no signs.](https://prod-files-secure.s3.us-west-2.amazonaws.com/bcc84f75-a08e-44e5-94e8-8418e8377ebf/dc8133c3-4a27-462e-a27f-999e6eebc6d4/image.png)

**Figure 38. The vehicle position and the game elements layout for the example 4**

**Starting Position of the Vehicle**

The vehicle is positioned in a straightforward section, facing clockwise around the inner square platform.

- The intersections directly in front of the vehicle's starting zone are clear of obstacles.
- Behind the vehicle, in the intersection closest to the starting zone, there's a green pillar. This green pillar is positioned behind the starting point and will only be passed later in the lap when the robot returns to this section after completing its circuit around the track.

**Robot’s Movement in One Successful Lap**

1. **First and Second Turns**: The vehicle moves forward and approaches the **first corner**, making a **right turn**. It continues toward the **second corner** and makes another **right turn**, entering the next straightforward section.
2. **Third Turn and First Pillar (Green)**: After the second turn, the vehicle approaches the **third corner** and makes another **right turn**. In this section, the vehicle encounters the **first green pillar** and passes it on the left.
3. **Second Pillar (Green)**: The vehicle continues forward in the same section and passes the **second green pillar** on the left.
4. **Final Turn and Third Pillar (Green)**: After clearing the second green pillar, the vehicle approaches the **final corner** and makes a **right turn**. It then passes the **third green pillar**, which was previously behind it, on the left, completing the lap.

**Completing the Lap**

After completing the final right turn and crossing the boundary between the corner section and the straightforward section, the vehicle finishes the lap. The green pillar in this straightforward section is positioned in the middle. Therefore, the lap is considered complete before the vehicle passes the pillar (assuming the vehicle's length is less than the distance between the section boundary and the pillar).

**The last traffic sign in the lap:**

The green pillar positioned in the starting section behind the vehicle is considered the last traffic sign of the lap. This is because the vehicle can only react to it (pass on the proper side) after completing the entire circuit.

## Summary and Conclusions

After examining various scenarios of vehicle movement and traffic sign placement, the following conclusions can be drawn:

### 1. Lap Completion

It's crucial to distinguish between lap completion as defined in the game rules and the completion of a full circuit around the track. A lap is considered complete when the vehicle fully exits the last (corner) section in the lap and enters the straightforward section where it started. This definition is based on the discrete nature of the track, composed of corner and straightforward sections.

**Aplicability**

The definition of lap completion is applied in several important cases within the game rules:

- To award points for lap completion, the lap must be fully completed by the vehicle crossing entirely into the starting section.
- To allow the vehicle to begin moving in the opposite direction after the second lap (if the last traffic sign is red), the vehicle must fully cross the boundary into the starting section at the end of the second lap.
- To permit the vehicle to proceed to the parking lot after the third lap, the vehicle must first completely cross into the starting section upon finishing the third lap.

### 2. The Last Traffic Sign in a Lap

The last traffic sign in a lap is defined as the final traffic sign that the vehicle must react to (by passing it on the correct side) before completing its full circuit around the track. This concept requires a more granular view of the track, considering the 12 radiuses where obstacles can be placed. The vehicle's path in relation to these radiuses determines which sign is truly the last one in the lap.

**Important note**: The physical completion of the lap (crossing the boundary into the starting section) may occur either before or after passing the last traffic sign, depending on the specific layout of the course and the placement of the signs.

This distinction between lap completion and full circuit completion is crucial because:

a) It allows for a more precise definition of the last traffic sign, which may be located in the starting straightforward section or the straightforward section immediately before it.
b) It accounts for scenarios where signs are placed behind the vehicle's initial starting position or in sections that might seem counterintuitive when considering only the discrete lap completion definition.

These definitions ensure consistent interpretation across various track configurations, driving directions, and sign placements.

**Aplicability**

Determining the last traffic sign in a lap is critical in one specific scenario:

- It helps to establish the correct direction the vehicle should take when starting the third lap, once the second lap has been physically completed.