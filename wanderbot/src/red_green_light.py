#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist

cmd_vel_pub = rospy.Publisher('cmd_vel', Twist, queue_size=1)
rospy.init_node('red_green_light')
red_light_twist = Twist()
green_light_twist = Twist()
green_light_twist.linear.x = 0.5
driving_forward = False

rate = rospy.Rate(10)

#while rospy.Time.is_zero(rospy.Time.now()):
#    rate.sleep()
light_change_time = rospy.Time.now()

while not rospy.is_shutdown():
    if driving_forward:
        cmd_vel_pub.publish(green_light_twist)
    else:
        cmd_vel_pub.publish(red_light_twist)
    if light_change_time < rospy.Time.now():
        driving_forward = not driving_forward
        light_change_time = rospy.Time.now() + rospy.Duration(3)

    #print("current time = ", rospy.Time.now(), "change_time = ", light_change_time)
    rate.sleep()
