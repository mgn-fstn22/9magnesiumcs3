class Drone(): #creates a drone class separate from the other classes
    def move(self): #creates a move method for the drone class
        print("The drone flies in the sky.") #prints a string

class Car(): #creates a car class separate from the other classes
    def move(self): #creates a move method for the car class
        print("The car drives on the road.") #prints a string

class Boat(): #creates a boat class separate from the other classes
    def move(self): #creates a move method for the boat class
        print("The boat sails on the water.") #prints a string

def start_trip(vehicle): #creates a function with a paremeter vehicle that can accept any object with a move method
    vehicle.move() #calls the move method of the vehicle object

vehicles = [Drone(), Car(), Boat()] #creates a list of objects which has the move method

for vehicle in vehicles: #creates a for loop that goes through each object in the vehicles list
    start_trip(vehicle) #calls the start_trip function with the objects in the list as the parameter