#poly: many morphism: forms
# it means that one thing can behave in different ways depending on the situation

#example:
class Dog:
    def speak(self):
        print("Bark")
class Cat:
    def speak(self):
        print("Meow")
class Robot:
    def speak(self):
        print("Hello")

def make_it_speak(obj):
    obj.speak()      

make_it_speak(Robot())
make_it_speak(Cat())
make_it_speak(Dog())



#PROBELM SET:1 - Polymorphism using Duck Typing
class Mahi:
    def bday(self):
        print("18th of April,2006")

class Shree:
    def bday(self):
        print("20th of September,2011")

class Rishabh:
    def bday(self):
        print("1st of October,2010")

def birth_date(date):
  date.bday()

birth_date(Mahi())
birth_date(Rishabh())
birth_date(Shree())

#PROBLEM SET:2 - PAYMENT METHODS

class UPIPayment():
    def pay(self):
        print("Paid using UPI")

class CardPayment():
    def pay(self):
        print("Paid using Card")        

class CashPayment():
    def pay(self):
        print("Paid using Cash")  

def process_payment(payment):
    payment.pay()

process_payment(UPIPayment())
process_payment(CardPayment())
process_payment(CashPayment())

#PROBLEM SET:3 - polymorphism + inheritance

class Employee:
    def work(self):
        print("Employee is Working")

class Developer(Employee):
    def work(self):
        print("Developer is writing Code")

class Designer(Employee):
    def work(self):
        print("Designer is creating Designs") 

def start_work(employee):
    employee.work()

start_work(Developer())
start_work(Designer())
