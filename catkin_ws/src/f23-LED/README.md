

LED emitter
-----------
The coordination team will use 3 signals: CAR_SIGNAL_A, CAR_SIGNAL_B, CAR_SIGNAL_C. 
To test the LED emitter with your joystick, run the following command:

	roslaunch led_joy_mapper led_joy_with_led_emitter_test.launch veh:=${VEHICLE_NAME}

This launches the joy controller, the mapper controller, and the led emitter nodes. You should not need to run anything external for this to work. Use the joystick buttons A, B and C to change your duckiebot’s LED’s blinking frequency.
Button A broadcasts signal CAR_SIGNAL_A (2.8hz), button B broadcasts signal CAR_SIGNAL_B (4.1hz), and button CAR_SIGNAL_C (Y on the controller) broadcasts signal C(5hz).The LB button will make the LEDs all white, the RB button will make some LEDs blue and some LEDs green, and the logitek button (middle button) will make the LEDs all red

Repeat this for each vehicle at the intersection that you wish to be blinking. Use previous command replacing ${VEHICLE_NAME} the names of the vehicles and try command different blinking patterns on different duckiebots.

(optional tests) For a grasp of the low level LED emitter, run:

	roslaunch led_emitter led_emitter_node.launch veh:=${VEHICLE_NAME}

You can then publish to the topic manually by running the following command in another screen on the duckiebot:

	rostopic pub /${VEHICLE_NAME}/led_emitter_node/change_to_state std_msgs/Float32 <float-value>

Where <float-value> is the desired blinking frequency, e.g. 1.0, .5, 3.0, etc. If you wish to run the LED emitter test, run the following:

	roslaunch led_emitter led_emitter_node_test.launch veh:=${VEHICLE_NAME}

This will cycle through frequencies of 3.0hz, 3.5hz, and 4hz every 5 seconds. Once done, kill everything and make sure you have joystick control as described above. 


LED detector 
-----------
Pick your favourite duckiebot as the observer-bot. Refer to it as ${VEHICLE_NAME} for this step. If you are in good company, this can be tried on all the available duckiebots. First, activate the camera on the observer-bot:

	roslaunch duckietown camera.launch veh:=${VEHICLE_NAME}

In a separate terminal, fire up the LED detector and the custom GUI by running:

	roslaunch led_detector LED_detector_with_gui.launch veh:=${VEHICLE_NAME} 

NOTE: to operate without a GUI:

	laptop $ roslaunch led_detector LED_detector.launch veh:=${VEHICLE_NAME} 
	
The LED_detector_node will be launched on the robot, while LED_visualizer (a simple GUI) will be started on your laptop. Make sure the camera image from the observer-bot is visualized and updated in the visualizer (tip: check that your camera cap is off).

Hit on Detect and wait to trigger a detection. This will not have any effect if LED_detector_node is not running on the duckiebot (it is included in the above launch file). After the capture and processing phases, the outcome will look like: 

The red numbers represent the frequencies directly inferred from the camera stream, while the selected detections with the associated signaling frequencies will be displayed in green.
You can click on the squares to visualize the brightness signals and the Fourier amplitude spectra of the corresponding cells in the video stream. You can also click on the camera image to visualize the variance map.

Unit tests
-----------

To run the unit tests for  the LED detector, you need to have the F23 rosbags on you hard disk. These bag files should be synced from this dropbox (https://www.dropbox.com/sh/5kx8qwgttu69fhr/AAASLpOVjV5r1xpzeW7xWZh_a?dl=0). For the test to locate the bag files, you should have the ${DUCKIETOWN_DATA} environment variable set, pointing to the location of you duckietown-data folder. This can be achieved by:

	export DUCKIETOWN_DATA=<local-path-to-duckietown-data-folder>

All the available tests are specified in file all_tests.yaml in the  scripts/ folder of the package led_detection in the duckietown ROS workspace. To run these, use the command:

	rosrun led_detection unittests.py ‘<algorithm>’ ‘<name-of-test>’

Currently, <algorithm> can be either ‘baseline’ or ‘LEDDetector_plots’ to also display the plot in the process. 
To run all test with all algorithms, execute:

	rosrun led_detection unittests.py '*' '*'

How detection and interpretation works
-----------
[LED_detector_node](https://github.com/OSLL/Duckietown-Software/blob/master/catkin_ws/src/f23-LED/led_detection/src/LED_detector_node.py) node receives the image from the camera. The process of detection is triggered by the flag in the topic <i>/duckmobile/LED_detector_node/trigger</i>. The result of the work of [LED_detector_node](https://github.com/OSLL/Duckietown-Software/blob/master/catkin_ws/src/f23-LED/led_detection/src/LED_detector_node.py) is an [LEDDetectionArray](https://github.com/OSLL/Duckietown-Software/blob/master/catkin_ws/src/duckietown_msgs/msg/LEDDetectionArray.msg) (array of [LEDDetection](https://github.com/OSLL/Duckietown-Software/blob/master/catkin_ws/src/duckietown_msgs/msg/LEDDetection.msg)) in the topic <i>raw_led_detection</i>.

For interpretation, as it is not strange, the node [LED_interpreter_node](https://github.com/OSLL/Duckietown-Software/blob/master/catkin_ws/src/f23-LED/led_interpreter/src/LED_interpreter_node.py) answers. The node get data from <i>raw_led_detection</i> topic and uses parameters from configuration files [location_config](https://github.com/OSLL/Duckietown-Software/blob/master/catkin_ws/src/duckietown/config/baseline/led_interpreter/location_config.yaml) to determine the scope boundaries and [LED_protocol](https://github.com/OSLL/Duckietown-Software/blob/master/catkin_ws/src/duckietown/config/baseline/led_interpreter/LED_protocol.yaml) where the colors and frequencies of the led signals are described.
The result of the interpretation ([SignalsDetection](https://github.com/OSLL/Duckietown-Software/blob/master/catkin_ws/src/duckietown_msgs/msg/SignalsDetection.msg)) is published in the topic <i>signals_detection</i>
