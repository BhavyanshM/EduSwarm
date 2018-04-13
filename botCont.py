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
	microbit = "F:\\" + s
	shutil.copy(original, microbit)

while True:
	ip = input("Forward(f) Left(l) Right(r) Quit(q)")
	print(ip)
	if ip == 'q':
		break
	if ip == 'f':
		forward(0)
	if ip == 'l':
		left(0)
	if ip == 'r':
		right(0)