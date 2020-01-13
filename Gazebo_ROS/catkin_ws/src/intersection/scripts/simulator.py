#!/usr/bin/env python
import Intersection_Manager_class as IMC


import random
import csv
import rospy
import spawner
from intersection.srv import *
import subprocess



#setup
list_car_data = []
pastLane = None
startTime = 0

numberOfCars = 5
speedLimit = 35
maxSpeed = 3500
minSpeed = 3000



#used for generating data (globals)
count = 0
delay = 0
lane = 0


#helpful dictionaries
xpos_dict =	{
  1: "5",
  2: "200",
  3: "-5",
  4: "-200"
}
ypos_dict =	{
  1: "-200",
  2: "5",
  3: "200",
  4: "-5"
}
YAWpos_dict =	{
  1: "1.5707",
  2: "3.1415",
  3: "-1.5707",
  4: "0"
}

lane = 0

def genData():
    global count
    global delay
    global lane
    global pastLane
    vin = count
    lane = ((count + 1) % 4) + 1 #random.randint(1, 4) #

    delay = random.randrange(250, 500, 1)
    speed = random.randrange(minSpeed, maxSpeed, 1) / 100.00
    accel = 0.0#random.randrange(-20, 20, 1) / 100.0
    turn = random.randint(0, 1)
    length = random.randrange(20, 30, 1) / 10.0
    width = random.randrange(10, 20, 1) / 10.0
    now = (rospy.get_rostime().to_nsec() / 10 ** 6) + 1000 
    count = count + 1
    pastLane = lane
    return (vin, speed, accel, now, lane, turn, length, width)


#create a node
rospy.init_node("sim")

#build world delay
print("Starting world")
print("sleeping for 8 seconds to build world, then will create cars")
rospy.sleep(8)
print("done sleeping")

# generate cars :)
for i in range (numberOfCars):
    #generate data
    data = genData()
    print(data)

    #spawn model
    subprocess.Popen("roslaunch intersection alt.launch naming:=robo_"
                     + str(data[0])
                     + " x_pos:=" + str(xpos_dict[data[4]])
                     + " y_pos:=" + str(ypos_dict[data[4]])
                     + " yaw:=" + str(YAWpos_dict[data[4]])
                     + " vin:=" + str(data[0])
                     + " speed:=" + str(data[1])
                     + " accel:=" + str(data[2])
                     + " now:=" + str(data[3])
                     + " lane:=" + str(data[4])
                     + " turn:=" + str(data[5])
                     + " length:=" + str(data[6])
                     + " width:=" + str(data[7])
                     , shell = True) # naming:=robo_" + str(data[0]))


    #sleep zzzzz
    rospy.sleep(0.8)
    print("again")

    #name = "robo_{}".format(data[0])
    #mover(name, 50)


rospy.spin()

