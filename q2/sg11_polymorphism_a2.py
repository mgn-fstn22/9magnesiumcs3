#1. Answer the following questions:
    #a. What is duck typing, as explained in the video?
        #According to the video, duck typing  is one of the ways to achieve polymorphism in Python. 
        #It is a concept that allows any object (even if it isn't a child class of a parent class; in simpler terms, no inheritance is needed) to be used as long as it has the same method or attribute as the other objects.
    #b. What did the Car class need to have so it could work inside the same loop as Dog and Cat, even if it does not inherit from the Animal class?
        #The Car class needed to have the same method as the Dog and Cat class, which is the speak method. If the Car class retained its method of horn, then it would not work inside the same loop.
        #Moreover, the Car class also needed to have the same attribute as the other classes, which is the alive attribute. If the Car class did not have the alive attribute, then it would contrinute printing an AttributeError.

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

#3. How does the code in 2.2 demonstrate polymorphism?
    #This activity demonstrates polymorphism because it allows different objects to be used interchangeably through the same method call. This relies on what the object can do, rather than what class it inherits from.
    #When the function move is called, it can be called on any class as long as they have that function (many forms for one method). Each class responds on its own way, but uses the same method call.