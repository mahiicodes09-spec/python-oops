#INHERITANCE IMPLEMENTATION!!!

class Student:
    college = "AKGEC"
    def __init__(self,name,rno):
        self.name=name
        self.rno=rno
    def display(self):
        print("Name:",self.name)
        print("Roll No:",self.rno)
        print("College:",self.college)


class EngStudent(Student):

    def __init__(self,name,rno,branch):
        super().__init__(name,rno)
        self.branch = branch

    def display(self):
        super().display()
        print("Branch:",self.branch)   


class  society(EngStudent):
    def __init__(self,name,rno,branch,society_name):
        super().__init__(name,rno,branch)
        self.society_name = society_name

    def display(self):
        super().display()
        print("Society:",self.society_name)


s1=society("Mahi",91,"CS","CSI")
s1.display()
print(isinstance(s1,society))
print(issubclass(society,Student))

#using property,GETTER,SETTER,DELETER!!

class Stu:
    def __init__(self,fn,ln,marks):
        self._fn= fn
        self._ln= ln
        self._marks= marks

    @property
    def fullname(self):
        return self._fn + " " + self._ln

    @fullname.setter
    def fullname(self,name):
        first, last = name.split(" ")
        self._fn = first
        self._ln = last

    @fullname.deleter
    def fullname(self):
        print("Deleting Name")
        self._fn = None
        self._ln = None  
        

    @property
    def marks(self):
        return self._marks

    @marks.setter
    def marks(self,value):
        if 0 <= value <= 100:
            self._marks=value
        else:
            print("Invalid Input")

                  
st1= Stu("Mahi","Gupta",89)
print(st1.fullname)
print(st1.marks)
st1.fullname= "Gracy Dixit"
del st1.fullname



#PRACTICE SET : PRODUCT!
class Product:
    def __init__(self,name,price,dis):
        self._name = name
        self._price = price
        self._dis = dis

    @property
    def name(self):
        return self._name

    @property 
    def price(self):
        return self._price

    @price.setter
    def price(self,value):
        if value>0:
            self._price = value
        else:
            print("Invalid Price")  

    @property
    def final_price(self):
        discount_amount = self._price * self._dis / 100
        return self._price - discount_amount       


p1 =Product("Noodles",50,2)
print(p1.name)
print(p1.price)
print("Discount Price:",p1.final_price)
