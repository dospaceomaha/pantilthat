#!/usr/bin/env python

import pantilthat
import curses
import random
import threading
from picamera import PiCamera
from time import sleep

stdscr = curses.initscr()
camera = PiCamera()
sleep(2)

curses.noecho()
curses.cbreak()
#stdscr.keypad(True)
c = ''

#camera
camera.resolution = (1024, 768)
camera.vflip = True
camera.hflip = True
camera.start_preview()
sleep(2)

#Functions
def nope( x ):
	if x >= 0:
		pantilthat.servo_one(-90)
		sleep(.15)
		pantilthat.servo_one(90)
		sleep(.15)
		pantilthat.servo_one(-90)
		sleep(.15)
		pantilthat.servo_one(90)
		sleep(.15)
		pantilthat.servo_one(0)
	else:
		pantilthat.servo_one(90)
		sleep(.15)
		pantilthat.servo_one(-90)
		sleep(.15)
		pantilthat.servo_one(90)
		sleep(.15)
		pantilthat.servo_one(-90)
		sleep(.15)
		pantilthat.servo_one(x)
		return

def yep( z ):
	if z >= 0:
		pantilthat.servo_two(-90)
		sleep(.15)
		pantilthat.servo_two(90)
		sleep(.15)
		pantilthat.servo_two(-90)
		sleep(.15)
		pantilthat.servo_two(90)
		sleep(.15)
		pantilthat.servo_two(0)
	else:
		pantilthat.servo_two(90)
		sleep(.15)
		pantilthat.servo_two(-90)
		sleep(.15)
		pantilthat.servo_two(90)
		sleep(.15)
		pantilthat.servo_two(-90)
		sleep(.15)
		pantilthat.servo_two(x)
		return

def vid( name, i ):
	camera.start_recording(name)
	sleep(i)
	camera.stop_recording
	return
	
def lft( x ):
	pantilthat.servo_one(x)
	return
	
def rgt( x ):
	pantilthat.servo_one(x)
	return
	
def up( z ):
	pantilthat.servo_two(z)
	return

def dwn( z ):
	pantilthat.servo_two(z)
	return


#Main Program Loop
x,z,i=0,0,5
pantilthat.servo_one(x)
pantilthat.servo_one(z)
while c != ord('q'):
	c=stdscr.getch()
	if c == ord('a') and x <= 90:
		for i in range(3):
			a = threading.Thread(target=lft, args=(x,))
			a.setDaemon(True)
			a.start()
		x=x+1

	if c == ord('d') and x >= -90:
		for i in range(3):
			a = threading.Thread(target=rgt, args=(x,))
			a.setDaemon(True)
			a.start()
		x=x-1

	if c == ord('s') and z <=90:
		for i in range(3):
			a = threading.Thread(target=up, args=(z,))
			a.setDaemon(True)
			a.start()
		z=z+1

	if c == ord('w') and z >= -90:
		for i in range(3):
			a = threading.Thread(target=dwn, args=(z,))
			a.setDaemon(True)
			a.start()
		z=z-1

	if c == ord(' '):
		name='image'+`random.randrange(1,1000)`+'.jpg'
		camera.capture(name)

	if c == ord('v'):
		name='video'+`random.randrange(1,1000)`+'.h264'
		for i in range(3):
			v = threading.Thread(target=vid, args=(name, i,))
			v.setDaemon(True)
			v.start()

	if c == ord('y'):
		for i in range(3):
			y = threading.Thread(target=yep, args=(z,))
			y.setDaemon(True)
			y.start()

	if c == ord('n'):
		for i in range(3):
			n = threading.Thread(target=nope, args=(x,))
			n.setDaemon(True)
			n.start()
	
#	if c == curses.KEY_UP
#		if i < 10
#			i+=1
	
#	if c == curses.KEY_DOWN
#		if i > 0
#		i-=1
		






#End
camera.stop_preview()
curses.nocbreak(); stdscr.keypad(0); curses.echo(); curses.keypad( False )
curses.endwin()
