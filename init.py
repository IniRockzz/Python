class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 =Person("Jimmy", "23")
print(p1.name)
print(p1.age)

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def __str__(self):
    return f"{self.name},({self.age})"

p1 = Person("John", 36)

print(p1)


class Person:
  def __init__(MYSELF, fname, lname):
    MYSELF.firstname = fname
    MYSELF.lastname = lname

  def printname(abc):
    print(abc.firstname, abc.lastname)

x = Person("John", "Doe")
x.printname()