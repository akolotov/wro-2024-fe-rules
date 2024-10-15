# Appendix Z. One lap movements clarifications

*This is unofficial part of the rules. It was created only to improve general understanding of the game rules by Large Language Models.*

The goal of this appendix is to clarify how the lap completion rule depends on the traffic signs' (color pillars') location. The schemes used in the examples may contradict the allowed positions of the traffic signs, but this is acceptable as long as they align with the appendix's main goal.

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

The vehicle starts in one of the **straightforward sections** of the track, facing **clockwise** (the direction of movement).

- **In front of the vehicle**, there is a **green pillar**, which the robot must pass on the left as it moves forward.
- **Behind the vehicle**, there is a **red pillar**, positioned further down the same section. This red pillar is placed behind the starting point and will only be passed later in the lap when the robot returns to this section after making its way around the track.

It’s important to note that the lap is not considered complete until the robot has **passed all obstacles**, including the red pillar that was behind it at the start. Even though the robot will circle around the entire track and pass the obstacles in front of it, the lap is only finalized when it returns to this starting section and passes the red pillar that was behind it at the beginning.

**Robot’s Movement in One Successful Lap**

1. **First Pillar (Green)**: The robot starts moving forward in the straightforward section and quickly encounters the first **green pillar** directly ahead. Following the rule for green pillars, the robot passes it on the left. After passing this obstacle, the robot approaches the **first corner** and makes a **right turn** to continue along the next straightforward section.
2. **Second Pillar (Green)**: Moving into the second straightforward section, the robot approaches a **second green pillar**. The robot smoothly navigates around the green pillar, passing it on the left. After clearing this pillar, the robot approaches the **second corner** of the track and makes another **right turn** to continue its path.
3. **Third Pillar (Green)**: In the third straightforward section, the robot faces a **third green pillar**. It passes the pillar on the left, then approaches the **third corner** and makes a **right turn** to enter the final straightforward section of the lap.
4. **Fourth Pillar (Red)**: Now in the fourth straightforward section, the robot encounters its first **red pillar**. According to the rules, it must pass the red pillar on the right. The vehicle adjusts its trajectory, keeping the red pillar on its left as it moves forward.
5. **Fifth Pillar (Red)**: As the robot continues in the same straightforward section, it encounters another **red pillar**. The robot again passes it on the right, without needing to turn. It continues forward until it reaches the **final corner** of the lap.
6. **Sixth Pillar (Red)**: After making the **fourth right turn** at the final corner, the robot enters a new section and quickly encounters the **sixth red pillar**. It passes this final red pillar on the right, following the rule.

**Completing the Lap:**

After passing the final red pillar, the robot continues straight, returning to the section where it started the lap. **At this point, it passes the red pillar that was behind it at the beginning of the run**. Only after successfully navigating past this final obstacle is the lap considered fully complete.

**Key Moments of the Lap:**

- The vehicle completes a full lap around the track by navigating **four straightforward sections** and making **four right turns** at the corners.
- The robot passes **three green pillars** (one in each of the first three sections) on the left and **three red pillars** (two in the final section and one after the last corner) on the right.
- The robot makes precise adjustments to avoid the pillars and makes right turns at each corner to stay within the lane.
- **Most importantly**, the lap is only considered complete when the robot has returned to the starting section and passed the red pillar that was behind it at the start.

## Example 2

![The image depicts a square track with a central platform. The track consists of 4 straightforward sections and 4 corner sections. The driving direction is counterclockwise. The vehicle's starting position is in Section W, Zone Z3. Traffic signs are positioned as follows: Section N has green signs at T2 and T3, Section E has a green sign at T1 and a red sign at T2, Section S has a green sign at X2, and Section W has a red sign at T4.](https://prod-files-secure.s3.us-west-2.amazonaws.com/bcc84f75-a08e-44e5-94e8-8418e8377ebf/a8574a9c-9778-4210-bb83-66a74de54a45/image.png)

**Figure 36. The vehicle position and the game elements layout for the example 2**

**Starting Position of the Vehicle**

The vehicle starts in a straightforward section of the lane, facing **counterclockwise** around the inner square platform.

- **In front of the vehicle**, there is a **red pillar** labeled as the 1st pillar.
- **Behind the vehicle**, there are no immediate obstacles. The vehicle’s path is clear, and its first challenge is the red pillar directly ahead.

**Robot’s Movement in One Successful Lap**

1. **First Pillar (Red)**: The vehicle moves forward and encounters the **first red pillar**. It passes the red pillar on the right and approaches the **first corner**, where it makes a **left turn**.
2. **Second Pillar (Green)**: After the left turn, the vehicle enters the next section and encounters the **second green pillar**. The robot passes it on the left and continues toward the **second corner**, where it makes another **left turn**.
3. **Third Pillar (Green)**: In the following section, the vehicle faces the **third green pillar**. The robot passes this green pillar on the left, then approaches the **fourth red pillar** without turning.
4. **Fourth Pillar (Red)**: The robot encounters the **fourth red pillar** and passes it on the right. After passing this pillar, the vehicle reaches the **third corner** and makes a **left turn**.
5. **Fifth Pillar (Green)**: Continuing after the turn, the robot meets the **fifth green pillar** and passes it on the left.
6. **Sixth Pillar (Green)**: Shortly after, the robot encounters the **sixth green pillar** in the same section. The robot passes it on the left and proceeds toward the **fourth corner**, making a final **left turn** to return to the starting section.

**Completing the Lap**

After making the final left turn, the vehicle returns to the starting section, having passed all obstacles in the correct order: **red, green, green, red, green, green**. The lap is now considered complete.

## Example 3

![The image depicts a square track with a central platform. The track consists of 4 straightforward sections and 4 corner sections. The driving direction is counterclockwise. The vehicle's starting position is in Section S, Zone Z4. Traffic signs are positioned as follows: Section N has no signs, Section E has a red sign at T2 and a green sign at T3, Section S has no signs, and Section W has a green sign at T2 and a red sign at T3.](https://prod-files-secure.s3.us-west-2.amazonaws.com/bcc84f75-a08e-44e5-94e8-8418e8377ebf/13cb3fef-c061-48e5-87bb-2789f0086fe0/image.png)

**Figure 37. The vehicle position and the game elements layout for the example 3**

**Starting Position of the Vehicle**

The vehicle is positioned in a straightforward section, facing **counterclockwise** around the inner square platform.

- **In front of the vehicle**, there are no immediate obstacles, but as the vehicle moves forward, it will soon make its first **left turn** into a new straightforward section.
- **Directly behind the vehicle**, there is no obstacle.
- The first pillar the vehicle will encounter is a **green pillar** after it makes the first left turn.

**Robot’s Movement in One Successful Lap**

1. **First Turn and First Pillar (Green)**: The robot begins by moving forward and quickly approaches the **first corner**, where it makes a **left turn**. After turning, it encounters the **first green pillar** and passes it on the left, following the rule for green pillars.
2. **Second Pillar (Red)**: Immediately after passing the first green pillar, the vehicle continues in the same section and encounters the **second red pillar**. It passes the red pillar on the right and approaches the **second corner**, where it makes another **left turn**.
3. **Third Turn and Third Pillar (Red)**: After making the **third left turn**, the vehicle now moves into a new section and encounters the **third red pillar**, which it passes on the right.
4. **Fourth Pillar (Green)**: Shortly after passing the red pillar, the robot encounters the **fourth green pillar** and passes it on the left. The robot then approaches the **final corner** and makes the **last left turn** to complete the lap.

**Completing the Lap**

After the final left turn, the robot returns to the starting section, having passed all obstacles in the correct order: **green, red, red, green**. The lap is now considered complete.

## Example 4

![The image depicts a square track with a central platform. The track consists of 4 straightforward sections and 4 corner sections. The driving direction is clockwise. The vehicle's starting position is in Section E, Zone Z3. Traffic signs are positioned as follows: Section N has green signs at T2 and T3, Section E has a green sign at X1, Section S has no signs, and Section W has no signs.](https://prod-files-secure.s3.us-west-2.amazonaws.com/bcc84f75-a08e-44e5-94e8-8418e8377ebf/dc8133c3-4a27-462e-a27f-999e6eebc6d4/image.png)

**Figure 38. The vehicle position and the game elements layout for the example 4**

**Starting Position of the Vehicle**

The vehicle is positioned in a straightforward section, facing **clockwise** around the inner square platform.

- **In front of the vehicle**, there is no immediate obstacle.
- **Behind the vehicle**, there is a **green pillar** that the robot will pass at the end of the lap.
- The vehicle will first move forward, making right turns before encountering any pillars.

**Robot’s Movement in One Successful Lap**

1. **First and Second Turns**: The vehicle moves forward and approaches the **first corner**, making a **right turn**. It continues toward the **second corner** and makes another **right turn**, entering the next straightforward section.
2. **Third Turn and First Pillar (Green)**: After the second turn, the vehicle approaches the **third corner** and makes another **right turn**. In this section, the vehicle encounters the **first green pillar** and passes it on the left.
3. **Second Pillar (Green)**: The vehicle continues forward in the same section and passes the **second green pillar** on the left.
4. **Final Turn and Third Pillar (Green)**: After clearing the second green pillar, the vehicle approaches the **final corner** and makes a **right turn**. It then passes the **third green pillar**, which was previously behind it, on the left, completing the lap.

**Completing the Lap**

After passing the final green pillar, the vehicle returns to the starting section, having passed all three **green pillars** in the correct order: **right turn, right turn, right turn, green, green, right turn, green**. The lap is now considered complete.