import os
import shutil

def forward(i):
	s = "forward.hex"
	if(i > 0):
		s = "forward"+str(i)+".hex"
	move(s)

def left(i):
	s = "left.hex"
	if(i > 0):
		s = "left"+str(i)+".hex"
	move(s)

def right(i):
	s = "right.hex"
	if(i > 0):
		s = "right"+str(i)+".hex"
	move(s)

def move(s):

	original = "commands/" + s
	#original = "C:\\Users\\DSPOTHP116\\Documents\\EduSwarm\\EduSwarm\\commands\\forward.hex"
	microbit = "F:\\" + s
	shutil.copy(original, microbit)

forward(0)