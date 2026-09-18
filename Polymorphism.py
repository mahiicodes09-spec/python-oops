#poly: many morphism: forms
# it means that one thing can behave in different ways depending on the situation

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

#make_it_speak(Robot())
#make_it_speak(Cat())
#make_it_speak(Dog())



#PRACTICE SET!
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

birth_date(Shree())

#different classes have same method hence it is an example of polymorphism