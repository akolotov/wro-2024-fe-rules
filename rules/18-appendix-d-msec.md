# **Appendix D: Minimal set of electromechanical components**

The list below represents the list of equipment which can be used for electromechanical parts of the vehicle. This is suggestion rather than the requirements. Teams are on their own to follow these suggestions or not.

- a single board computer: it will be used for real time video processing, analysing sensor
data, sending/managing signals to the motor controller.
- a single board microcontroller + a motor shield: this combination of equipment receives
managing signals from the main SBC and operates with motors correspondingly.
- a wide-angle camera
- two distance sensors
- two light sensors
- servomotor: it controls steering
- DC-motor with gearbox: it controls the vehicle’s velocity
- at least one encoder: it allows the vehicle to measure angular velocity of a DC motor
- IMU (inertial measurement unit) – this is usually a combination of gyroscope and
accelerometer: it can be used to improve the vehicle navigation
- two batteries: one is for SBC and SBM, another is for motors
- a voltage stabilizer: it is required to provide adequate power supply for the SBC/SBM
- two switches to connect batteries to the power consumers: SBC/SBM, motors
- push button: it could be used as a trigger to start the round

An example vehicle configuration could be:

- Chassis from a Remote Controlled (RC) Car
- The main controller -- Raspberry Pi 3 (https://www.raspberrypi.org/products/raspberry-pi-
3-model-b-plus/), and a MicroSD card to keep an operating system and programs.
- Camera module (https://www.raspberrypi.org/products/camera-module-v2/) with extra
wide-angle lens
- The motor and sensor controller -- Arduino UNO (https://store.arduino.cc/arduino-uno-
rev3) with a prototyping shield (https://store.arduino.cc/proto-shield-rev3-uno-size)
- DC Motor Controller (https://www.robotshop.com/en/cytron-13a-5-30v-single-dc-motor-
controller.html)
- DC Motor to drive the vehicle (could be part of the chassis),
- Servo Motor for steering (could be part of the chassis)
- IMU sensor (https://www.sparkfun.com/products/13762)
- 2 Ultrasonic Distance Sensor (https://www.sparkfun.com/products/15569)
- 2 Analog Line sensors (https://www.sparkfun.com/products/9453)
- Rotary Encoder (https://www.sparkfun.com/products/10790)
- An external USB Battery with a hub to split the consumption between Raspberry Pi and Arduino
- Additional battery applicable to power the DC motor (could be part of the chassis)