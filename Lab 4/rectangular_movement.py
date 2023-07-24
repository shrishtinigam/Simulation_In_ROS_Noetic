#!/usr/bin/env python3
# license removed for brevity
import rospy
import math
from geometry_msgs.msg import Twist
def rectangular_movement_node():
    pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
    rospy.init_node('tbsim_driver', anonymous=True)
    rate = rospy.Rate(1)
    i = 0
    f = 0
    while not rospy.is_shutdown():
        robot_velocity = Twist()
        if i == 0:
            if f == 0:
                i = 1
                f = 1
                robot_velocity.linear.x = 4.5
                robot_velocity.angular.z = 0
            else:
                robot_velocity.linear.x = 1.5
                robot_velocity.angular.z = 0
                i = 1
                f = 0
        else:
            robot_velocity.linear.x = 0
            robot_velocity.angular.z = math.pi/2
            i = 0
    pub.publish(robot_velocity)
    rate.sleep()
if __name__ == '__main__':
    try:
        rectangular_movement_node()
    except rospy.ROSInterruptException:
        pass