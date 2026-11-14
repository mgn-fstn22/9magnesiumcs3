class Patient(): #creates a parent class named Patient
    def __init__(self, name:str, bill_amount: float): #creates a constructor method that initializes the name and bill amount of the patient
        self.__name = name #initializes the private attribute of patient __name
        self.__bill_amount = bill_amount #initializes the private attribute of patient __bill_amount

    @property #makes the function be treated as an attribute
    def get_name(self): #creates a function that prints the name of the patient
        return f"Patient Name: {self.__name}"  #prints the string "Patient Name:" along with the name of the patient

    @property #makes the function be treated as an attribute
    def get_bill_amount(self): #creates a function that prints the bill amount of the patient
        return f"Original Bill: {self.__bill_amount:,.2f}" #returns the private attribute of patient __bill_amount

    def set_bill_amount(self,bill_amount): #creates a function that sets the bill amount of patient
            self.__bill_amount = bill_amount #sets the bill_amount to a new value that is inputted

    def calculate_bill(self, bill_amount):
        return f"Final Bill: {self.__bill_amount:,.2f}" #prints the bill amount of the patient (without discount since this is just ordinary patient)

    @property #makes the function be treated as an attribute
    def display_patient_type(self): #creates a function that displays the type of patient
        return f"Patient Type: Regular Patient" #prints the string "Ordinary Patient"

class SeniorPatient(Patient): #creates a child class named SeniorPatient (inherits from parent class Patient)
    def __init__(self, name:str, bill_amount:float): #creates a constructor method that initializes the name and bill amount of the senior patient
        self.__name = name #initializes the private attribute of senior patient __name
        self.__bill_amount = bill_amount #initializes the private attribute of senior patient __bill

    @property #makes the function be treated as an attribute
    def get_name(self): #creates a function that prints the name of the senior patient
        return f"Patient Name: {self.__name}"

    @property #makes the function be treated as an attribute
    def get_bill_amount(self): #creates a function that prints the bill amount of the senior patient
        return f"Original Bill: {self.__bill_amount:,.2f}"

    def set_bill_amount(self,bill_amount): #creates a function that sets the bill amount of senior patient
        self.__bill_amount = bill_amount #sets the bill_amount to a new value that is inputted

    def calculate_bill(self, bill_amount): #creates a function that calculates the bill amount of senior patient
        discount = self.__bill_amount *0.2 #calculates the discount
        fbill = self.__bill_amount - discount #calculates the final bill after discount
        return f"Final Bill: {fbill:,.2f}" #prints the final bill after discount

    @property #makes the function be treated as an attribute
    def display_patient_type(self): #creates a function that displays the type of patient
        return f"Patient Type: Senior Patient" #prints the string "Senior Patient"


class PhilHealthPatient(Patient): #creates a child class named PhilHealthPatient (inherits from parent class Patient)
    def __init__(self, name:str, bill_amount:float): #creates a constructor method that initializes the name and bill amount of the senior patient
        self.__name = name #initializes the private attribute of patient __name
        self.__bill_amount = bill_amount #initializes the private attribute of patient __bill_amount

    @property #makes the function be treated as an attribute
    def get_name(self): #creates a function that prints the name of the senior patient
        return f"Patient Name: {self.__name}"
      
    @property #makes the function be treated as an attribute
    def get_bill_amount(self): #creates a function that prints the bill amount of the senior patient
       return f"Original Bill: {self.__bill_amount:,.2f}" #returns the private attribute of patient __bill_amount
      
    def set_bill_amount(self,bill_amount): #creates a function that sets the bill amount of senior patient
        self.__bill_amount = bill_amount #sets the bill_amount to a new value that is inputted
      
    def calculate_bill(self, bill_amount): #creates a function that calculates the bill amount of senior patient
        discount = self.__bill_amount *0.15 #calculates the discount
        fbill = self.__bill_amount - discount #calculates the final bill after discount
        return f"Final Bill: {fbill:,.2f}" #prints the final bill after discount
      
    @property #makes the function be treated as an attribute
    def display_patient_type(self): #creates a function that displays the type of patient
        return f"Patient Type: PhilHealth Member " #prints the string "PhilHealth Member "

patient1 = Patient("Juan Dela Cruz", 0) #create an object from class Patient
senior_patient1 = SeniorPatient("Maria Santos", 0) #create an object from class SeniorPatient
philhealth_patient1 = PhilHealthPatient("Pedro Reyes", 0) #create an object from class PhilHealthPatient

patient1.set_bill_amount(15000.00) #sets the bill amount of patient1
senior_patient1.set_bill_amount(15000.00) #sets the bill amount of senior_patient1
philhealth_patient1.set_bill_amount(15000.00) #sets the bill amount of philhealth_patient1


print("\nHospital Billing System") #prints a string
print("- - - - - - - - - - - - -") #prints a string

print(patient1.get_name) #prints the name of patient1
print(patient1.display_patient_type) #prints the type of patient1 (which is regular patient)
print(patient1.get_bill_amount) #prints the bill amount of patient1 (which is 15000.00)
print(patient1.calculate_bill(15000.00)) #calculates and prints the final bill of patient1

print("\n") #prints a newline
print(senior_patient1.get_name) #prints the name of senior_patient1
print(senior_patient1.display_patient_type) #prints the type of senior_patient1 (which is senior patient)
print(senior_patient1.get_bill_amount) #prints the bill amount of senior_patient1 (which is also 15000.00)
print(senior_patient1.calculate_bill(15000.00)) #calculates and prints the final bill of senior_patient1

print("\n")
print(philhealth_patient1.get_name) #prints the name of philhealth_patient1
print(philhealth_patient1.display_patient_type) #prints the type of philhealth_patient1 (which is PhilHealth member)
print(philhealth_patient1.get_bill_amount) #prints the bill amount of philhealth_patient1 (which is also 15000.00)
print(philhealth_patient1.calculate_bill(15000.00), "\n") #calculates and prints the final bill of philhealth_patient1 and prints a newline

