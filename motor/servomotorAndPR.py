import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)
GPIO.setup(2, GPIO.IN)

GPIO.setup(3, GPIO.OUT)
pwm=GPIO.PWM(3, 50)
pwm.start(0)

def SetAngle(angle):
    dutyCycle = 1/20 * angle + 3
    pwm.ChangeDutyCycle(dutyCycle)
    sleep(0.2)

if __name__ == "__main__":
    try:
        while True:
            RPstate = GPIO.input(2)
            if PRstate == True:
                SetAngle(90)
                SetAngle(0)
                SetAngle(180)

    except KetboardInterrupt:
        pwm.stop()
        GPIO.cleanup()   
