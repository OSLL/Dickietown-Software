#!/bin/bash
source ./prepare.sh
roslaunch duckietown_demos master.launch veh:=duckmobile local:=true obstacle_avoidance:=true joystick:=false coordination:=true navigation:=true apriltags:=false anti_instagram:=false intersectionType:=trafficLight /LED/detector:=true /LED/interpreter:=true visualization:=false /navigation/apriltags_random:=false /obstacle_avoidance/safety:=false /obstacle_avoidance/detection:=false line_detector_param_file_name:=osll
