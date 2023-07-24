#!/usr/bin/env python3
# licence removed for brevity
import rospy
from std_msgs.msg import String
def encrypt(text, s):
    result = ""
    for i in range(len(text)):
        char = text[i]
        if(char.isupper()):
            result += chr((ord(char) + s-65) % 26 + 65)
        else:
            result += chr((ord(char) + s-97) % 26 + 97)
        return result
def talker():
    pub = rospy.Publisher('topic1', String, queue_size = 10)
    rospy.init_node('talker1', anonymous=True)
    rate = rospy.Rate(10)
    while not rospy.is_shutdown():
        hello_str = "VITCC"
        hello_str = encrypt(hello_str, 3)
        rospy.loginfo(hello_str)
        pub.publish(hello_str)
        rate.sleep()
if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass