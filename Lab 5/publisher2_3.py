#!/usr/bin/env python3
# licence removed for brevity
import rospy
import random
from std_msgs.msg import String
def talker():
    pub = rospy.Publisher('topic1', String, queue_size = 10)
    rospy.init_node('talker1', anonymous=True)
    rate = rospy.Rate(10)
    while not rospy.is_shutdown():
        n = random.randint(1, 100)
        rospy.loginfo(str(n))
        pub.publish(str(n))
        rate.sleep()
if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
