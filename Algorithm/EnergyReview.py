import Simulation_Settings as SS
class EnergyReview:

    def __init__(self):
        self.total_energy = 0.0  # E


        self.total_delay = 0.0


        # used for TTI calculation
        self.originalUseTime = 0
        self.updatedUseTime = 0



    def total_delay_per_car(self):
        return self.total_delay / SS.Simulation_Settings.numberOfCars

    def TTI(self):
        return self.updatedUseTime / self.originalUseTime
