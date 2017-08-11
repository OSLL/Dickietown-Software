#!/bin/bash
roslaunch duckietown_demos master.launch \
veh:=duckula joystick:=false coordination:=true navigation:=true \
verbose:=true anti_instagram:=false \
intersectionType:=plain \
/LED/emitter:=false /LED/detector:=true /LED/interpreter:=true \
visualization:=false \
/navigation/apriltags_random:=false apriltags:=false \
obstacle_avoidance:=false /obstacle_avoidance/safety:=false /obstacle_avoidance/detection:=false \
line_detector_param_file_name:=osll
