class Bank_Account: # This will create the class
    def __init__(self, account_num, balance): #This will intialize the data fields
        self.__account_number = account_num #data field account number is being created
        self.__balance_acc = balance
    # This is where the methods are being created and initialized
    def set_account_number(self, account_num):
        self.__account_number = account_num
    def set_balance(self, balance):
        if balance > 0: # This will ensure that if the account balance is zero, then it won't accept it followed by a warning.
            self.__balance_acc = balance
        else:
            print("The balance you inputted CAN NOT be a negative value, please enter another balance.")
    def get_account_number(self): #returns the value
        return self.__account_number
    def get_balance(self): #returns the value
        return self.__balance_acc
    
# information is being inputted   
account_num = int(input("Please enter your account number: "))
balance = int(input("Please enter your account balance: "))
#using the inputted information, an object is created from the class
bank_account = Bank_Account(account_num, balance)

print("Account 1")
bank_account.set_account_number(account_num)
print(f"Account Number: {bank_account.get_account_number()}")#prints the account number
bank_account.set_balance(balance)
print(f"Balance: {bank_account.get_balance()}")#prints the balance

bank_account.set_balance(-400)#updates the balance 
print(f"Account Number: {bank_account.get_account_number()}")
print(f"Balance: {bank_account.get_balance()}")

