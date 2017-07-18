# mdoap package
Finds obstacle objects ("ducks" / "cones") and the distance to them

# to test static object detector:
run [`static_object_detector_node_test.launch`](https://github.com/OSLL/Duckietown-Software/blob/master/catkin_ws/src/mdoap/launch/static_object_detector_node_test.launch)

You should see the image with the selected frame and the signed found objects (ducks and / or cones) in `/duckmobile/static_object_detector_node/cone_detection_image` topic and list of detected objects in `/duckmobile/static_object_detector_node/detection_list` topic

# How detection works

[static_object_detector_node](https://github.com/OSLL/Duckietown-Software/blob/master/catkin_ws/src/mdoap/src/static_object_detector_node.py) receives raw image from camera. 
It finds a cluster of pixels defined for the duck (yellow and shades) and cone (red and shades) color and size 
(all sizes and numbers are hardcoded in the code). 
The node is able to recognize only 2 of these "objects". 
The result is:
* list of found objects in `~detection_list` topic ([ObstacleImageDetection.msg](https://github.com/OSLL/Duckietown-Software/blob/master/catkin_ws/src/duckietown_msgs/msg/ObstacleImageDetection.msg) where [ObstacleType](https://github.com/OSLL/Duckietown-Software/blob/master/catkin_ws/src/duckietown_msgs/msg/ObstacleType.msg)) 
* image on which the found objects are taken in the frame and signed in `~cone_detection_image` topic

[obstacle_safety_node](https://github.com/OSLL/Duckietown-Software/blob/master/catkin_ws/src/mdoap/src/obstacle_safety_node.py) (subscribed to `~detection_list` topic) converts the coordinates of the area into the coordinates and the distance to the object. 
Publishes this data ([ObstacleProjectedDetection list](https://github.com/OSLL/Duckietown-Software/blob/master/catkin_ws/src/duckietown_msgs/msg/ObstacleProjectedDetection.msg)) in a topic `~detection_list_proj` and publishes BoolStamp in topic `~object_too_close`

[simple_stop_controller_node](https://github.com/OSLL/Duckietown-Software/blob/master/catkin_ws/src/mdoap/src/simple_stop_controller_node.py) (subscribed to `~object_too_close` chanel) and publish [Twist2DStamped](https://github.com/OSLL/Duckietown-Software/blob/master/catkin_ws/src/duckietown_msgs/msg/Twist2DStamped.msg)
to `~car_cmd` topic with `v` and `omega` equals zero and the same header 
