#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist



def mover(name, speed):

    destination = "{}/cmd_vel".format(name)
    velocity_publisher = rospy.Publisher(destination, Twist, queue_size=10)
    print("\n\n\n name:   " + str(name))

    rospy.sleep(0.5)
    vel_msg = Twist()





    vel_msg.linear.x = abs(speed)
    #Since we are moving just in x-axis
    vel_msg.linear.y = 0
    vel_msg.linear.z = 0
    vel_msg.angular.x = 0
    vel_msg.angular.y = 0
    vel_msg.angular.z = 0

    #Publish the velocity
    velocity_publisher.publish(vel_msg)
    return


#rospy.init_node("velocity_controller")