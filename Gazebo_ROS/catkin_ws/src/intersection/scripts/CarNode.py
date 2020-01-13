#!/usr/bin/env python



import rospy
from intersection.srv import *
import Car_Class as CC
from geometry_msgs.msg import Twist
from nav_msgs.msg import Odometry
import subprocess
import os
instructions = []


#global variables
global distance
removed = 0


def InitialRequest_Client(inOut, vin, speed, accel, enterTime, lane, turn, length, width):
    print("trying to connect")
    rospy.wait_for_service('InitialRequest')
    print("connectde")
    try:
        InitialRequest = rospy.ServiceProxy('InitialRequest', CarComOne)
        resp1 = InitialRequest(inOut, vin, speed, accel, enterTime, lane, turn, length, width)
        return resp1.requestedAccel, resp1.expectedTime
    except rospy.ServiceException, e:
        print "Service call failed: %s"%e

#get things moving
def mover(name, speed):

    destination = "{}/cmd_vel".format(name)
    print (name, speed)
    velocity_publisher = rospy.Publisher(destination, Twist, queue_size=10)

    vel_msg = Twist()
    vel_msg.linear.x = abs(speed)
    # Since we are moving just in x-axis
    vel_msg.linear.y = 0
    vel_msg.linear.z = 0
    vel_msg.angular.x = 0
    vel_msg.angular.y = 0
    vel_msg.angular.z = 0
    velocity_publisher.publish(vel_msg)


#get data to establish car
data =[0,0,0,0,0,0,0,0]
data[0] = rospy.get_param('/vin')
data[1] = rospy.get_param('/speed')
data[2] = rospy.get_param('/accel')
data[3] = rospy.get_param('/now')
data[4] = rospy.get_param('/lane')
data[5] = rospy.get_param('/turn')
data[6] = rospy.get_param('/length')
data[7] = rospy.get_param('/width')
name = rospy.get_param('/name')

#set up new node for this car
rospy.init_node(str(name), anonymous=True)


#sleep for a bit...
print("waiting\n\n\n")
rospy.wait_for_service('/robo_0/robot_state_publisherrobo_0/set_logger_level')
print("NOT waiting \n\n\n")


#creat car class instance and a reservation ticket
tempCar = CC.Car(data[0],data[1],data[2],data[3],data[4],data[5],data[6],data[7])
tempRes = tempCar.generatereservation()

#request accelValue
print(data)
instructions = InitialRequest_Client(0,data[0],data[1],data[2],data[3],data[4],data[5],data[6],data[7])
print (instructions)

tempCar.updateAccel01(instructions)


distance = 0.0

#keep updating velocity
def my_callback(event):
    global distance
    time = (rospy.get_rostime().to_nsec() / 10 ** 6)
    if(time >= instructions[1]) and (tempCar.set != 1):  #get output instructions
         outrRes = tempCar.generatereservationOUT()
         tempCar.set = 1
         tempCar.updateAccel1(InitialRequest_Client(1,outrRes[0],outrRes[1],outrRes[2],outrRes[3],outrRes[4],outrRes[5],outrRes[6],outrRes[7]))
        # print("got Outro")

    if(time >= data[3]):   #if has started
        d = tempCar.velocity01(time)
        #print(d)
        distance = (0.02 * d) + distance

       # print("Distance Travlled: " + str(distance))
        #print("-----------------------------------")
        name = "robo_{}".format(data[0])
        mover(name, d)
        #print("##################################")
    else:
        print("car not ready: " + str(data[0]) )

#check when to delete
def ODOM(data):
    global removed
    #if ((abs(data.pose.pose.position.y) > 205) or ( (abs(data.pose.pose.position.x) > 205)) and removed == 0):
        #name = "robo_{}".format(tempCar.vin)
        #string = "rosservice call gazebo/delete_model '{model_name: " + str(name) + "}'"
        #print (string)
        #removed = 1 #so does not try to reomve twice by mistake
        #subprocess.call(string,shell=True)
        #rospy.signal_shutdown("out of range")



#internal timers
rospy.Subscriber(str(name) +"/odom", Odometry, ODOM)
rospy.Timer(rospy.Duration(0.02), my_callback)  #update car every 0.02 seconds (50Hz)





###########################################
rospy.spin()

