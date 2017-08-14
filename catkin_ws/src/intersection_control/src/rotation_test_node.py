#!/usr/bin/env python
import rospy
from duckietown_msgs.msg import FSMState, BoolStamped, Twist2DStamped, LanePose, StopLineReading
from std_srvs.srv import EmptyRequest, EmptyResponse, Empty
from std_msgs.msg import String, Int16 #Imports msg
import copy

class RotationTestNode(object):
    def __init__(self):
        # Save the name of the node
        self.node_name = rospy.get_name()

        # Construct originalManeuvers
        self.originalManeuvers = dict()

        self.originalManeuvers[0] = self.getManeuver("turn_left")
        self.originalManeuvers[1] = self.getManeuver("turn_forward")
        self.originalManeuvers[2] = self.getManeuver("turn_right")
        # self.originalManeuvers[-1] = self.getManeuver("turn_stop")
        self.maneuvers = copy.deepcopy(self.originalManeuvers)

        self.srv_turn_left = rospy.Service("~turn_left", Empty, self.cbSrvLeft)
        self.srv_turn_right = rospy.Service("~turn_right", Empty, self.cbSrvRight)
        self.srv_turn_forward = rospy.Service("~turn_forward", Empty, self.cbSrvForward)

    def cbSrvLeft(self,req):
        self.trigger(0)
        return EmptyResponse()

    def cbSrvForward(self,req):
        self.trigger(1)
        return EmptyResponse()

    def cbSrvRight(self,req):
        self.trigger(2)
        return EmptyResponse()


    def getManeuver(self,param_name):
        param_list = rospy.get_param("~%s"%(param_name))
        # rospy.loginfo("PARAM_LIST:%s" %param_list)
        maneuver = list()
        for param in param_list:
            maneuver.append((param[0],Twist2DStamped(v=param[1],omega=param[2])))
        # rospy.loginfo("MANEUVER:%s" %maneuver)
        return maneuver

    def trigger(self,turn_type):
        for index, pair in enumerate(self.maneuvers[turn_type]):
            rospy.loginfo("[%s] drive %s sec", self.node_name, pair[0])
            cmd = copy.deepcopy(pair[1])
            start_time = rospy.Time.now()
            end_time = start_time + rospy.Duration.from_sec(pair[0])
            while rospy.Time.now() < end_time:
                cmd.header.stamp = rospy.Time.now()
                self.pub_cmd.publish(cmd)
                self.rate.sleep()

    def on_shutdown(self):
        rospy.loginfo("[%s] Shutting down." %(self.node_name))

if __name__ == '__main__':
    # Initialize the node with rospy
    rospy.init_node('rotation_test_node', anonymous=False)

    # Create the NodeName object
    node = RotationTestNode()

    # Setup proper shutdown behavior
    rospy.on_shutdown(node.on_shutdown)
    # Keep it spinning to keep the node alive
    rospy.spin()
