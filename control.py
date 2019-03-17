import RPi.GPIO as GPIO
import time
import threading
from brailler import BRAIL_DICT
import json
from get_data import CURRENT

GPIO.setmode(GPIO.BCM)


halfstep_seq = [
  [1,0,0,0],
  [1,1,0,0],
  [0,1,0,0],
  [0,1,1,0],
  [0,0,1,0],
  [0,0,1,1],
  [0,0,0,1],
  [1,0,0,1]
]

ulta_halfstep_seq = halfstep_seq[::-1]

def setup(pins):
    for pin in pins:
        try:
            GPIO.setup(pin, GPIO.OUT)
        except:
            print(pin)
        GPIO.output(pin, 0)


def move(pins, direction = -1):
    seq = halfstep_seq if direction == 1 else ulta_halfstep_seq
    for i in range(15):
        for halfstep in range(8):
            for pin in range(4):
                GPIO.output(pins[pin], seq[halfstep][pin])
            time.sleep(0.001)

brail_0_0 = [2, 3, 4, 14]
brail_1_0 = [15, 18, 17, 27]
brail_0_1 = [22, 23, 24, 10]
brail_1_1 = [11, 8, 25, 9]
brail_2_0 = [26, 20, 16, 19]

brails = [brail_0_0, brail_1_0, brail_0_1, brail_1_1, brail_2_0]

servoPIN = 13
GPIO.setup(servoPIN, GPIO.OUT)
p = GPIO.PWM(servoPIN, 50)
p.start(2.5)
time.sleep(1)

for brail in brails:
    setup(brail)

def move_servo_up():
    p.ChangeDutyCycle(4)

def move_servo_down():
    p.ChangeDutyCycle(2.5)


def move_up_brails(brails):
    was1In, was2In, was3In = False, False, False
    was4In, was5In, was6In = False, False, False
    if 1 in brails:
        a = threading.Thread(target=move, args=(brail_0_0, 1))
        a.start()
        was1In = True
    if 2 in brails:
        b = threading.Thread(target=move, args=(brail_1_0, -1))
        b.start()
        was2In = True
    if 3 in brails:
        c = threading.Thread(target=move, args=(brail_0_1, 1))
        c.start()
        was3In = True
    if 4 in brails:
        d = threading.Thread(target=move, args=(brail_1_1, -1))
        d.start()
        was4In = True
    if 5 in brails:
        e = threading.Thread(target=move, args=(brail_2_0, 1))
        e.start()
        was5In = True
    if 6 in brails:
        f = threading.Thread(target=move_servo_up)
        f.start()
        was6In = True
    
    if was1In:
        a.join()
    if was2In:
        b.join()
    if was3In:
        c.join()
    if was4In:
        d.join()
    if was5In:
        e.join()
    if was6In:
        f.join()


def move_down_brails(brails):
    was1In, was2In, was3In = False, False, False
    was4In, was5In, was6In = False, False, False
    if 1 in brails:
        a = threading.Thread(target=move, args=(brail_0_0, -1))
        a.start()
        was1In = True
    if 2 in brails:
        b = threading.Thread(target=move, args=(brail_1_0, 1))
        b.start()
        was2In = True
    if 3 in brails:
        c = threading.Thread(target=move, args=(brail_0_1, -1))
        c.start()
        was3In = True
    if 4 in brails:
        d = threading.Thread(target=move, args=(brail_1_1, 1))
        d.start()
        was4In = True
    if 5 in brails:
        e = threading.Thread(target=move, args=(brail_2_0, -1))
        e.start()
        was5In = True
    if 6 in brails:
        f = threading.Thread(target=move_servo_down)
        f.start()
        was6In = True
    
    if was1In:
        a.join()
    if was2In:
        b.join()
    if was3In:
        c.join()
    if was4In:
        d.join()
    if was5In:
        e.join()
    if was6In:
        f.join()

text= list(CURRENT.lower())

for ch in text:
    if ch not in BRAIL_DICT: continue
    brails = BRAIL_DICT[ch]
    move_up_brails(brails)
    time.sleep(0.1)
    move_down_brails(brails)
    time.sleep(0.1)

GPIO.cleanup()
