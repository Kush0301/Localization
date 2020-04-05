#!/usr/bin/env python

import rospy
import tf
from geometry_msgs.msg import Twist,PoseStamped,Quaternion
from geometry_msgs.msg import PoseWithCovarianceStamped
from nav_msgs.msg import Odometry
from std_msgs.msg import Empty,Char,UInt8
from sensor_msgs.msg import Imu

def command_inputs():

    rospy.init_node('Command')
    pub = rospy.Publisher('command',UInt8,queue_size = 10)
    while(1):
        command = input('Command Input: ')
        print command
        pub.publish(command)
        


if __name__ == '__main__':
	command_inputs()

