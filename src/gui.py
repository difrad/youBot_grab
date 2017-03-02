#!/usr/bin/env python

'''
todo: fix drop todo
downs: call appropriate functions from gui
todo: fix shape of windows
todo: keep log
todo: plan into this smooth path planning
'''

import rospy
from std_msgs.msg import Float32MultiArray, Bool,UInt8MultiArray
from Tkinter import *
import random

sliderLength = 640 #the physical length of a slider
enableBot = False #if true, robot commands will be published
enableScan = False #if true, robot scan will be run on predefined actions
widthRight = 24  #width of the right frame
widthLeft = 32  #width of the left frame
taskOptions = ["dropRight","dropLeft","grabBlock","scanLeft","scanRight",'waveHello',"stackGood","stackBad","giveHumanGood","giveHumanBad","toggleGripper"]


#hardcode position configurations, from base to end effector
configurations = {
	'left':[3.14-1.24,1.77,-1.30,2.23,2.88],
	'right':[3.14+1.24,1.77,-1.30,2.23,2.88],
	'middleGood':[3.14,0.98,-0.92,3.01,2.88],
	'middleRight':[3.14-.5,0.98,-0.92,3.01,2.88],
	'middleLeft':[3.14+.5,0.98,-0.92,3.01,2.88],
	#'hopperClose':[0.02,2.04,-0.68,0.69,2.88],
	#'hopperTouch':[0.02,2.16,-1.15,0.95,2.88],
	'hopperPoint0':[0.0224, 0.93, -0.24, 1.27, 2.948],
	'hopperPoint1':[0.0224, 1.033, -0.335, 1.25, 2.948],
	'hopperPoint2':[0.0224, 1.132, -0.407, 1.25, 2.948],
	'hopperPoint3':[0.0224, 1.365, -0.693585, 1.7, 2.948],
	'hopperPoint4':[0.0224, 1.365, -0.693585, 1.295, 2.948],
	'safe':[0.02+3.14,0.02,-0.02,0.03,0.12],
	'stackGood':[0.02,0.29,-3.06,0.03,3.47]
}

gripper = {
	# 'open':[0.0114,0.000001],
	'open':[0.0114,0.0114],
	# 'close':[0.000001,0.000001]
	'close':[0.000001,0.0065]
}

#possible configurations that make the robot look like it's 'scanning'.  Can append more
scanMiddleConfiguration = [
[0.02+3.14,0.02,-0.02,2.18,2.88-1],
[0.02+3.14,0.02,-0.02,1.80,2.88+1],
[0.02+3.14,1.48,-1.97,2.94,2.88-1],
[0.02+3.14,1.80,-0.57,0.82,2.88+1]
]

scanRightConfiguration = [
[3.14+1.24,0.02,-0.02,1.70,2.88],
[3.14+1.24,0.02,-0.02,2.40,2.88],
# [3.38+1,1.48,-1.97,2.94,2.88-1],
[3.14+1.24,0.85,-1.01,2.95,2.88],
[3.14+1.24,1.20,-0.14,1.36,2.88+1]
]

scanLeftConfiguration = [
[3.14-1.24,0.02,-0.02,1.70,2.88],
[3.14-1.24,0.02,-0.02,2.40,2.88],
# [3.38+1,1.48,-1.97,2.94,2.88-1],
[3.14-1.24,0.85,-1.01,2.95,2.88],
[3.14-1.24,1.20,-0.14,1.36,2.88+1]
]

def check():
	'''hopefully makes it so you can control+c from the terminal'''
	root.after(50,check) #50ms

def junk(data):
	pass

def zeroBot():
	'''tries to zero the robot'''
	pass

def enableToggle():
	'''enables or disables the robot, for safety.  Defaults to disabled.'''
	global enableBot

	if enableBot:
		enableBot = False
		b0["text"] = "BOT IS DISABLED"
	else:
		enableBot = True
		b0["text"] = "BOT IS ENABLED"

def enableScan():
	'''enables or disables the pretend scan function.  Defaults to disabled.'''
	global enableScan

	if enableScan:
		enableScan = False
		b2["text"] = "SCAN DISABLED"
	else:
		enableScan = True
		b2["text"] = "SCAN ENABLED"

def moveArm(data=[]):
	'''publishes arm data'''

	if len(data) == 0:
		a = Float32MultiArray()
		a.data.append(float(var0.get()))
		a.data.append(float(var1.get()))
		a.data.append(float(var2.get()))
		a.data.append(float(var3.get()))
		a.data.append(float(var4.get()))
		armPublisher.publish(a)

	else:
		a = Float32MultiArray()
		a.data.append(data[0])
		a.data.append(data[1])
		a.data.append(data[2])
		a.data.append(data[3])
		a.data.append(data[4])
		armPublisher.publish(a)

def moveGripper(data=[]):
	'''Moves gripper.  If False, gripper is OPEN.'''

	a = Float32MultiArray()
	if len(data) == 0:
		a.data.append(float(var5.get()))
		a.data.append(float(var6.get()))
	else:
		a.data.append(data[0])
		a.data.append(data[1])
	gripperPublisher.publish(a)

def safeHome(data):
	'''our bandaid fix to make the robot move safely without crashing into the table.  So far, it works...'''

	a = Float32MultiArray()
	a.data.append(data[0])
	a.data.append(data[1])
	a.data.append(data[2])
	a.data.append(data[3])	
	a.data.append(data[4])	
	safeHomePublisher.publish(a)

def dropRight():
	'''drops a block to the robot's right.  The robot is assumed to have a block and in the safeHome position '''
	
	#moveTo(goalLeft)
	moveArm(configurations['right'])

	#delay()
	rospy.sleep(4)

	#openGripper
	moveGripper(gripper['open'])

	rospy.sleep(2)
	safeHome(configurations['safe'])

	rospy.sleep(1)
	grabBlock()

def dropLeft():
	'''drops a block to the robot's right.  The robot is assumed to have a block and in the safeHome position '''

	#moveTo(goalLeft)
	moveArm(configurations['left'])

	#delay()
	rospy.sleep(4)

	#openGripper
	moveGripper(gripper['open'])

	rospy.sleep(2)
	safeHome(configurations['safe'])

	rospy.sleep(1)
	grabBlock()

def stackGood():
	#moveTo(goalLeft)
	moveArm(configurations['stackGood'])
	rospy.sleep(4)

	#openGripper
	moveGripper(gripper['open'])
	rospy.sleep(2)

	safeHome(configurations['safe'])
	rospy.sleep(1)

def stackBad():
	pass

def giveHumanGood():
	moveArm(configurations['middleGood'])
	rospy.sleep(4.5)

	#openGripper
	moveGripper(gripper['open'])
	rospy.sleep(3)

	safeHome(configurations['safe'])
	rospy.sleep(1)

def giveHumanBad():
	moveArm(configurations['middleLeft'])
	rospy.sleep(3)

	moveArm(configurations['middleRight'])
	rospy.sleep(2)

	moveArm(configurations['middleGood'])
	rospy.sleep(2)

	#openGripper
	moveGripper(gripper['open'])
	rospy.sleep(2.5)

	safeHome(configurations['safe'])
	rospy.sleep(1)

def grabBlock():
	'''grabs a block from a known location.  The robot is assumed to be in safeHome position and have no block in its gripper.'''

	# moveArm(configurations['hopperPoint0'])
	# rospy.sleep(1)
	#moveArm(configurations['hopperPoint1'])
	#rospy.sleep(1)
	moveGripper(gripper['open'])
	rospy.sleep(3)
	# moveArm(configurations['hopperPoint2'])
	rospy.sleep(3)
	moveArm(configurations['hopperPoint3'])
	rospy.sleep(3)
	moveArm(configurations['hopperPoint4'])
	rospy.sleep(3)
	moveGripper(gripper['close'])
	rospy.sleep(1)
	#moveArm(configurations['hopperPoint3'])
	#rospy.sleep(3)
	# moveArm(configurations['hopperPoint2'])
	# rospy.sleep(3)
	#moveArm(configurations['hopperPoint1'])
	#rospy.sleep(3)
	moveArm(configurations['hopperPoint0'])
	rospy.sleep(3)
	safeHome(configurations['safe'])
	# rospy.sleep(5)

def scanLeft():
	'''pretends to scan the structure with a 3D camera by moving to a few random configurations.'''

	moveArm(scanLeftConfiguration[0])
	rospy.sleep(1)

	moveArm(scanLeftConfiguration[1])
	rospy.sleep(1)

	moveArm(scanLeftConfiguration[0])
	rospy.sleep(4)

	moveArm(scanLeftConfiguration[2])
	rospy.sleep(4)

	moveArm(scanLeftConfiguration[3])
	rospy.sleep(4)

	# moveArm(scanLeftConfiguration[2])
	# rospy.sleep(4)

	safeHome(configurations['safe'])
	rospy.sleep(3)

def scanRight():
	'''pretends to scan the structure with a 3D camera by moving to a few random configurations.'''

	moveArm(scanRightConfiguration[0])
	rospy.sleep(1)

	moveArm(scanRightConfiguration[1])
	rospy.sleep(1)

	moveArm(scanRightConfiguration[0])
	rospy.sleep(4)

	moveArm(scanRightConfiguration[2])
	rospy.sleep(4)

	moveArm(scanRightConfiguration[3])
	rospy.sleep(4)

	# moveArm(scanRightConfiguration[2])
	# rospy.sleep(4)

	safeHome(configurations['safe'])
	rospy.sleep(3)

def scanMiddle():
	'''pretends to scan the structure with a 3D camera by moving to a few random configurations.'''

	moveArm(scanMiddleConfiguration[0])
	rospy.sleep(1)

	moveArm(scanMiddleConfiguration[1])
	rospy.sleep(1)

	moveArm(scanMiddleConfiguration[0])
	rospy.sleep(4)

	moveArm(scanMiddleConfiguration[2])
	rospy.sleep(4)

	moveArm(scanMiddleConfiguration[3])
	rospy.sleep(4)

	moveArm(scanMiddleConfiguration[2])
	rospy.sleep(4)

	safeHome(configurations['safe'])
	rospy.sleep(3)

def waveHello():
	count = 3

	for i in range(count):
		moveArm(scanMiddleConfiguration[0])
		rospy.sleep(.2)

		moveArm(scanMiddleConfiguration[1])
		rospy.sleep(.2)

def toggleGripper():
	count = 5

	for i in range(count):
		#openGripper
		moveGripper(gripper['open'])
		rospy.sleep(2)
		moveGripper(gripper['close'])
		rospy.sleep(2)

def execute():
	'''Tries to execute the command to the robot'''
	if enableBot:
		print "Executing action..."

		#decide on how to handle the request
		if v0.get() == "forward kinematics":
			moveArm()
			moveGripper()
		elif v0.get() == "predefined task":
			#try to read the action
			if v1.get() == 'dropRight':
				if b2['text'] == 'SCAN ENABLED':
					scanMiddle()
				dropRight()
			elif v1.get() == 'dropLeft':
				if b2['text'] == 'SCAN ENABLED':
					scanMiddle()
				dropLeft()
			elif v1.get() == 'grabBlock':
				grabBlock()
			elif v1.get() == 'scanRight':
				scanRight()
			elif v1.get() == 'scanLeft':
				scanLeft()
			elif v1.get() == 'waveHello':
				waveHello()
			elif v1.get() == 'stackGood':
				stackGood()
			elif v1.get() == 'stackBad':
				stackBad()
			elif v1.get() == 'giveHumanGood':
				giveHumanGood()
			elif v1.get() == 'giveHumanBad':
				giveHumanBad()
			elif v1.get() == 'toggleGripper':
				toggleGripper()
			else:
				print 'not yet enabled'
		else:
			print "Solver not enabled yet.  Please make a different selection."
	else:
		print "Please enable the robot first."

#create the GUI window
root = Tk()
root.title("Robot Control Interface")
frame = Frame(root)
frame.pack()

#build subframes into the main GUI frame
frameRight = Frame(frame)
frameLeft = Frame(frame)
frameTopLeft = Frame(frameLeft,bd=2,relief=RIDGE)
frameBotLeft = Frame(frameLeft,bd=2,relief=RIDGE)
frameTopRight = Frame(frameRight,bd=2,relief=RIDGE)
frameMidRight = Frame(frameRight,bd=2,relief=RIDGE)
frameBotRight = Frame(frameRight,bd=2,relief=RIDGE)
frameLeft.grid(row=0,column=0)
frameRight.grid(row=0,column=1)
frameTopLeft.grid(row=0,column=0)
frameBotLeft.grid(row=1,column=0)
frameTopRight.grid(row=0,column=0)
frameMidRight.grid(row=1,column=0)
frameBotRight.grid(row=2,column=0)

############## BUILD INTO TOP RIGHT FRAME ##############
#######################################################
v0 = StringVar(frameTopRight)
v0.set("Select Solver") # default value
Label(frameTopRight,text="BOT SETUP",font="Helvetica 16 bold").grid(row=0, column=0, sticky=W+E+N+S, columnspan=2,rowspan=1)
Label(frameTopRight,text="Solver:").grid(row=3, column=0, sticky=W+E+N+S)
b0 = Button(frameTopRight, text="CLICK TO ENABLE BOT", command = enableToggle, width=widthRight)
Label(frameTopRight, text="Solver: ").grid(row=4,column=0)
w0 = OptionMenu(frameTopRight, v0, "forward kinematics","inverse kinematics","predefined task")
b0.grid(row=1,column=0, columnspan=2,rowspan=1)
# b1.grid(row=2,column=0, columnspan=2,rowspan=1)
w0.grid(row=4,column=1)

############## BUILD INTO MID RIGHT FRAME ##############
#######################################################
v1 = StringVar(frameTopRight)
v1.set("waveHello") # default value
b2 = Button(frameTopRight, text="SCAN DISABLED", command=enableScan,width=widthRight)
b2.grid(row=3,column=0, columnspan=2,rowspan=1)
Label(frameTopRight, text="Predefined task: ").grid(row=5,column=0)
w1 = OptionMenu(frameTopRight, v1, taskOptions[0],taskOptions[1],taskOptions[2],taskOptions[3],taskOptions[4],taskOptions[5],taskOptions[6],taskOptions[7],taskOptions[8],taskOptions[10]).grid(row=5,column=1)

############## BUILD INTO BOT RIGHT FRAME ##############
#######################################################
b3 = Button(frameTopRight, text="EXECUTE", command = execute, width=widthRight/2,font="Helvetica 16 bold").grid(row=6,column=0, columnspan=2,rowspan=1)


############## BUILD INTO TOP LEFT FRAME ##############
########################################################

Label(frameTopLeft,text="JOINT CONFIG",font="Helvetica 16 bold").grid(row=0, column=0, columnspan=2,rowspan=1,sticky=W+E+N+S)

#stored variables
var0 = DoubleVar()
var1 = DoubleVar()
var2 = DoubleVar()
var3 = DoubleVar()
var4 = DoubleVar()
var5 = DoubleVar()
var6 = DoubleVar()

#sliders
scale0 = Scale(frameTopLeft, variable = var0, from_ = 0.02, to = 5.84, length=sliderLength, resolution=0.01, command = junk, orient = HORIZONTAL).grid(row=1,column=1)
scale1 = Scale(frameTopLeft, variable = var1, from_ = 0.02, to = 2.61, length=sliderLength, resolution=0.01, command = junk, orient = HORIZONTAL).grid(row=2,column=1)
scale2 = Scale(frameTopLeft, variable = var2, from_ = -5.02, to = -0.02, length=sliderLength, resolution=0.01, command = junk, orient = HORIZONTAL).grid(row=3,column=1)
scale3 = Scale(frameTopLeft, variable = var3, from_ = 0.03, to = 3.42, length=sliderLength, resolution=0.01, command = junk, orient = HORIZONTAL).grid(row=4,column=1)
scale4 = Scale(frameTopLeft, variable = var4, from_ = 0.12, to = 5.64, length=sliderLength, resolution=0.01, command = junk, orient = HORIZONTAL).grid(row=5,column=1)
scale5 = Scale(frameTopLeft, variable = var5, from_ = 0.001, to = 0.011, length=sliderLength, resolution=0.001, command = junk, orient = HORIZONTAL).grid(row=6,column=1)
scale6 = Scale(frameTopLeft, variable = var6, from_ = 0.001, to = 0.011, length=sliderLength, resolution=0.001, command = junk, orient = HORIZONTAL).grid(row=7,column=1)

Label(frameTopLeft,text="m0_base").grid(row=1,column=0)
Label(frameTopLeft,text="m1").grid(row=2,column=0)
Label(frameTopLeft,text="m2").grid(row=3,column=0)
Label(frameTopLeft,text="m3").grid(row=4,column=0)
Label(frameTopLeft,text="m4").grid(row=5,column=0)
Label(frameTopLeft,text="m5_grip_l").grid(row=6,column=0)
Label(frameTopLeft,text="m6_grip_r").grid(row=7,column=0)


############## BUILD INTO BOT LEFT FRAME ##############
########################################################
Label(frameBotLeft,text="END EFFECTOR CONFIG",font="Helvetica 16 bold").grid(row=0, column=0, columnspan=2,rowspan=1,sticky=W+E+N+S)

e0 = Entry(frameBotLeft, width=10).grid(row=1,column=1)
e1 = Entry(frameBotLeft, width=10).grid(row=2,column=1)
e2 = Entry(frameBotLeft, width=10).grid(row=3,column=1)
e3 = Entry(frameBotLeft, width=10).grid(row=4,column=1)
e4 = Entry(frameBotLeft, width=10).grid(row=5,column=1)
e5 = Entry(frameBotLeft, width=10).grid(row=6,column=1)
e6 = Entry(frameBotLeft, width=10).grid(row=7,column=1)
e7 = Entry(frameBotLeft, width=10).grid(row=8,column=1)

Label(frameBotLeft,text="x").grid(row=1,column=0)
Label(frameBotLeft,text="y").grid(row=2,column=0)
Label(frameBotLeft,text="z").grid(row=3,column=0)
Label(frameBotLeft,text="roll").grid(row=4,column=0)
Label(frameBotLeft,text="pitch").grid(row=5,column=0)
Label(frameBotLeft,text="yaw").grid(row=6,column=0)
Label(frameBotLeft,text="grip_l").grid(row=7,column=0)
Label(frameBotLeft,text="grip_r").grid(row=8,column=0)

#create the publishers
armPublisher = rospy.Publisher('moveArm', Float32MultiArray, queue_size=20)
gripperPublisher = rospy.Publisher('moveGripper', Float32MultiArray, queue_size=20)
safeHomePublisher = rospy.Publisher('safeHome', Float32MultiArray, queue_size=20)
rospy.init_node('gui', anonymous=True)

#run the loop indefinitely
root.after(50,check)
root.mainloop()