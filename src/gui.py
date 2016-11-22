#!/usr/bin/env python

# import rospy
# from std_msgs.msg import Float32MultiArray, Bool,UInt8MultiArray
from Tkinter import *

sliderLength = 160 #the physical length of a slider

def junk(data):
	pass

#create the GUI window
root = Tk()
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

############## BUILD INTO TOP RIGHT FRAME ##############
#######################################################
variable = 0
Label(frameTopRight,text="ROBOT SETUP",font="Helvetica 16 bold").grid(row=0, column=0, sticky=W+E+N+S, padx=5, pady=5)
b0 = Button(frameTopRight, text='ENABLE BOT',width=32).grid(row=1,column=0)
b1 = Button(frameTopRight, text='ZERO BOT',width=32) .grid(row=2,column=0)
w0 = OptionMenu(frameTopRight, variable, "one","two","three").grid(row=3,column=0)
# b0.pack(side=TOP)
# b1.pack(side=TOP)
# w0.pack(side=TOP)

############## BUILD INTO MID RIGHT FRAME ##############
#######################################################
Label(frameMidRight, text="QUEUE ACTION",font ="Helvetica 16 bold").grid(row=0,column=0)
b2 = Button(frameMidRight, text="'SCAN'",width=32).grid(row=1,column=0)
w1 = OptionMenu(frameMidRight, variable, "one","two","three").grid(row=2,column=0)
# b2.pack(side=TOP)
# w1.pack(side=TOP)

############## BUILD INTO BOT RIGHT FRAME ##############
#######################################################
b3 = Button(frameBotRight, text="EXECUTE",width=32,font="Helvetica 16 bold").grid(row=0,column=0)


############## BUILD INTO TOP LEFT FRAME ##############
########################################################

Label(frameTopLeft,text="JOINT CONFIGURATIONS",font="Helvetica 16 bold").grid(row=0, column=0, columnspan=2,rowspan=1,sticky=W+E+N+S, padx=5, pady=5)

#stored variables
var0 = 3
var1 = 1
var2 = 2
var3 = 3
var4 = 5
var5 = 2
var6 = 0

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

e0 = Entry(frameBotLeft).grid(row=1,column=1)
e1 = Entry(frameBotLeft).grid(row=2,column=1)
e2 = Entry(frameBotLeft).grid(row=3,column=1)
e3 = Entry(frameBotLeft).grid(row=4,column=1)
e4 = Entry(frameBotLeft).grid(row=5,column=1)
e5 = Entry(frameBotLeft).grid(row=6,column=1)
e6 = Entry(frameBotLeft).grid(row=7,column=1)
e7 = Entry(frameBotLeft).grid(row=8,column=1)

Label(frameBotLeft,text="x").grid(row=1,column=0)
Label(frameBotLeft,text="y").grid(row=2,column=0)
Label(frameBotLeft,text="z").grid(row=3,column=0)
Label(frameBotLeft,text="roll").grid(row=4,column=0)
Label(frameBotLeft,text="pitch").grid(row=5,column=0)
Label(frameBotLeft,text="yaw").grid(row=6,column=0)
Label(frameBotLeft,text="grip_l").grid(row=7,column=0)
Label(frameBotLeft,text="grip_r").grid(row=8,column=0)

#pack all the frames
frameRight.pack(side = RIGHT)
frameLeft.pack(side = LEFT)
frameTopLeft.pack(side=TOP)
frameBotLeft.pack(side=TOP)
frameTopRight.pack(side=TOP)
frameMidRight.pack(side=TOP)
frameBotRight.pack(side=TOP)

#create the publishers
# pub = rospy.Publisher('sliderData', Float32MultiArray, queue_size=20)
# rospy.Subscriber("fail_safe",Bool, lostSignal)
# rospy.Subscriber("pwm_control", UInt8MultiArray, updatePWM)
# rospy.init_node('tkinterGUI', anonymous=True)

#run the loop indefinitely
root.mainloop()