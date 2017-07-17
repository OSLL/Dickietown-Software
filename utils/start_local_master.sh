#!/bin/bash
source ./prepare_bot.sh
roslaunch duckietown_demos master.launch veh:=duckmobile local:=true obstacle_avoidance:=true joystick:=false coordination:=true navigation:=true apriltags:=true intersectionType:=trafficLight
