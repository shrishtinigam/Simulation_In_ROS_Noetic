#!/usr/bin/env python3
import rospy
from std_msgs.msg import String
def callback(data):
 rospy.loginfo(rospy.get_caller_id() + "I heard %s", data.data)
 
def listener():
 rospy.init_node('listener1', anonymous=True)
 rospy.Subscriber("\CSE3102", String, callback)
 # spin() simply keeps python from exiting until this node is stopped
 rospy.spin()
if __name__ == '__main__':
 listener()