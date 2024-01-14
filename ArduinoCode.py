from pyfirmata import Arduino, SERVO
import time

yAxisPin = 9
xAxisPin = 10
triggerPin = 11



class idk_what_to_call_this():
    def __init__(self):
        self.board = Arduino('COM4')

        self.board.digital[yAxisPin] = SERVO
        self.board.digital[xAxisPin] = SERVO
        self.board.digital[triggerPin] = SERVO

        board.digital[yAxisPin].write(180)
        board.digital[xAxisPin].write(180)
        board.digital[triggerPin].write(0)

        time.sleep(1)

    def servoRotate(speed, direction, pin, currAngle):
        if direction:
            self.board.digital[pin].write(currAngle + speed/20)
            return currAngle + speed/20
        self.board.digital[pin].write(currAngle - speed/20)
        return currAngle - speed/20
    def servoLock(pin, angle):
        self.board.digital[pin].write(angle)


