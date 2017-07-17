#!/bin/bash
source /home/ubuntu/github/Software/catkin_ws/devel/setup.bash
export PYTHONPATH=$PYTHONPATH:/home/ubuntu/ros_catkin_ws/install_isolated/lib/python2.7/site-packages
export ROS_HOSTNAME="duckmobile.local"
export ROSLAUNCH_SSH_UNKNOWN=1
export VEHICLE_NAME="duckmobile"
