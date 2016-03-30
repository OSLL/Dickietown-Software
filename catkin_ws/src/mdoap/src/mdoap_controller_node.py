#!/usr/bin/env python
import rospy
from duckietown_msgs.msg import WheelsCmdStamped, BoolStamped, ObstacleProjectedDetectionList, ObstacleProjectedDetection

class MDOAPControllerNode:
    def __init__(self):
        self.name = 'mdoap_controller_node'
        rospy.loginfo('[%s] started', self.name)
        self.sub_close = rospy.Subscriber("~too_close", BoolStamped, self.cbBool, queue_size=1)
        self.sub_detections = rospy.Subscriber("~detection_list_proj", ObstacleProjectedDetectionList, self.cbDetections, queue_size=1)
        self.pub_wheels_cmd = rospy.Publisher("~control",WheelsCmdStamped,queue_size=1)
        self.too_close = False

    def setupParameter(self,param_name,default_value):
        value = rospy.get_param(param_name,default_value)
        rospy.set_param(param_name,value) #Write to parameter server for transparancy
        rospy.loginfo("[%s] %s = %s " %(self.node_name,param_name,value))
        return value
    def cbBool(self, bool_msg):
        self.too_close = bool_msg.data
    def cbDetections(self, detections_msg):
        if self.too_close:
            minDist = 999999999999999999999.0
            offset = 0.0
            # + -> offset to left in lane
            # - -> offset to right in lane
            for projected in detections_msg.list:
                if projected.distance <minDist:
                    offset = projected.location.y * 2.0
            #Hijack the param for seting offset of the lane
            self.setupParameter("lane_controller/d_offset", offset)
        else:
            #Reset offset of lane to 0
            self.setupParameter("lane_controller/d_offset", 0.0)
        stop = WheelsCmdStamped()
        stop.header = bool_msg.header
        stop.vel_left = 0.0
        stop.vel_right = 0.0
        self.pub_wheels_cmd.publish(stop)

if __name__=="__main__":
    rospy.init_node('mdoap_controller_node')
    node = MDOAPControllerNode()
    rospy.spin()