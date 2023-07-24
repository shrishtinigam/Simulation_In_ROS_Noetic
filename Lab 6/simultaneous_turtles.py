#!/usr/bin/env python3
import rospy
from geometry_msgs.msg import Twist
from turtlesim.srv import Spawn
import time
def create_turtle1():
 rospy.wait_for_service('spawn')
 spawner = rospy.ServiceProxy('spawn', Spawn)
 turtle1_x = 1
 turtle1_y = 1
 turtle1_theta = 0
 turtle1_name = "turtle2"
 spawner(turtle1_x, turtle1_y, turtle1_theta, turtle1_name)
def create_turtle2():
 rospy.wait_for_service('spawn')
 spawner = rospy.ServiceProxy('spawn', Spawn)
 turtle2_x = 9
 turtle2_y = 9
 turtle2_theta = 0
 turtle2_name = "turtle3"
 spawner(turtle2_x, turtle2_y, turtle2_theta, turtle2_name)
def move_turtle1():
 pub = rospy.Publisher('/turtle2/cmd_vel', Twist, queue_size=10)
 rate = rospy.Rate(10)
 twist = Twist()
 twist.linear.x = 2
 twist.angular.z = 2
 while not rospy.is_shutdown():
    pub.publish(twist)
    time.sleep(0.1)
    move_turtle2()
    #rate.sleep()
 
def move_turtle2():
 pub = rospy.Publisher('/turtle3/cmd_vel', Twist, queue_size=10)
 rate = rospy.Rate(10)
 twist = Twist()
 twist.linear.x = -2
 twist.angular.z = -2
 while not rospy.is_shutdown():
    pub.publish(twist)
    time.sleep(0.1)
    move_turtle1()
    #rate.sleep()
if __name__ == '__main__':
 try:
    rospy.init_node('turtle_spawner')
    create_turtle1()
    create_turtle2()
    move_turtle1()
 #move_turtle2()
 except rospy.ROSInterruptException:
    pass