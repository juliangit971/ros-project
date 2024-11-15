#!/usr/bin/env

import rospy
import random 
from std_msgs.msg import Int32



def talk_to_me():
    pub = rospy.Publisher('sensor_topic', Int32, queue_size=10)
    
    rospy.init_node('publisher_node', anonymous=True)

    rate = rospy.Rate(1)

    rospy.loginfo("Publisher Node started, now publishing messages...")
    
    while not rospy.is_shutdown():
        msg = random.randint(0, 1000)
        pub.publish(msg)
        rate.sleep() 



if __name__ == "__main__":
    try:
        talk_to_me()
    except rospy.ROSInterruptException:
        pass
    