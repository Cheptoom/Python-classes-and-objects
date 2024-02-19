class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age
name=input("Enter your name:")
age=input("Enter your age:")
p1 = Person(name,age)
print(p1.name)
print(p1.age)

#Object methods
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name)

p1 = Person("Marion", 20)
print(p1.myfunc())

#Inheritance
class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

class Student(Person):
  pass

x = Student("Marion", "Ch")
x.printname()

#Super()function,will make the child class inherit all the methods and properties from its parent:
class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname
  def printname(self):
    print(self.firstname, self.lastname)
class Student(Person):
  def __init__(self, fname, lname):
    super().__init__(fname, lname)

x = Student("Marion", "Ch")
x.printname()

#Add methods
class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

class Student(Person):
  def __init__(self, fname, lname, year):
    super().__init__(fname, lname)
    self.graduationyear = year

  def welcome(self):
    print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)

x = Student("Marion", "Ch", 2024)
x.welcome()

