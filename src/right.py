import rospy
from std_msgs.msg import Int32
from brics_actuator.msg import JointPositions
from brics_actuator.msg import JointValue

"""trying to create a python script equivalent of 
rostopic pub /arm_1/arm_controller/position_command brics_actuator/JointPositions '{positions:[ {joint_uri: arm_joint_1, unit: rad, value: 1.0}]}' """

pub_right = rospy.Publisher('arm_1/arm_controller/position_command', JointPositions, queue_size=15)
pub_gripper = rospy.Publisher('arm_1/gripper_controller/position_command', JointPositions, queue_size=15)

def callback(data):
    rospy.loginfo(data.data)
    
    #creating a JointValue() List/Array
    jvaluelist = [0 for i in range(5)]

    #creating a JointValue() Object for joint 1 (base)
    jvalue1 = JointValue()
    jvalue1.joint_uri = 'arm_joint_1'
    jvalue1.unit = 'rad'
    jvalue1.value = 0.632
    jvaluelist[0] = jvalue1

    #creating a JointValue() Object for joint 2
    jvalue2 = JointValue()
    jvalue2.joint_uri = 'arm_joint_2'
    jvalue2.unit = 'rad'
    jvalue2.value = 0.0039
    jvaluelist[1] = jvalue2

    #creating a JointValue() Object for joint 3
    jvalue3 = JointValue()
    jvalue3.joint_uri = 'arm_joint_3'
    jvalue3.unit = 'rad'
    jvalue3.value = -2.711
    jvaluelist[2] = jvalue3

    #creating a JointValue() Object for joint 4    
    jvalue4 = JointValue()
    jvalue4.joint_uri = 'arm_joint_4'
    jvalue4.unit = 'rad'
    jvalue4.value = 0.684
    jvaluelist[3] = jvalue4

    #creating a JointValue() Object for joint 5    
    jvalue5 = JointValue()
    jvalue5.joint_uri = 'arm_joint_5'
    jvalue5.unit = 'rad'
    jvalue5.value = 2.834
    jvaluelist[4] = jvalue5

    #setting JointPosition msg properties 
    rate = rospy.Rate(20)
    msg = JointPositions()
    msg.positions = jvaluelist
    pub_right.publish(msg)

    rospy.sleep(5)
    
    #creating a JointValue() List/Array
    jvaluegrippers = [0 for i in range(2)]

    #creating a JointValue() Object for gripper left    
    jvalue6 = JointValue()
    jvalue6.joint_uri = 'gripper_finger_joint_l'
    jvalue6.unit = 'm'
    jvalue6.value = 0.0115
    jvaluegrippers[0] = jvalue6

    #creating a JointValue() Object for gripper right
    jvalue7 = JointValue()
    jvalue7.joint_uri = 'gripper_finger_joint_r'
    jvalue7.unit = 'm'
    jvalue7.value = 0.0115
    jvaluegrippers[1] = jvalue7
    
    #setting JointPosition msg properties 
    rate = rospy.Rate(20)
    msg2 = JointPositions()
    msg2.positions = jvaluegrippers
    pub_gripper.publish(msg2)

def listener():
    #creating publisher, subscriber, and node
    rospy.Subscriber("right", Int32, callback)
    rospy.init_node('right')
    rospy.spin()


if __name__ == '__main__':
    listener()
    
