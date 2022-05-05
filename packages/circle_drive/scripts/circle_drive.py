#!/usr/bin/env python3
import sys
import rospy
from duckietown.dtros import DTROS, NodeType
from duckietown_msgs.msg import Twist2DStamped

class MyNode(DTROS):
    def __init__(self, node_name):
        super(MyNode, self).__init__(node_name=node_name, node_type=NodeType.DEBUG)
        self.pub = rospy.Publisher("~car_cmd", twist2DStamped, queue_size=1)

    def run(self):
        while not rospy.is_shitdown():
            msg = Twist2DStamped()
            msg.v = 0.0
            msg.omega = 1.0
            self.pub.publish(msg)

        
if __name__ == "__main__":
    node = MyNode(node_name="circle_drive_node")
    node.run()
    rospy.spin()
