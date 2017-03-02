youBot moveIt Configuration
=============


Introduction
------------------
This configuration files are were created with the setup wizard of moveIt. Also a launch-file is added to use this configuration with my moveIt controller manager.


Usage
------------------
* in terminal, source your environment with "source devel/bash" and "source ~/catkin_ws/devel/setup.bash"
* (optional) move into your ros environment with "cd catkin_ws/src"
* (optional) type 'ls' to familiarize with all the ROS projects
* Power cycle the robot by pressing the green button to red.  If the button is red, the robot's firmware and drivers are powered off.
* Verify the ethernet-to-usb connection is made and that it is plugged into the LEFT USB port (the right port seemed glitchy for unknown reasons)
* Launch the ROS project using "roslaunch youbot_moveit_configuration robotRun.launch"
* The robot should go through a calibration sequence, a GUI and a visualizer should also open

(Helpful hint: ROS is much easier to navigate with liberal use of the tab button)

(Learn about ROS here: wiki.ros.org)

Error Handling
-----------------
Issue: "Lost Ethercat connection"
Solution: control+c the command, unplug USB, power robot off (note that gravity kicks in pretty damn quick), power robot on, plug in USB, rerun the launch command.  This issue seems to be common if the physical ethernet connection is wiggled too much, so try to keep the computer in one place.

Issue: gripper connection lost
Solution: same as above.  The gripper connection appears to be the most sensitive, and has gone out in the middle of experimentation.  This can lead to crasehs, so it's important to address this issue when running manipulation tasks.

Issue: robot doesn't seem to complete its calibration
Solution: Rotate the robot's base motor to one of its hard stops, and back off about 30 degrees.  I suspect its the robot's limit switch being buggy, but the robot operates pretty normal in practical use.

Issue: gripper is stuck
Solution: Go into forward kinematic mode, instruct the gripper to open and close.  You'll hopefully hear the motor trying to turn.  As it tries to move, use your finger to provide a few pounds of extra force on the gripper.  Careful not to push the gripper past its center, as it may lose its threading.

Dependencies
------------------
* ROS-Environment
* moveIt-Controller-Manager
* a trajectory controller of your choice
