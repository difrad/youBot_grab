#!/usr/bin/env python

'''
todo: fix drop downs
todo: call appropriate functions from gui
todo: fix shape of windows
todo: keep log
'''

# import rospy
# from std_msgs.msg import Float32MultiArray, Bool,UInt8MultiArray
from Tkinter import *

sliderLength = 160 #the physical length of a slider
enable = False #if true, robot commands will be published

def junk(data):
	pass

def enableToggle():
	'''enables or disables the robot, for safety.  Defaults to disabled.'''
	global enable

	if enable:
		enable = False
		b0["text"] = "BOT IS DISABLED"
	else:
		enable = True
		b0["text"] = "BOT IS ENABLED"

	enableStatus = 'True'

def execute():
	'''Tries to execute the command to the robot'''
	if enable:
		print "execute action"
	else:
		print "robot is disabled"

#create the GUI window
root = Tk()
root.title("Robot Control Interface")
frame = Frame(root)
frame.pack()

#build subframes into the main GUI frame
frameRight = Frame(frame)
frameLeft = Frame(frame)
frameTopLeft = Frame(frameLeft,bd=2,relief=RIDGE)
frameBotLeft = Frame(frameLeft,bd=2,relief=RIDGE,width=800)
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
variable = 0
Label(frameTopRight,text="ROBOT SETUP",font="Helvetica 16 bold").grid(row=0, column=0, sticky=W+E+N+S, padx=5, pady=5)
b0 = Button(frameTopRight, text="CLICK TO ENABLE BOT", command = enableToggle, width=32)
b1 = Button(frameTopRight, text='ZERO BOT',width=32) 
w0 = OptionMenu(frameTopRight, variable, "one","two","three")
b0.grid(row=1,column=0)
b1.grid(row=2,column=0)
w0.grid(row=3,column=0)

############## BUILD INTO MID RIGHT FRAME ##############
#######################################################
Label(frameMidRight, text="QUEUE ACTION",font ="Helvetica 16 bold").grid(row=0,column=0)
b2 = Button(frameMidRight, text="'SCAN'",width=32).grid(row=1,column=0)
w1 = OptionMenu(frameMidRight, variable, "one","two","three").grid(row=2,column=0)

############## BUILD INTO BOT RIGHT FRAME ##############
#######################################################
b3 = Button(frameBotRight, text="EXECUTE", command = execute, width=32,font="Helvetica 16 bold").grid(row=0,column=0)


############## BUILD INTO TOP LEFT FRAME ##############
########################################################

Label(frameTopLeft,text="JOINT CONFIGURATIONS",font="Helvetica 16 bold").grid(row=0, column=0, columnspan=2,rowspan=1,sticky=W+E+N+S, padx=5, pady=5)

#stored variables
var0 = 0
var1 = 1
var2 = 2
var3 = 3
var4 = 4
var5 = 5
var6 = 6

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
Label(frameBotLeft,text="END EFFECTOR CONFIGURATION",font="Helvetica 16 bold").grid(row=0, column=0, columnspan=2,rowspan=1,sticky=W+E+N+S, padx=5, pady=5)

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
# pub = rospy.Publisher('sliderData', Float32MultiArray, queue_size=20)
# rospy.Subscriber("fail_safe",Bool, lostSignal)
# rospy.Subscriber("pwm_control", UInt8MultiArray, updatePWM)
# rospy.init_node('tkinterGUI', anonymous=True)

#run the loop indefinitely
root.mainloop()