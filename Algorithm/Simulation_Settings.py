class Simulation_Settings:
    timeLimit = 200 # seconds
    numberOfCars = 60

    speedLimit = 35
    maxSpeed = 3601  # upper-bound on spawn
    minSpeed = 3400 # lower-bound on spawn

    maxZ = 2500

    inter_side_length = 200  #half of intersection, enter -> exit
    inter_size = 20          #size of middle of intersection. Black squares on 2d visual


    inter_spawn_min = 600 # ms
    inter_spawn_max = 700

    #lengths and width are measured from center of car
    car_min_length = 20   # 0.1m
    car_max_length = 28
    car_min_width = 8  # 0.1m
    car_max_width = 14

    record_position = True



    experiment_num = 0

    """
    experiment 0
    -----------
    1-2-3-4
    
    experiment 1
    -----------
    random
    
     experiment 2
    -----------
     np.random.choice(4,1,replace=False, p=[0.1, 0.4, 0.1, 0.4])
    
    experiment 3  *BROKEN*
    -----------
    2x2
    
    experiment 4
    -----------
    same lane
    
    """