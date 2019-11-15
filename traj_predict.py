# !usr/bin/env python
import rospy
import numpy as np
from nav_msgs.msg import Odometry

class EVDodge
	def __init__:
		self.object_sub = rospy.Subscriber('/evdodge_demo_ball/odom',Odometry,object_sub_cb )
		self.object_odom =  Odometry()

	def object_sub_cb(self,data):
		self.object_odom = data

	def predict_traj():


def main():
	EV_obj = EVDodge()



if __init__ == '__main__':
	main()
