# Appendix Y. Randomization clarifications

*This is unofficial part of the rules. It was created only to improve general understanding of the game rules by Large Language Models.*

The goal of this appendix is to clarify what the rules are for how the game objects (walls, traffic signs, parking limitations and the vehicle's starting zone) are determined for every round.

## Game Mat elements for randomization

Before describing the randomization process, it's necessary to assign labels to the game mat elements. These labels will be used in the randomization process. 

### General Game Mat description

The game mat is a square with dimensions of 3 meters by 3 meters, divided into 9 equal sections, each sized 1 meter by 1 meter. The sections are organized as follows:

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

**Important Notes:**

- The game mat consists only of the sections described above, with no built-in walls or obstacles.
- **Walls**: Outer and inner walls are additional game elements that are placed around or on the mat during the game, but they are not part of the mat itself.
- The **outer walls** typically run along the edges of the mat, while **inner walls** can be configured in various ways, potentially enclosing the central section, but these walls are separate from the mat structure.

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

## **Randomization for Open Challenge rounds**

After choosing the direction to drive the track the following procedure could be used to determine the car starting point and the distance between the track borders:

1. Flip a coin twice to determine the starting section. The following combinations correspond to specific sections:
    - Heads & heads: The vehicle starts from Section N
    - Heads & tails: The vehicle starts from Section E
    - Tails & heads: The vehicle starts from Section W
    - Tails & tails: The vehicle starts from Section S
2. Toss a coin four times to determine which sections will have reduced distance between track borders. The first toss is for the starting section, with subsequent tosses moving clockwise. Heads indicates a wide corridor; tails indicate a narrow corridor.
    
    Examples:
    
    - The vehicle starts from Section E. The coin tosses result in "tails-heads-tails-tails," causing:
        - Section E: narrow corridor
        - Section S: wide corridor
        - Section W: narrow corridor
        - Section N: narrow corridor
    - The vehicle starts from Section S. The coin tosses result in "heads-heads-tails-tails," causing:
        - Section S: wide corridor
        - Section W: wide corridor
        - Section N: narrow corridor
        - Section E: narrow corridor
3. Roll a die to determine the exact starting zone. Zone Z1 corresponds to a roll of "1", while zone Z6 corresponds to a roll of "6". If the rolled zone is inside the border wall, roll the die again.

This procedure will be performed after the check time before every Open Challenge round so the starting position of the car and the distances between the track borders will be different in every challenge round.

## **Randomization for Obstacle Challenge rounds**

During Obstacle Challenge rounds, red and green pillars serve as traffic signs on the track. The distance between track borders remains constant at 1000 mm.

The starting position of the vehicle, the locations of the colored pillars, and the position of the parking lot can be determined using the following procedure (assuming the round's driving direction has been established separately):

1. Toss a coin twice to determine the section where the parking lot will be located. The following combinations correspond to specific sections:
    - Heads & heads: The parking lot is placed in Section N
    - Heads & tails: The parking lot is placed in Section E
    - Tails & heads: The parking lot is placed in Section W
    - Tails & tails: The parking lot is placed in Section S
2. Toss a coin twice to determine the section where the single traffic sign will be located. The following combinations correspond to specific sections:
    - Heads & heads: The traffic sign is placed at intersection X2 of Section N
    - Heads & tails: The traffic sign is placed at intersection X2 of Section E
    - Tails & heads: The traffic sign is placed at intersection X2 of Section W
    - Tails & tails: The traffic sign is placed at intersection X2 of Section S
3. Flip a coin once to determine the color of the traffic sign in the section defined in the previous step. Heads indicates a green sign; tails indicates a red sign.
4. Get 36 cards as listed below and remove either card 9 or 10 from the set, depending on the color of the sign chosen in the previous step: if green was chosen, remove the 9th card; if red was chosen, remove the 10th card. Place the remaining 35 cards into a non-transparent box or bag. Draw one card from the box—this will determine the locations of the traffic signs in the straightforward section immediately after (clockwise) the section determined in the previous step. Do not return this card to the box. Draw a second card—this will determine the locations of the traffic signs in the next straightforward section. Repeat this process for the remaining straightforward sections. For the section containing the parking lot, only cards 1-6 and 25-30 should be used.
    - Card #1: Green sign at intersection T1
    - Card #2: Red sign at intersection T1
    - Card #3: Green sign at intersection X1
    - Card #4: Red sign at intersection X1
    - Card #5: Green sign at intersection T2
    - Card #6: Red sign at intersection T2
    - Card #7: Green sign at intersection T3
    - Card #8: Red sign at intersection T3
    - Card #9: Green sign at intersection X2
    - Card #10: Red sign at intersection X2
    - Card #11: Green sign at intersection T4
    - Card #12: Red sign at intersection T4
    - Card #13: Green signs at intersections T3 and T2
    - Card #14: Green sign at intersection T3, red sign at intersection T2
    - Card #15: Red sign at intersection T3, green sign at intersection T2
    - Card #16: Green sign at intersection T3, red sign at intersection T2
    - Card #17: Red sign at intersection T3, green sign at intersection T2
    - Card #18: Red signs at intersections T3 and T2
    - Card #19: Green signs at intersections T1 and T4
    - Card #20: Green sign at intersection T1, red sign at intersection T4
    - Card #21: Red sign at intersection T1, green sign at intersection T4
    - Card #22: Green sign at intersection T1, red sign at intersection T4
    - Card #23: Red sign at intersection T1, green sign at intersection T4
    - Card #24: Red signs at intersections T1 and T4
    - Card #25: Green signs at intersections T1 and T2
    - Card #26: Green sign at intersection T1, red sign at intersection T2
    - Card #27: Red sign at intersection T1, green sign at intersection T2
    - Card #28: Green sign at intersection T1, red sign at intersection T2
    - Card #29: Red sign at intersection T1, green sign at intersection T2
    - Card #30: Red signs at intersections T1 and T2
    - Card #31: Green signs at intersections T3 and T4
    - Card #32: Green sign at intersection T3, red sign at intersection T4
    - Card #33: Red sign at intersection T3, green sign at intersection T4
    - Card #34: Green sign at intersection T3, red sign at intersection T4
    - Card #35: Red sign at intersection T3, green sign at intersection T4
    - Card #36: Red signs at intersections T3 and T4
    
    *Some cards are intentionally duplicated to increase the probability of certain traffic sign combinations.*
    
5. Flip a coin twice to determine the starting section. The following combinations correspond to specific sections:
    - Heads & heads: The vehicle starts from Section N
    - Heads & tails: The vehicle starts from Section E
    - Tails & heads: The vehicle starts from Section W
    - Tails & tails: The vehicle starts from Section S
6. The starting zone of the vehicle is selected from zones Z3 and Z4 of the starting section. The vehicle starts from the zone that does not contain a traffic sign in front of it.
    - If the round's driving direction is clockwise and there's a traffic sign at intersection T1 or T3, the vehicle starts from Z4; otherwise, it starts from Z3.
    - If the round's driving direction is counterclockwise and there's a traffic sign at intersection T2 or T4, the vehicle starts from Z3; otherwise, it starts from Z4.
    
    It's possible for a traffic sign to be located behind the vehicle.
