age =int(input("enter the age:"))

if age>=18:
    print("you are eligible to vote")
else:
    print("you are not eligible to vote")

class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def myfunc(self):
        print("hello "+self.name)

p1=Person("john",36)
p1.myfunc()