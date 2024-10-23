# **5. Game Description and Game Field**

The self-driving car challenges in this season are Time Attack races: there will not be multiple cars at the same time on the track. Instead, one car per attempt will try to achieve the best time by driving several laps fully autonomously. The two challenges are the following:

**Open Challenge:** The vehicle must complete three (3) laps on the track with random placements of the inside track walls.

**Obstacle Challenge:** The vehicle must complete three (3) laps on the track with randomly placed green and red traffic signs. The traffic signs indicate the side of the lane the vehicle must follow. The traffic sign to keep to the ***right side*** of the lane is a ***red pillar***. The traffic sign to keep to the ***left side*** of the lane is a ***green pillar***. The continuation of the vehicle to the third round is indicated by the last traffic sign of the second round. A green traffic sign indicates that the robot must go ahead and continue the third round in the same direction. A red traffic sign indicates that the vehicle must turn around and complete the third round in the opposite direction. The vehicle <new_in_2024>should not move</new_in_2024> any of the traffic signs. <new_in_2024>After the robot completed the three rounds, it has to find the parking lot and has to perform parallel parking.</new_in_2024>

The starting direction in which the car must drive on the track (clockwise or counter clockwise) will vary in different challenge rounds. The starting position of the car as well as the number and location of traffic signs are randomly defined before the round (after the check time). The following graphic shows the game field with the game objects.

![The image shows a self-driving car challenge field with square-shaped walls forming a lane. The car must complete laps while navigating obstacles and following traffic signs, represented by red and green pillars. A yellow self-driving car, equipped with a camera, is ready to race, following blue and orange lines for direction. The track includes a magenta parking lot where the car will perform parallel parking at the end of the race. The central platform features the “FUTURE ENGINEERS” logo, but it’s decorative.](https://prod-files-secure.s3.us-west-2.amazonaws.com/bcc84f75-a08e-44e5-94e8-8418e8377ebf/b1aee6da-8d1c-48c7-92a2-614c609a94cc/image.png)

**Figure 1: Detailed game field**

The game field represents a racetrack where traffic signs (represented by the coloured obstacles pillars) are set up.

The track consists of eight sections: four corner sections and four straightforward sections. Corner sections are marked with red dashed lines on the next Figure. Straightforward sections are marked with blue dashed lines.

![The image shows a robotics competition field divided into eight sections by dashed red and blue lines to highlight zones. These lines represent four corner sections (red) and four straightforward sections (blue) that form the track. Colored lines (blue and orange) connect the corners of the inner and outer squares. The center of the field features a decorative “FUTURE ENGINEERS” logo. The dashed lines are visual aids for understanding the track layout but are not present on the actual field.](https://prod-files-secure.s3.us-west-2.amazonaws.com/bcc84f75-a08e-44e5-94e8-8418e8377ebf/611e73c1-a1cc-49ce-91db-fb62ffab085c/image.png)

**Figure 2: Different types of sections on the game field**

Every straightforward section is divided into 6 zones. Six internal zones within the section are for starting position of the car. 4 T-intersections and 2 X-intersections are used to position the traffic signs. The places where the traffic signs can be set up are called traffic signs’ seats.

![The image shows a detailed layout of a straightforward section on a robotics competition field. The section is divided into six zones, with T-intersections and X-intersections marked as circular points where traffic signs (pillars) can be placed. These intersections and zones define where the car can start and where the traffic signs will be positioned during the challenge.](https://prod-files-secure.s3.us-west-2.amazonaws.com/bcc84f75-a08e-44e5-94e8-8418e8377ebf/9acf426b-557e-4ecc-a763-07a098665250/image.png)

**Figure 3: Zones and traffic signs’ seats in the straightforward section**

<new_in_2024>It is possible, that a parking lot is placed in one of the straight forward sections. The width of the parking lot is always 20 cm. The length is variable and calculated: *1,25 * length of the robot.*</new_in_2024>

<new_in_2024>The parking lot is limited by two wood elements with 20 cm x 2 cm x 10 cm in magenta. The right element is placed right next to the dotted line. The position of the left one is defined as described above.</new_in_2024>

![The image shows the parking lot layout in a straightforward section of a robotics competition field. The parking lot is located at the bottom of the section, near the field’s outer edge. It has a fixed width of 20 cm and a variable length based on the robot’s size (1.25 times the robot’s length). The parking lot is bordered by two magenta lines, with the right line placed next to a dotted boundary line and the left line adjusting to the required length for the robot to perform parallel parking.](https://prod-files-secure.s3.us-west-2.amazonaws.com/bcc84f75-a08e-44e5-94e8-8418e8377ebf/b0d974a0-bbb2-4b70-b19d-242728187ba7/image.png)

**Figure 4: Definition of size of the parking lot**