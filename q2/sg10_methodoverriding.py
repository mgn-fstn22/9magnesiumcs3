class Animal(): #create parent class Animal
    def __init__ (self, name:str): #
        self.__name = name #

    @property #the @property makes the function be treated as an attribute
    def eat(self): #functions that returns 
        return f"{self.__name} is eating."

    @property #the @property makes the function be treated as an attribute
    def make_sound(self):
        return f"{self.__name} is making a sound."

class Lion(Animal):
    def __init__(self, name:str):
        self.__name = name

    @property #the @property makes the function be treated as an attribute
    def eat(self):
        return f"{self.__name} eats fresh meat"

    @property #the @property makes the function be treated as an attribute
    def make_sound(self):
        return f"{self.__name} roars loudly!"

class Monkey(Animal):
    def __init__(self, name:str):
        self.__name = name

    @property #the @property makes the function be treated as an attribute
    def eat(self):
        return f"{self.__name} eats bananas"

    @property #the @property makes the function be treated as an attribute
    def make_sound(self):
        return (f"{self.__name} chatters!")

class Elephant(Animal):
    def __init__(self, name:str):
        self.__name = name

    @property #the @property makes the function be treated as an attribute
    def eat(self):
        return(f"{self.__name} eats grass and fruits")

    @property #the @property makes the function be treated as an attribute
    def make_sound(self):
        return(f"{self.__name} trumpets!")

lion = Lion("Simba")
elephant = Elephant("Dumbo")
monkey = Monkey("George")

print(lion.make_sound) #prints the make_sound method of the Lion class
print(lion.eat) #prints the eat method of the Lion class
print("- - - - -") #prints a string

print(elephant.make_sound)
print(elephant.eat)
print("- - - - -") #prints a string

print(monkey.make_sound) #prints the make_sound method of the Monkey class, which is "chatters!"
print(monkey.eat)
print("- - - - -") #prints a string