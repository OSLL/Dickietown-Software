#!/bin/bash
roslaunch duckietown_demos master.launch \
veh:=duckmobile joystick:=false coordination:=true navigation:=true apriltags:=true \
verbose:=true anti_instagram:=false \
intersectionType:=any \
/LED/emitter:=false /LED/detector:=true /LED/interpreter:=true \
visualization:=false \
/camera/raw:=true /camera/raw/rect:=true \
obstacle_avoidance:=false /obstacle_avoidance/safety:=false /obstacle_avoidance/detection:=false \
lane_following:=true line_detector_param_file_name:=osll
