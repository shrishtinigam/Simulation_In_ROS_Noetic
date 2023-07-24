#!/usr/bin/env python3
# license removed for brevity
import rospy
import math
from geometry_msgs.msg import Twist
def triangular_movement_node():
    pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
    rospy.init_node('tbsim_driver', anonymous=True)
    rate = rospy.Rate(1)
    i = 0
    while not rospy.is_shutdown():
        robot_velocity = Twist()
        if i < 1:
            robot_velocity.linear.x = 4.5
            robot_velocity.angular.z = 0
            i += 1
        else:
            robot_velocity.linear.x = 0
            robot_velocity.angular.z = math.pi/1.5
            i = 0
        pub.publish(robot_velocity)
        rate.sleep()
if __name__ == '__main__':
    try:
        triangular_movement_node()
    except rospy.ROSInterruptException:
        pass
