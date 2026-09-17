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