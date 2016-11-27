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

sliderLength = 160 #the physical length of a slider
enableBot = False #if true, robot commands will be published
enableScan = False #if true, robot scan will be run on predefined actions
widthRight = 24  #width of the right frame
widthLeft = 32  #width of the left frame
taskOptions = ["dropRight","dropLeft","dropMiddle","grabBlock", "zeroBot"]


#hardcode position configurations, from base to end effector
configurations = {
	'left':[1,2,3,2,1],
	'right':[1,2,3,2,1],
	'middle':[1,2,3,2,1],
	'hopperClose':[1,2,3,2,1],
	'hopperTouch':[1,2,3,2,1],
	'safe':[1,2,3,2,0]
}

gripper = {
	'open':[1,1],
	'close':[0,0]
}

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

def moveGripper(data=False):
	'''Moves gripper.  If False, gripper is OPEN.'''

	a = Float32MultiArray()
	if data:
		#close gripper
		a.data.append(float(gripper['close'][0]))
		a.data.append(float(gripper['close'][1]))
	else:
		#open gripper
		a.data.append(float(gripper['open'][0]))
		a.data.append(float(gripper['open'][1]))
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
	
	#moveTo(goalRight)
	moveArm(configurations['right'])

	#delay()
	rospy.sleep(3)

	#openGripper
	moveGripper()

	rospy.sleep(2)
	safeHome(configurations['safe'])

def dropLeft():
	'''drops a block to the robot's right.  The robot is assumed to have a block and in the safeHome position '''

	#moveTo(goalLeft)
	moveArm(configurations['left'])

	#delay()
	rospy.sleep(3)

	#openGripper
	moveGripper()

	rospy.sleep(2)
	safeHome(configurations['safe'])

def dropMiddle():
	'''drops a block to the robot's right.  The robot is assumed to have a block and in the safeHome position '''

	#moveTo(goalMiddle)
	moveArm(configurations['middle'])

	#delay()
	rospy.sleep(3)

	#openGripper
	moveGripper()

	rospy.sleep(2)
	safeHome(configurations['safe'])

def grabBlock():
	'''grabs a block from a known location.  The robot is assumed to be in safeHome position and have no block in its gripper.'''

	moveArm(configurations['hopperClose'])
	rospy.sleep(3)
	moveGripper()
	rospy.sleep(2)
	moveArm(configurations['hopperTouch'])
	rospy.sleep(2)
	moveGripper(data=True)
	rospy.sleep(2)
	moveArm(configurations['hopperClose'])
	rospy.sleep(2)
	safeHome(configurations['safe'])

def scan():
	'''pretends to scan the structure with a 3D camera by moving to a few random configurations.'''
	#generate random configurations (within selected thresholds)
	#moveTo(conf1)
	#delay()
	#rinse and repeat
	pass

def execute():
	'''Tries to execute the command to the robot'''
	if enableBot:
		print "Executing action..."

		#decide on how to handle the request
		if v0.get() == "forward kinematics":
			moveArm()
		elif v0.get() == "predefined task":
			#try to read the action
			if v1.get() == 'zeroBot':
				zeroBot()
			elif v1.get() == 'dropRight':
				if b2['text'] == 'SCAN ENABLED':
					# print 'doing scan'
					scan()
				# else:
					# print 'not doing scan'
				# print 'dropRight'
				dropRight()
			elif v1.get() == 'dropLeft':
				if b2['text'] == 'SCAN ENABLED':
					# print 'doing scan'
					scan()
				# else:
					# print 'not doing scan'
				# print 'dropLeft'
				dropLeft()
			elif v1.get() == 'dropMiddle':
				if b2['text'] == 'SCAN ENABLED':
					# print 'doing scan'
					scan()
				# else:
					# print 'not doing scan'
				# print 'dropMiddle'
				dropMiddle()
			elif v1.get() == 'grabBlock':
				grabBlock()
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
v1.set("zeroBot") # default value
b2 = Button(frameTopRight, text="SCAN DISABLED", command=enableScan,width=widthRight)
b2.grid(row=3,column=0, columnspan=2,rowspan=1)
Label(frameTopRight, text="Predefined task: ").grid(row=5,column=0)
w1 = OptionMenu(frameTopRight, v1, taskOptions[0],taskOptions[1],taskOptions[2],taskOptions[3],taskOptions[4]).grid(row=5,column=1)

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
scale0 = Scale(frameTopLeft, variable = var0, from_ = 0.00, to = 5.00, length=sliderLength, resolution=0.01, command = junk, orient = HORIZONTAL).grid(row=1,column=1)
scale1 = Scale(frameTopLeft, variable = var1, from_ = 0.00, to = 5.00, length=sliderLength, resolution=0.01, command = junk, orient = HORIZONTAL).grid(row=2,column=1)
scale2 = Scale(frameTopLeft, variable = var2, from_ = 0.00, to = 5.00, length=sliderLength, resolution=0.01, command = junk, orient = HORIZONTAL).grid(row=3,column=1)
scale3 = Scale(frameTopLeft, variable = var3, from_ = 0.00, to = 5.00, length=sliderLength, resolution=0.01, command = junk, orient = HORIZONTAL).grid(row=4,column=1)
scale4 = Scale(frameTopLeft, variable = var4, from_ = 0.00, to = 5.00, length=sliderLength, resolution=0.01, command = junk, orient = HORIZONTAL).grid(row=5,column=1)
scale5 = Scale(frameTopLeft, variable = var5, from_ = 0.00, to = 5.00, length=sliderLength, resolution=0.01, command = junk, orient = HORIZONTAL).grid(row=6,column=1)
scale6 = Scale(frameTopLeft, variable = var6, from_ = 0.00, to = 5.00, length=sliderLength, resolution=0.01, command = junk, orient = HORIZONTAL).grid(row=7,column=1)

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
root.mainloop()