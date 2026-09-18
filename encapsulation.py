#encapsulation is how the class controls its internal data.
#GETTER : USED TO READ
#SETTER : USED TO CHANGE

class BankAcc():
    def __init__(self,balance):
        self._balance = 0
        self.balance = balance

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self,value):
        if value >= 0:
            self._balance = value
        else:
            print("Invalid Value")

b1=BankAcc(8000)
print(b1.balance)

b2=BankAcc(-500)
print(b2.balance)           
