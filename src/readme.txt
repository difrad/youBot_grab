youBot moveIt Configuration
=============


Introduction
------------------
This configuration files are were created with the setup wizard of moveIt. Also a launch-file is added to use this configuration with my moveIt controller manager.


Starting from a cold start
------------------
* in terminal, source your environment with "source devel/bash" and "source ~/catkin_ws/devel/setup.bash"
* Verify that the ethernet-to-usb connection to the computer is broken
* Power the robot on by pressing the red illuminated button.  It should turn green.
* Plug in the ethernet-to-usb connection into the LEFT USB port (the right port seemed glitchy for unknown reasons)
* Launch the ROS project using "roslaunch youbot_moveit_configuration robotRun.launch" in the same terminal as where sourcing occured
* The robot should go through a calibration sequence, a GUI should also open.  The initialization is complete when the grippers (try to) open and close
* Verify that the grippers begin in the fully CLOSED position.  This particular youBot has a stick gripper that is unreliable.  If the grippers are not in the fully closed position, follow the instructions below to manually open and close the grippers while providing a gental amount of physical assistance with your hands.
* IMPORTANT: Once the grippers have been begun in the CLOSED position, manually control the robot to fully OPEN 'm6_grip_l', which should move without any issues.  If this is not done, then the robot may crash upon retrieving its first block.

Navigating the GUI
---------------------
* To manually control the robot:
	* Click "Enable Robot"
	* Under "Solver", select "Forward kinematics"
	* Select desired joint angles.  Please be mindful of the robot's position and conscious of crashes.  Upon calibration, the robot starts in the zero position.
	* Select "Execute" to move to the joint angles.
* To grab a block:
	* Select the corresponding block number that you would like to retrieve.  Start at block 0 and increment up.  Be mindful of crashes, as no collision checks are being run.  

Editing the Script
------------------
* gui.py is where nearly all of the scripting is done.  
* To edit where the blocks are dispensed, modify 'targetList'
* To edit where 'left' and 'right' are, edit the joint angles under 'configurations'.  Note that the list of numbers correlate to m0 thru m4 in manual mode.
* To edit where the arm goes to retrieve a block, edit 'moveList'.  Each list has two lists of motor configurations nested within it.  The first list corresponds to the "approach" of the robot, whereas the second list corresponds to the "grasp" of the robot.  'grabAngles' dictates the angle of the robot's base, which corresponds to the four block hoppers.
* To change which GUI button corresponds to which block, edit variables 'b4' thru 'b23' by changing the value of 'moveFromButtonPress'.

Error Handling
-----------------
Issue: "Lost Ethercat connection"
Solution: control+c the command, unplug USB, power robot off (note that gravity kicks in pretty damn quick), power robot on, plug in USB, rerun the launch command.  This issue seems to be common if the physical ethernet connection is wiggled too much, so try to keep the computer in one place.

Issue: gripper connection lost
Solution: same as above.  The gripper connection appears to be the most sensitive, and has gone out in the middle of experimentation.  This can lead to crasehs, so it's important to address this issue when running manipulation tasks.

Issue: robot doesn't seem to complete its calibration
Solution: Power the robot off, rotate the robot's base motor to one of its hard stops, and back off about 30 degrees.  I suspect its the robot's limit switch being buggy, but the robot operates pretty normal in practical use.

Issue: gripper is stuck
Solution: Go into forward kinematic mode, instruct the gripper to open and close.  You'll hopefully hear the motor trying to turn.  As it tries to move, use your finger to provide a few pounds of extra force on the gripper.  Careful not to push the gripper past its center, as it may lose its threading.

Dependencies
------------------
* ROS-Environment
* moveIt-Controller-Manager
* a trajectory controller of your choice

(Helpful hint: ROS is much easier to navigate with liberal use of the tab button)

(Learn about ROS here: wiki.ros.org)