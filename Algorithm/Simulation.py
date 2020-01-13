import Intersection_Manager_class as IMC
import Car_Class as CC
import Simulation_Settings as SS
import random
import csv
import time
import numpy as np
import mathHelp
import EnergyReview



manager = IMC.Intersection_Manager()
list_car_data = []
pastLane = None
startTime = 0
timeLimit = SS.Simulation_Settings.timeLimit #seconds
numberOfCars = SS.Simulation_Settings.numberOfCars
speedLimit = SS.Simulation_Settings.speedLimit
maxSpeed = SS.Simulation_Settings.maxSpeed # not used
minSpeed = SS.Simulation_Settings.minSpeed # not used


#set up statistic measurer
stats = EnergyReview.EnergyReview()



#set up csv writer
f = open('carData.csv', 'wb')
w = csv.writer(f)

def clearFile():
    file = open('carData.csv', 'wb')
    file.truncate()

def addLine(data):
    w.writerow(data)

#clear old data
clearFile()

#generate cars
cars = []


start_all = time.time()
for i in range(numberOfCars):
    # generate data
    vin = i

    #lane
    if SS.Simulation_Settings.experiment_num == 0:
        lane = (i % 4) + 1
    elif SS.Simulation_Settings.experiment_num == 1:
        lane = random.randint(1, 4)
    elif SS.Simulation_Settings.experiment_num == 2:
        lane = np.random.choice(4, 1, replace=False, p=[0.15, 0.35, 0.15, 0.35])[0] + 1
    elif SS.Simulation_Settings.experiment_num == 3:
        lane = 1 #(i % 4) + 1
        pastLane = not pastLane
    elif SS.Simulation_Settings.experiment_num == 4:
        lane = 1  # (i % 4) + 1
    #delay
    if SS.Simulation_Settings.experiment_num == 3:
       if(pastLane == True):
           delay = 200
       else:
           delay = 700
    else:
        delay = random.randrange(SS.Simulation_Settings.inter_spawn_min, SS.Simulation_Settings.inter_spawn_max, 1)



    speed = random.randrange(SS.Simulation_Settings.minSpeed, SS.Simulation_Settings.maxSpeed, 1) / 100.00
    accel = 0 # random.randrange(-10, 10, 1) / 100.0
    turn = 0#random.randint(0, 1)
    lenth = random.randrange(SS.Simulation_Settings.car_min_length, SS.Simulation_Settings.car_max_length, 1) / 10.0
    width = random.randrange(SS.Simulation_Settings.car_min_width, SS.Simulation_Settings.car_max_width, 1) / 10.0


    startTime = startTime + delay


    # create car
    test_car = CC.Car(vin, speed, accel, startTime, lane, turn, lenth, width)


    #statistical stats
    test_car.originalComlpetionTime =  mathHelp.expect(SS.Simulation_Settings.inter_side_length * 2,speed,accel)
    stats.originalUseTime += test_car.originalComlpetionTime

    #add car to car list
    cars.append(test_car)



#time keeping
total_intro = 0
total_outro = 0

#generate header VIN, Lane, length, width
header = []
for i in range(4):
    for C in cars:
        if i == 0:
            header.append(C.vin)
        elif i == 1:
            header.append(C.lane)
        elif i == 2:
            header.append(C.length)
        elif i == 3:
            header.append(C.width)
    addLine(header)
    header = []


#insert each car and get updated accel value
for C in cars:
    start = time.time()


    C.updateAccel01(manager.addReservation(C.generatereservation()))

    #stats for time it takes to insert
    total_intro =+ time.time() - start

#get positioning and check for needing outro
positionsX = []
positionsY = []
currentTime = 0
while (currentTime < timeLimit * 1000):

    for C in cars:
        #check if completed p2  (combine these two checks please)
        if C.expectedTime01 <= currentTime and C.set == 0:  #
            C.set = 1
            start = time.time()                                  # time stats
            C.updateAccel1(manager.bookOutro(C.generatereservationOUT()))

            total_outro = total_outro + ( time.time() - start)  # time stats
        #check for done with interection
        if C.checkForDone(currentTime) and C.set == 1:

            # time stats
            if(not C.hasContributed):
                C.realComlpetionTime = (currentTime - C.enterTime0)/1000.0   # find real time it takes to leave intersection
                stats.total_delay += C.realComlpetionTime - C.originalComlpetionTime
                stats.updatedUseTime += C.realComlpetionTime
                stats.total_energy += C.getEnergyUse()
                C.hasContributed = True

            #record blank spaces
            if (SS.Simulation_Settings.record_position):
                positionsX.append(0)
                positionsY.append(0)
           # else:
                # can only remove when not storing data, b\c header
             #   cars.remove(C)
        else:
            if (SS.Simulation_Settings.record_position):
                delta = C.distanceTravelledTime(currentTime)
                positionsX.append(delta[0])
                positionsY.append(delta[1])

    if (SS.Simulation_Settings.record_position):
        addLine(positionsX)
        addLine(positionsY)
        positionsX = []
        positionsY = []
    currentTime = currentTime + 1


manager.toString()
print ("Intro time used: {}".format(total_intro))
print ("Outro time used: {}".format(total_outro))
print ("Total time used per car: {}".format((time.time() - start_all)/SS.Simulation_Settings.numberOfCars))
print ("Total time used : {}".format((time.time() - start_all)))
print ("Total delay : {}".format(stats.total_delay))
print ("Total delay per car : {}".format(stats.total_delay / SS.Simulation_Settings.numberOfCars))
print ("Time Travel Index : {}".format(stats.TTI()))
print ("Total wasted energy: {}".format(stats.total_energy))
print ("Total wasted energy per car: {}".format(stats.total_energy / SS.Simulation_Settings.numberOfCars))