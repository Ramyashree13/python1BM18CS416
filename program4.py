import string
class student:
    def __init__(self):
        name = None
        age = None
        marks = None

    def setter(self,name,age,marks):
        self.name=name
        self.age=age
        self.marks=marks

    def getter(self):
        print(self.name,self.age,self.marks)

    def validate_marks(self):
        if(self.marks>=0 and self.marks<=100):
            return True
        return False

    def validate_age(self):
        if(self.age>20):
            return True
        return False

    def check_qualification(self):
        if(self.marks>=65):
            print("student %s qualifies for exam" %self.name)
        else:
            print("student %s not eligible for exam" %self.name)

        
#name=input("enter the name")
#age=int(input("enter the age"))
#marks=int(input("enter the marks"))
x=student()
x.setter("ramya",21,66)
x.getter()
y=x.validate_marks()
print(y)
z=x.validate_age()
print(z)
x.check_qualification()
