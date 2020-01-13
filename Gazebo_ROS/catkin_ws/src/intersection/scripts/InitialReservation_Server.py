#!/usr/bin/env python
import Intersection_Manager_class as IMC
import Car_Class as CC
from intersection.srv import *
import rospy

# set up
NAME = 'InitialRequest_Server'
manager = IMC.Intersection_Manager()


def InitialRequest(req):
    res = IMC.IC.Reservation(req.vin, req.speed, req.accel, req.enterTime, req.lane, req.turn, req.length, req.width)
    if (req.inOut == 0):
        data = manager.addReservation(res)
    else:
        data = manager.bookOutro(res)
    print("\n\n\n got a request \n\n\n")
    print(manager.toString())
    return CarComOneResponse(data[0], data[1])


def InitialRequest_Server():
    rospy.init_node(NAME)
    s = rospy.Service('InitialRequest', CarComOne, InitialRequest)
    print("Ready to accept a request!")
    # spin() keeps Python from exiting until node is shutdown
    rospy.spin()


InitialRequest_Server()
