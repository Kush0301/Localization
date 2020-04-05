#!usr/bin/env python
import rospy
from geometry_msgs.msg import Twist

def callback(msg):
	linear_vel_x=msg.linear.x
	linear_vel_y=msg.linear.y
	linear_vel_z=msg.linear.z
	linear_data=[linear_vel_x,linear_vel_y,linear_vel_z]
	angular_vel_x=msg.angular.x
	angular_vel_y=msg.angular.y
	angular_vel_z=msg.angular.z
	angular_data=[angular_vel_x,angular_vel_y,angular_vel_z]
	print(linear_data,angular_data)
def main():
	rospy.init_node('odom')
	rospy.Subsrciber('mobile_base/commands/velocity',Twist,callback)
	rospy.spin()
if __name__='__main()__':
	main()
