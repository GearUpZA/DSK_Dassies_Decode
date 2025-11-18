from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

hub = PrimeHub()

#Naming the Motors
left_motor = Motor(Port.F, Direction.COUNTERCLOCKWISE)
right_motor = Motor(Port.D)

#Naming the Attachment motors
Att_motor1 = Motor(Port.A)
Att_motor2 = Motor(Port.B, Direction.COUNTERCLOCKWISE)

#Defining the drive base
Drive_Base = DriveBase(left_motor, right_motor, 86, 132)
Drive_Base.use_gyro(True)

#Doing the missions
Drive_Base.straight(330)
Drive_Base.turn(-3)
for i in range(4):
    Att_motor1.run_angle(500, 140)
    Att_motor1.run_angle(500, -140)
Drive_Base.turn(-35)
Drive_Base.straight(450)
Drive_Base.turn(82)
Drive_Base.straight(170)
Drive_Base.turn(-135)