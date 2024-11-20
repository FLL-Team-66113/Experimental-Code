from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import Car
from pybricks.tools import wait, StopWatch
from pybricks.iodevices import XboxController

hub = PrimeHub()

drive_motor=Motor(Port.C, Direction.CLOCKWISE)
drive_motor2=Motor(Port.E,)
turn_motor=Motor(Port.A, Direction.COUNTERCLOCKWISE)

car = Car(turn_motor,[drive_motor, drive_motor2], 20)

xc = XboxController()

while True:
    jx, jy = xc.joystick_left()
    tl, tr = xc.triggers()
    car.drive_power(-tl + tr)
    car.steer(jx)

    wait(.1)

print('code ran')