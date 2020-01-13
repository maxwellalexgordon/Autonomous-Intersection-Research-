#!/usr/bin/env python

import sys
import rospy
from intersection.srv import *

def InitialRequest_Client(vin, speed, accel):
    rospy.wait_for_service('InitialRequest')
    try:
        InitialRequest = rospy.ServiceProxy('InitialRequest', CarComOne)
        resp1 = InitialRequest(vin, speed, accel, vin, speed, accel, vin, speed)
        return resp1.requestedAccel, resp1.expectedTime
    except rospy.ServiceException, e:
        print "Service call failed: %s"%e

def usage():
    return "something wqrong"

if __name__ == "__main__":
    if len(sys.argv) == 4:
        x = int(sys.argv[1])
        y = int(sys.argv[2])
        z = int(sys.argv[3])
    else:
        print usage()
        sys.exit(1)
   # print "Requesting Vin: %s Speed: %s  Accel: %s"%(x, y, z, x, x, x, x, x)
    print (InitialRequest_Client(x, y, x))
