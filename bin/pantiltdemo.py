#!/usr/bin/env python

import pantilthat
import curses
import random
from picamera import PiCamera
from time import sleep

stdscr = curses.initscr()
camera = PiCamera()
sleep(2)

curses.noecho()
curses.cbreak()
c = ''

#camera
camera.resolution = (1024, 768)
camera.vflip = True
camera.hflip = True
camera.start_preview()
sleep(2)

#Functions
def nope():
	if x >= 0:
		pantilthat.servo_one(-90)
		sleep(.1)
		pantilthat.servo_one(90)
		sleep(.1)
		pantilthat.servo_one(-90)
		sleep(.1)
		pantilthat.servo_one(90)
		sleep(.1)
		pantilthat.servo_one(0)
	else:
		pantilthat.servo_one(90)
		sleep(.1)
		pantilthat.servo_one(-90)
		sleep(.1)
		pantilthat.servo_one(90)
		sleep(.1)
		pantilthat.servo_one(-90)
		sleep(.1)
		pantilthat.servo_one(0)
		
def yep():
	if z >= 0:
		pantilthat.servo_two(-90)
		sleep(.1)
		pantilthat.servo_two(90)
		sleep(.1)
		pantilthat.servo_two(-90)
		sleep(.1)
		pantilthat.servo_two(90)
		sleep(.1)
		pantilthat.servo_two(0)
	else:
		pantilthat.servo_two(90)
		sleep(.1)
		pantilthat.servo_two(-90)
		sleep(.1)
		pantilthat.servo_two(90)
		sleep(.1)
		pantilthat.servo_two(-90)
		sleep(.1)
		pantilthat.servo_two(0)


#Main Program Loop
x,z,i=0,0,0
pantilthat.servo_one(x)
pantilthat.servo_one(z)
while c != ord('q'):
	c=stdscr.getch()
	if c == ord('d') and x <= 90:
		pantilthat.servo_one(x)
		x=x+1
	if c == ord('a') and x >= -90:
		pantilthat.servo_one(x)
		x=x-1
	if c == ord('s') and z <=90:
		pantilthat.servo_two(z)
		z=z+1
	if c == ord('w') and z >= -90:
		pantilthat.servo_two(z)
		z=z-1
	if c == ord(' '):
		name='image'+`random.randrange(1,1000)`+'.jpg'
		camera.capture(name)
	if c == ord('v'):
		name='video'+`random.randrange(1,1000)`+'.h264'
		camera.start_recording(name)
		sleep(5)
		camera.stop_recording
	if c == ord('y'):
		yep()
	if c == ord('n'):
		nope()






#End
camera.stop_preview()
curses.nocbreak(); stdscr.keypad(0); curses.echo()
curses.endwin()
