#!/usr/bin/env python3
import rospy
from std_msgs.msg import String
def callback(data):
    rospy.loginfo(rospy.get_caller_id() + " Packet: %s" , data.data)
def listener():
    rospy.init_node('listerner1', anonymous=True)
    rospy.Subscriber('topic1', String, callback)
    rospy.spin()
if __name__ == '__main__':
    listener()