#!/usr/bin/env python

import rospy, tf
import numpy
from gazebo_msgs.srv import DeleteModel, SpawnModel
from geometry_msgs.msg import *
import sys
import roslib
import rospy
import os
import tf.transformations as tft
import math



def insertBot(name, x, y, yaw):
    #print("Waiting for gazebo services...")
    #rospy.init_node("spawn_products_in_bins")
    rospy.wait_for_service("gazebo/spawn_urdf_model")
    print("Got it.")
    s = rospy.ServiceProxy("gazebo/spawn_urdf_model", SpawnModel)

    file_location = "/home/maxwell/catkin_ws/src/turtlebot3/turtlebot3_description/urdf/turtlebot3_burger.urdf.xacro"
    #file_location = "/home/maxwell/catkin_ws/src/jackal/jackal_description/urdf/jackal.urdf.xacro"
    p = os.popen("rosrun xacro xacro.py " + file_location)
    xml_string = p.read()

    print("setting up orientation and position")
    position = [x, y, 0]
    orientation = [0, 0, yaw]
    quaternion = tft.quaternion_from_euler(orientation[0], orientation[1], orientation[2])

    object_pose = Pose()
    object_pose.position.x = float(position[0])
    object_pose.position.y = float(position[1])
    object_pose.position.z = float(position[2])
    object_pose.orientation.x = quaternion[0]
    object_pose.orientation.y = quaternion[1]
    object_pose.orientation.z = quaternion[2]
    object_pose.orientation.w = quaternion[3]


    print("prep spawn")
    print("Spawning model:", name)
    s(name, xml_string, "", object_pose, "world")






