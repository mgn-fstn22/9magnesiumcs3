class BankAccount:
    def __init__(self, account_number, balance):
        self.__account_number = account_number  
        self.__balance = balance  

    def set_account_number(self, account_number):
        self.__account_number = account_number

    def set_balance(self, balance):
        if balance > 0:
            self.__balance = balance
        else:
            print("The balance must not be a negative number.")

    def get_account_number(self):
        return self.__account_number

    def get_balance(self):
        return self.__balance

a1 = BankAccount(12345, 1000)

print("Account 1")
print(f"Account Number: {a1.get_account_number()}")
print(f"Balance: {a1.get_balance()}\n")

print("Update balance to -100")
a1.set_balance(-100)
print(f"Account Number: {a1.get_account_number()}")
print(f"Balance: {a1.get_balance()}\n")