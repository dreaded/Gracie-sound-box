#!/usr/bin/env python
import os
from time import sleep
 
import RPi.GPIO as GPIO
 
GPIO.setmode(GPIO.BCM)
GPIO.setup(02, GPIO.IN)
GPIO.setup(03, GPIO.IN)
GPIO.setup(04, GPIO.IN)
GPIO.setup(17, GPIO.IN)
GPIO.setup(27, GPIO.IN)
GPIO.setup(22, GPIO.IN)
GPIO.setup(23, GPIO.IN)
GPIO.setup(24, GPIO.IN)
GPIO.setup(25, GPIO.IN)
 
while True:
    if (GPIO.input(23) == False):
        os.system('killall mpg123 &')
 
    if (GPIO.input(24) == False):
        os.system('mpg123 -q aspesdestriaL.mp3 &')
 
    if (GPIO.input(25) == False):
        os.system('mpg123 -q BackwardandForwardThingy.mp3 &')

    if (GPIO.input(02) == False):
	os.system('mpg123 -q BackwardThingy.mp3 &')

    if (GPIO.input(03) == False):
	os.system('mpg123 -q cupOfTea.mp3 &')

    if (GPIO.input(04) == False):
	os.system('mpg123 -q eeebygum.mp3 &') 

    if (GPIO.input(17) == False):
	os.system('mpg123 -q sallyechers.mp3 &')

    if (GPIO.input(27) == False):
	os.system('mpg123 -q WishMe.mp3 &')

    if (GPIO.input(22) == False):
	os.system('mpg123 -q WishMeWhistle.mp3 &')

    sleep(0.1);
