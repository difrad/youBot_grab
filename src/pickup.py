import rospy
from std_msgs.msg import Int32
from brics_actuator.msg import JointPositions
from brics_actuator.msg import JointValue

"""trying to create a python script equivalent of 
rostopic pub /arm_1/arm_controller/position_command brics_actuator/JointPositions '{positions:[ {joint_uri: arm_joint_1, unit: rad, value: 1.0}]}' """

pub_pickup = rospy.Publisher('arm_1/arm_controller/position_command', JointPositions, queue_size=15)
pub_gripper = rospy.Publisher('arm_1/gripper_controller/position_command', JointPositions, queue_size=15)

def callback(data):
    rospy.loginfo(data.data)
    
    #move gripper to correct pickup position

    #creating a JointValue() List/Array
    jvaluelist = [0 for i in range(5)]

    #creating a JointValue() Object for joint 1 (base)
    jvalue1 = JointValue()
    jvalue1.joint_uri = 'arm_joint_1'
    jvalue1.unit = 'rad'
    jvalue1.value = 2.926
    jvaluelist[0] = jvalue1

    #creating a JointValue() Object for joint 2
    jvalue2 = JointValue()
    jvalue2.joint_uri = 'arm_joint_2'
    jvalue2.unit = 'rad'
    jvalue2.value = 1.2326
    jvaluelist[1] = jvalue2

    #creating a JointValue() Object for joint 3
    jvalue3 = JointValue()
    jvalue3.joint_uri = 'arm_joint_3'
    jvalue3.unit = 'rad'
    jvalue3.value = -4.00
    jvaluelist[2] = jvalue3

    #creating a JointValue() Object for joint 4    
    jvalue4 = JointValue()
    jvalue4.joint_uri = 'arm_joint_4'
    jvalue4.unit = 'rad'
    jvalue4.value = 1.700
    jvaluelist[3] = jvalue4

    #creating a JointValue() Object for joint 5    
    jvalue5 = JointValue()
    jvalue5.joint_uri = 'arm_joint_5'
    jvalue5.unit = 'rad'
    jvalue5.value = 2.908
    jvaluelist[4] = jvalue5

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
    msg = JointPositions()
    msg2 = JointPositions()
    msg.positions = jvaluelist
    msg2.positions = jvaluegrippers
    pub_pickup.publish(msg)
    pub_gripper.publish(msg2)

    rospy.sleep(5)

    #extend gripper

    #creating a JointValue() Object for joint 1 (base)
    jvalue1 = JointValue()
    jvalue1.joint_uri = 'arm_joint_1'
    jvalue1.unit = 'rad'
    jvalue1.value = 2.926
    jvaluelist[0] = jvalue1

    #creating a JointValue() Object for joint 2
    jvalue2 = JointValue()
    jvalue2.joint_uri = 'arm_joint_2'
    jvalue2.unit = 'rad'
    jvalue2.value = 0.527
    jvaluelist[1] = jvalue2

    #creating a JointValue() Object for joint 3
    jvalue3 = JointValue()
    jvalue3.joint_uri = 'arm_joint_3'
    jvalue3.unit = 'rad'
    jvalue3.value = -3.419
    jvaluelist[2] = jvalue3

    #creating a JointValue() Object for joint 4    
    jvalue4 = JointValue()
    jvalue4.joint_uri = 'arm_joint_4'
    jvalue4.unit = 'rad'
    jvalue4.value = 1.703
    jvaluelist[3] = jvalue4

    #creating a JointValue() Object for joint 5    
    jvalue5 = JointValue()
    jvalue5.joint_uri = 'arm_joint_5'
    jvalue5.unit = 'rad'
    jvalue5.value = 2.908
    jvaluelist[4] = jvalue5

    #setting JointPosition msg properties 
    rate = rospy.Rate(20)
    msg = JointPositions()
    msg.positions = jvaluelist
    pub_pickup.publish(msg)

    rospy.sleep(5)

    #creating a JointValue() Object for gripper left    
    jvalue6 = JointValue()
    jvalue6.joint_uri = 'gripper_finger_joint_l'
    jvalue6.unit = 'm'
    jvalue6.value = 0.001
    jvaluegrippers[0] = jvalue6

    #creating a JointValue() Object for gripper right
    jvalue7 = JointValue()
    jvalue7.joint_uri = 'gripper_finger_joint_r'
    jvalue7.unit = 'm'
    jvalue7.value = 0.001
    jvaluegrippers[1] = jvalue7
    
    #setting JointPosition msg properties 
    rate = rospy.Rate(20)
    msg2 = JointPositions()
    msg2.positions = jvaluegrippers
    pub_gripper.publish(msg2)

    rospy.sleep(5)
    
    #retract arm

    #creating a JointValue() Object for joint 1 (base)
    jvalue1 = JointValue()
    jvalue1.joint_uri = 'arm_joint_1'
    jvalue1.unit = 'rad'
    jvalue1.value = 2.926
    jvaluelist[0] = jvalue1

    #creating a JointValue() Object for joint 2
    jvalue2 = JointValue()
    jvalue2.joint_uri = 'arm_joint_2'
    jvalue2.unit = 'rad'
    jvalue2.value = 1.2326
    jvaluelist[1] = jvalue2

    #creating a JointValue() Object for joint 3
    jvalue3 = JointValue()
    jvalue3.joint_uri = 'arm_joint_3'
    jvalue3.unit = 'rad'
    jvalue3.value = -4.00
    jvaluelist[2] = jvalue3

    #creating a JointValue() Object for joint 4    
    jvalue4 = JointValue()
    jvalue4.joint_uri = 'arm_joint_4'
    jvalue4.unit = 'rad'
    jvalue4.value = 1.700
    jvaluelist[3] = jvalue4

    #creating a JointValue() Object for joint 5    
    jvalue5 = JointValue()
    jvalue5.joint_uri = 'arm_joint_5'
    jvalue5.unit = 'rad'
    jvalue5.value = 2.908
    jvaluelist[4] = jvalue5

    #setting JointPosition msg properties 
    rate = rospy.Rate(20)
    msg = JointPositions()
    msg.positions = jvaluelist
    pub_pickup.publish(msg)

def listener():
    #creating publisher, subscriber, and node
    rospy.Subscriber("pickup", Int32, callback)
    rospy.init_node('pickup')
    rospy.spin()


if __name__ == '__main__':
    listener()
    
