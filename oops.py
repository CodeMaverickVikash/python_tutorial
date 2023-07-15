# classes - Template - virashat
# object - instance of the class

# classes concept uses - Dry = Do not repeat yourself


class Parent:
    def __init__(self, a, b, c):
        self.a = a # This is public data member
        self._b = b # Protected data member
        self.__c = c # Private data member

    # Private member function
    def __sum(self):
        return self.a + self._b

    def multi(self):
        return self.__c + self.__sum()

class Child(Parent):
    def __init__(self, a, b, c):
        super().__init__(a, b, c)

    def Accessing(self):
        # print(Parent.multi(self))
        
        print(self.multi()) # Both are same
        print(self.a)
        

v = Child(2, 3, 4)
# print(v.multi())

v.Accessing()


# class and object
class Calculator:
    def __init__(self):
        print("welcome")
    def fact(self, name):
        self.name = name
        print("hello", self.name)

o = Calculator()
o.fact("vikash")

# self and __init__() (constructor)
class Employee:
    # class attribute
    no_of_leaves = 8

    def __init__(self):
        print("Hello vikash")

    def printdetails(self):
        return f"{self.name} salary is {self.salary}"

harry = Employee()
rohan = Employee()

# instance variable
harry.name = "vikash"
harry.salary = 345

rohan.name ="mayank"
rohan.salary = 543

print(rohan.printdetails())

# give the arguments of class is called constructor
