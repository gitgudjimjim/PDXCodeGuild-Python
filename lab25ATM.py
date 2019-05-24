#"""ATM with a class containing a balance property. A newly created account will default to a balance of 0. Implement the initializer, as well as the following methods:

#check_balance() returns the account balance
#deposit(amount) deposits the given amount in the account
#check_withdrawal(amount) returns true if the withdrawn amount won't put the account in the negative
#withdraw(amount) withdraws the amount from the account and returns it"""
class ATM:
    def __init__(self, ACC_NUM):
        self.ACC_NUM = ACC_NUM
        self.balance = balance

    def check_balance(self):
        #returns the account balance
        return self.balance

    def deposit(self, amount):
        #deposits the given amount into the account
        self.balance.append(amount)

    def check_withdrawal(self, amount):
        #returns true if withdrawn amount won't put account in the negative
        if amount < self.balance:
            return True
            print("you have the funds in your account for this withdrawal")
        else:
            return False
            print("you don't have the funds")

    def withdraw(self, amount):
        #withdraws the aount from the account and returns it
        remaining_bal -= amount
        remaining_bal = remaining_bal - amount
        if self.check_withdrawal(amount) is True:
            print("you have withdrawn {amount}")
            print("you have {remaining_bal} left")


atm = ATM(44)
atm.deposit(5)
print(atm.check_balance(500))
atm2 = ATM(45)
atm2.withdraw(5)
