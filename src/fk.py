#!/usr/bin/env python
import rospy
from std_msgs.msg import Float32MultiArray

def callback(data):
    rospy.loginfo(rospy.get_caller_id() + "I heard %s", data.data)
    
def listener():
    rospy.init_node('fk', anonymous=True)
    rospy.Subscriber("moveArm", Float32MultiArray, callback)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    listener()