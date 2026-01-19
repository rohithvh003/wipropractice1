# 1.Uses a parameterized constructor to initialize account_number and balance
# Implements methods deposit(amount) and withdraw(amount)
# Uses a destructor to display a message when the object is deleted
# Handle invalid withdrawal using proper checks


# solution:

class BankAccount:
    def __init__(self,Acc_no,balance):
        self.Acc_no = Acc_no
        self.balance = balance

    def deposit(self,amount):
        if amount > 0:

            self.balance += amount
            print(amount,"amount is deposited")
            print("current balance",self.balance)
        else:
            print("invalid amount")
    def withdraw(self,amount):

        if amount <=0 :
            print("invalid withdrawn amount")
        elif amount > self.balance:
            print("insufficient balance")
        else:
            self.balance -= amount
            print(amount,"amount is withdraw")
            print("current balance",self.balance)


    def __del__(self):
        print("object is deleted")

b1 = BankAccount(7854,1000)
b1.deposit(int(input()))
b1.withdraw(int(input()))



