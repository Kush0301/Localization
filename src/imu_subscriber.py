#!/usr/bin/env python

import rospy
import tf
from geometry_msgs.msg import Twist,PoseStamped,Quaternion
from geometry_msgs.msg import PoseWithCovarianceStamped
from nav_msgs.msg import Odometry
from std_msgs.msg import Empty
from sensor_msgs.msg import Imu


def callbackimu(data,pub):
    pose = PoseStamped()
    pose.header = data.header
    quaternion = (
    data.orientation.x,
    data.orientation.y,
    data.orientation.z,
    data.orientation.w)

    euler = tf.transformations.euler_from_quaternion(quaternion)

    pose.pose.orientation.x = euler[0]
    pose.pose.orientation.y = euler[1]
    pose.pose.orientation.z = euler[2]
    pub.publish(pose)

def pubeuler():
  
    rospy.init_node('pub_euler')
    pubimu = rospy.Publisher('euler_imu', PoseStamped,queue_size = 10)

    rospy.Subscriber('/android/imu',Imu,callbackimu, callback_args=pubimu)


    rospy.spin()


if __name__ == '__main__':
    
    
    pubeuler()
