#!/bin/bash
roslaunch duckietown_demos master.launch \
veh:=duckmobile joystick:=false coordination:=true navigation:=true anti_instagram:=false \
intersectionType:=trafficLight \
/LED/emitter:=false /LED/detector:=false /LED/interpreter:=false \
visualization:=false \
/navigation/apriltags_random:=false apriltags:=false \
obstacle_avoidance:=true /camera/raw:=true \
line_detector_param_file_name:=osll
