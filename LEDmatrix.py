import digitalio
import simpleio
from board import *

clock = digitalio.DigitalInOut(board.D0)
dataPin = digitalio.DigitalInOut(board.D1)
latchPin = digitalio.DigitalInOut(board.D2)

clock.direction = digitalio.Direction.OUTPUT
clock.pull = digitalio.Pull.DOWN

dataPin.direction = digitalio.Direction.OUTPUT
dataPin.pull = digitalio.Pull.DOWN

latchPin.direction = digitalio.Direction.OUTPUT
latchPin.pull = digitalio.Pull.DOWN

ledList = {
    "ledA": 1 << 0, # 00000001
    "ledB": 1 << 1, # 00000010
    "ledC": 1 << 2, # 00000100
    "ledD": 1 << 3, # 00001000
    "ledE": 1 << 4, # 00010000
    "ledF": 1 << 5, # 00100000
    "ledG": 1 << 6, # 01000000
    "ledH": 1 << 7 # 10000000
}

def knightRider():
    for x in range(3):
        for led in ledList:
            latchPin.value = False
            simpleio.shift_out(dataPin, clock, led, msb_first = False)
            latchPin.value = True
            time.sleep(0.5)

def quick():
    for led in ledList:
        latchPin.value = False
        simpleio.shift_out(dataPin, clock, led, msb_first = False)
        latchPin.value = True
        time.sleep(0.05)

baseLED = ledA

while True:
    # shifting out least significant bits
    # must toggle latchPin.value before and after shift_out to push to IC chip
    # this sample code was tested using
    knightRider()

    quick()
    