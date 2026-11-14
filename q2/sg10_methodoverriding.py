class Animal(): #create parent class Animal
    def __init__ (self, name:str): #creates a constructor method that initializes the name of the animal
        self.__name = name #initializes the private attribute of animal __name

    @property #the @property makes the function be treated as an attribute
    def eat(self): #functions that returns a string that describes what the animal is eating
        return f"{self.__name} is eating." #prints the name of the animal and its action, which is eating.

    @property #the @property makes the function be treated as an attribute
    def make_sound(self): #create a functions that returns a string describing what sound the animal is making
        return f"{self.__name} is making a sound." #prints the name of the animal and its action, which is making a sound.

class Lion(Animal): #create child class Lion(inherits from Animal class)
    def __init__(self, name:str): #creates the constructor method that initializes the name of the lion
        self.__name = name #initializes the private attribute of lion __name

    @property #the @property makes the function be treated as an attribute
    def eat(self): #creates a functions that returns a string describing what the lion is eating
        return f"{self.__name} eats fresh meat" #prints the name of the lion and its action, which is eating fresh meat.

    @property #the @property makes the function be treated as an attribute
    def make_sound(self): #creates a functions that returns a string describing what sound the lion is making
        return f"{self.__name} roars loudly!" #prints the name of the lion and its action, which is roaring loudly!

class Monkey(Animal): #create child class Monkey(inherits from Animal class)
    def __init__(self, name:str):  #creates the constructor method that initializes the name of the Monkey
        self.__name = name #initializes the private attribute of monkey __name

    @property #the @property makes the function be treated as an attribute
    def eat(self): #creates the function eat
        return f"{self.__name} eats bananas" #prints a string describing what the Monkey is eating, which is bananas.

    @property #the @property makes the function be treated as an attribute
    def make_sound(self): #creates the function make_sound
        return (f"{self.__name} chatters!") #prints a string describing what sound the Monkey is making, which is chatters.

class Elephant(Animal): #create child class Elephant(inherits from Animal class)
    def __init__(self, name:str): #creates the constructor method that initializes the name of the Elephant 
        self.__name = name #initializes the private attribute of elephant __name

    @property #the @property makes the function be treated as an attribute
    def eat(self): #creates the function eat
        return(f"{self.__name} eats grass and fruits") #prints a string describing what the Elephant is eating, which is grass and fruits)

    @property #the @property makes the function be treated as an attribute
    def make_sound(self): #creates the function make_sound
        return(f"{self.__name} trumpets!") #prints a string describing what sound the Elephant is making, which is trumpets.

lion = Lion("Simba") #creates an object of the Lion class
elephant = Elephant("Dumbo") #creates an object of the Elephant class
monkey = Monkey("George") #creates an object of the Monkey class

print(lion.make_sound) #prints the make_sound method of the Lion class, which is "roars loudly!"
print(lion.eat) #prints the eat method of the Lion class
print("- - - - -") #prints a string

print(elephant.make_sound) #prints the make_sound method of the Elephant class, which is "trumpets!"
print(elephant.eat) #prints the eat method of the Elephant class, which is "eats grass and fruits"
print("- - - - -") #prints a string

print(monkey.make_sound) #prints the make_sound method of the Monkey class, which is "chatters!"
print(monkey.eat) #prints the eat method of the Monkey class, which is "eats bananas"
print("- - - - -") #prints a string