# ABSTRACTION : it is basically hiding unnecessary implementation
# details and showing only what user needes, i.e. defining what must exist without mentioning how! 
# Eg: A car, for it the driver only wants to know how to start it
# he does not need to know the internal parts of the engine
# that is what abstraction is.
# py provides abstraction using ABC= Abstract Base Class module.

from abc import ABC, abstractmethod
class Payment(ABC):

    @abstractmethod
    def pay(self):
        pass

class UPI(Payment):
    def pay(self):
        print("UPI payment successful")

class Card(Payment):
    def pay(self):
        print("Card payment successful")

upi = UPI()
card = Card()

upi.pay()
card.pay()        

