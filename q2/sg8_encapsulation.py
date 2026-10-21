class BankAccount: #create class BankAccount
    def __init__(self, account_number, balance): #creating class attributes
        self.__account_number = account_number  #Private attribute for account number
        self.__balance = balance  #Private attribute for balance

    def account_number(self, account_number): #Function that sets the account number 
        self.__account_number = account_number #Sets the account number to the value inputted

    def balance(self, balance): #Function that sets the balance
        if balance > 0: #Checks if the balance is greater than 0
            self.__balance = balance #Assign the new balance to the private attribute
        else: #Condition if the balance is not greater than 0 or is 0.
            print("The balance must not be a negative number.") #Print error message when balance is not greater than 0

    def account_number(self):#Function that accesses and returns the account number
        return self.__account_number #return/print the account number

    def balance(self): #Function that accesses and returns the balance
        return self.__balance #return/print the balance

a1 = BankAccount(12345, 1000) #Creates an instance of the BankAccount class

print("Account 1") #prints a string
print(f"Account Number: {a1.get_account_number()}") #prints the account number of the bank account using the get_account_number
print(f"Balance: {a1.get_balance()}\n") #prints the balance of the bank account using the get_balance method

print("Update balance to -100") #prints a string
a1.set_balance(-100) #sets the balance of the bank account to -100 using the set_balance method
print(f"Account Number: {a1.get_account_number()}") #prints the account number of the bank account using the get_account_number
print(f"Balance: {a1.get_balance()}\n") #prints the balance of the bank account using the get_balance method
