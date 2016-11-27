#!/usr/bin/env python
import rospy
from std_msgs.msg import Float32MultiArray
from brics_actuator.msg import JointPositions
from brics_actuator.msg import JointValue

def armCommand(data):
    rospy.loginfo(rospy.get_caller_id() + "I heard %s", data.data)

    #creating a JointValue() List/Array
    jvaluelist = [0 for i in range(5)]    

    #creating a JointValue() Object for joint 1 (base)
    jvalue1 = JointValue()
    jvalue1.joint_uri = 'arm_joint_1'
    jvalue1.unit = 'rad'
    jvalue1.value = data.data[0]
    jvaluelist[0] = jvalue1    

    #creating a JointValue() Object for joint 2
    jvalue2 = JointValue()
    jvalue2.joint_uri = 'arm_joint_2'
    jvalue2.unit = 'rad'
    jvalue2.value = data.data[1]
    jvaluelist[1] = jvalue2

    #creating a JointValue() Object for joint 3
    jvalue3 = JointValue()
    jvalue3.joint_uri = 'arm_joint_3'
    jvalue3.unit = 'rad'
    jvalue3.value = data.data[2]
    jvaluelist[2] = jvalue3

    #creating a JointValue() Object for joint 4    
    jvalue4 = JointValue()
    jvalue4.joint_uri = 'arm_joint_4'
    jvalue4.unit = 'rad'
    jvalue4.value = data.data[3]
    jvaluelist[3] = jvalue4

    #creating a JointValue() Object for joint 5    
    jvalue5 = JointValue()
    jvalue5.joint_uri = 'arm_joint_5'
    jvalue5.unit = 'rad'
    jvalue5.value = data.data[4]
    jvaluelist[4] = jvalue5

    #setting JointPosition msg properties 
    pub = rospy.Publisher('arm_1/arm_controller/position_command',JointPositions)
    rate = rospy.Rate(20)
    msg = JointPositions()
    msg.positions = jvaluelist
    pub.publish(msg)
    
def listener():
    rospy.init_node('fk', anonymous=True)
    rospy.Subscriber("/moveArm", Float32MultiArray, armCommand)

    rospy.spin()

if __name__ == '__main__':
    listener()