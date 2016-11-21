#!/usr/bin/env python

import rospy
from std_msgs.msg import Float32MultiArray, Bool,UInt8MultiArray
from Tkinter import *

sliderLength = 160 #the physical length of a slider

def junk(data):
	pass

#create the GUI window
root = Tk()
frame = Frame(root)
frame.pack()

#build subframes into the main GUI frame
frameLeft = Frame(frame)
frameRight = Frame(frame)

frameTopRight = Frame(frameRight)
frameBotRight = Frame(frameRight)
frameTopLeft = Frame(frameLeft)
frameMidLeft = Frame(frameLeft)
frameBotLeft = Frame(frameLeft)

#build into all of the frames
# b0 = Button(frameTopRight, text='top right')

# b2 = Button(frameTopLeft, text='top left')
# b3 = Button(frameBotLeft, text='bot left')
# b0.pack(side=TOP)
# b1.pack(side=TOP)
# b2.pack(side=TOP)
# b3.pack(side=TOP)

############## BUILD INTO TOP LEFT FRAME ##############
#######################################################
variable = 0
b0 = Button(frameTopLeft, text='ENABLE BOT')
b1 = Button(frameTopLeft, text='ZERO BOT') 
w0 = OptionMenu(frameTopLeft, variable, "one","two","three")
b0.pack(side=TOP)
b1.pack(side=TOP)
w0.pack(side=TOP)

############## BUILD INTO MID LEFT FRAME ##############
#######################################################
b2 = Button(frameMidLeft, text="'SCAN'")
w1 = OptionMenu(frameTopLeft, variable, "one","two","three")
b2.pack(side=TOP)
w1.pack(side=TOP)

############## BUILD INTO BOT LEFT FRAME ##############
#######################################################
b3 = Button(frameBotLeft, text="EXECUTE")
b3.pack(side=TOP)

############## BUILD INTO TOP RIGHT FRAME ##############
########################################################

#stored variables
var0 = 3
var1 = 1
var2 = 1
var3 = 1
var4 = 5
var5 = 2
var6 = 0

#sliders
scale0 = Scale(frameTopRight, variable = var0, from_ = 0.00, to = 5.00, length=sliderLength, resolution=0.01, command = junk, orient = HORIZONTAL)
scale1 = Scale(frameTopRight, variable = var1, from_ = 0.00, to = 5.00, length=sliderLength, resolution=0.01, command = junk, orient = HORIZONTAL)
scale2 = Scale(frameTopRight, variable = var2, from_ = 0.00, to = 5.00, length=sliderLength, resolution=0.01, command = junk, orient = HORIZONTAL)
scale3 = Scale(frameTopRight, variable = var3, from_ = 0.00, to = 5.00, length=sliderLength, resolution=0.01, command = junk, orient = HORIZONTAL)
scale4 = Scale(frameTopRight, variable = var4, from_ = 0.00, to = 5.00, length=sliderLength, resolution=0.01, command = junk, orient = HORIZONTAL)
scale5 = Scale(frameTopRight, variable = var5, from_ = 0.00, to = 5.00, length=sliderLength, resolution=0.01, command = junk, orient = HORIZONTAL)
scale6 = Scale(frameTopRight, variable = var6, from_ = 0.00, to = 5.00, length=sliderLength, resolution=0.01, command = junk, orient = HORIZONTAL)



#initial values
scale0.set(2)
scale1.set(1)
scale2.set(2)
scale3.set(1)
scale4.set(2)
scale5.set(1)
scale6.set(2)

#pack
scale0.pack(side=TOP)
scale1.pack(side=TOP)
scale2.pack(side=TOP)
scale3.pack(side=TOP)
scale4.pack(side=TOP)
scale5.pack(side=TOP)
scale6.pack(side=TOP)

############## BUILD INTO BOT RIGHT FRAME ##############
########################################################
e0 = Entry(frameBotRight)
e1 = Entry(frameBotRight)
e2 = Entry(frameBotRight)
e3 = Entry(frameBotRight)
e4 = Entry(frameBotRight)
e5 = Entry(frameBotRight)
e6 = Entry(frameBotRight)
e7 = Entry(frameBotRight)
e0.pack(side=TOP)
e1.pack(side=TOP)
e2.pack(side=TOP)
e3.pack(side=TOP)
e4.pack(side=TOP)
e5.pack(side=TOP)
e6.pack(side=TOP)
e7.pack(side=TOP)

#pack all the frames
frameLeft.pack(side = LEFT)
frameRight.pack(side = RIGHT)
frameTopRight.pack(side=TOP)
frameBotRight.pack(side=TOP)
frameTopLeft.pack(side=TOP)
frameMidLeft.pack(side=TOP)
frameBotLeft.pack(side=TOP)

#create the publishers
pub = rospy.Publisher('sliderData', Float32MultiArray, queue_size=20)
# rospy.Subscriber("fail_safe",Bool, lostSignal)
# rospy.Subscriber("pwm_control", UInt8MultiArray, updatePWM)
rospy.init_node('tkinterGUI', anonymous=True)

#run the loop indefinitely
root.mainloop()