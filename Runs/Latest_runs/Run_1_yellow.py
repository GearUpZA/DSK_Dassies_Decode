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
"""
Doing the missions
Drive_Base.straight(275)
Drive_Base.turn(-46)
Drive_Base.straight(800)
Drive_Base.straight(-70)
Drive_Base.turn(135)
Drive_Base.straight(-190)
Drive_Base.turn(-125)
Drive_Base.straight(-500)
Drive_Base.straight(150)
Drive_Base.turn(135)
Drive_Base.straight(350)
"""
Drive_Base.straight(450)
Drive_Base.turn(-50)
Drive_Base.straight(590)
Drive_Base.straight(-120)
Drive_Base.turn(135)
Drive_Base.straight(-200)
Drive_Base.turn(-130)
Drive_Base.straight(-500)
Drive_Base.straight(100)
Drive_Base.turn(135)
Drive_Base.straight(440)
Drive_Base.turn(-155)
