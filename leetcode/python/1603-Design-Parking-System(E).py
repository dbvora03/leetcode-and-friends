class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.data = {
            1: [big, 0],
            2: [medium, 0],
            3: [small, 0]
        }
        

    def addCar(self, carType: int) -> bool:
        
        spot = self.data[carType]
        
        if spot[1] == spot[0]:
            return False
        else:
            self.data[carType][1] += 1

            return True
        