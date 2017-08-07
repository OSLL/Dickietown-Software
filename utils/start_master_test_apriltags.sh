#!/bin/bash
roslaunch duckietown_demos master.launch \
veh:=duckmobile joystick:=false coordination:=false navigation:=false \
verbose:=true anti_instagram:=false \
intersectionType:=plain \
/LED/emitter:=false /LED/detector:=false /LED/interpreter:=false \
visualization:=false \
/camera/raw:=true /camera/raw/rect:=true \
/navigation/apriltags_random:=false apriltags:=true \
obstacle_avoidance:=false /obstacle_avoidance/safety:=false /obstacle_avoidance/detection:=false \
lane_following:=false line_detector_param_file_name:=osll
