# Object Oriented Programming:
# 1) A class is a blueprint created using 'class' keyword and this class can be
#    instantiated i.e the action of creating different instances (objects).
# 2) Object oriented programming allow us to create objects that have some methods and attributes/properties.


class BigObject:  # Class
    # code
    pass


# So we are creating a new object by instantiating the above class.
obj1 = BigObject()  # Instantiate
obj2 = BigObject()  # Instantiate
obj3 = BigObject()  # Instantiate

# We can see the type of the obj1 datatype as we use to see for different datatypes:
print(type(obj1))
print(type(5))
print(type(0.3))
print(type(True))
print(type("Hii"))
print(type([]))
print(type({}))
print(type(()))
print(type(set()))
print(type(None))


# _____________________________________________________________________________________
class PlayerCharacter:
    def __init__(self, name, age):  # Constructor (Method)
        self.name = name  # Class Attribute/Property
        self.age = age

    def run(self):  # Method
        return "Run Run!"


player1 = PlayerCharacter("Ammar", 21)
player2 = PlayerCharacter("Elon Musk", 44)

print(player1.name)
print(player2.age)
print(player1.run())


# We can also create attributes for the object:
player1.height = "6ft"
print(player1.height)

# If we want help or want to know about a particular class/object/function/datatype etc., then we
# can use the help() function:
# help(player1)
# help(PlayerCharacter)
# help(list)
# help(int)

# _____________________________________________________________________________________


class User:
    # Class Object Atrribute (This does not change across different instances/objects or we can say that Class Object Attributes are static.).
    membership = True

    def __init__(self, name, age):
        if self.membership == True:  # or we can also use 'User.membership'
            self.name = name  # Class Attribute (They are dynamic or we can say that they are specific to each class object.)
            self.age = age

    def log_in(self):
        return f"Hello {self.name}, You have logged in successfully!"


user1 = User("Anil", 26)
print(user1.log_in())

# _____________________________________________________________________________________


# We can also give some default parameters inside the constructor &
# We can also give some kind of condition inside the constructor so that it will not create objects if
# the condition is not satisfied:
# Ex:
class Sample:
    def __init__(self, name="anonymous", age=0):
        if age > 18:
            self.name = name
            self.age = age


object1 = Sample()
# If we do not give the arguments then it will by default take 'age = 0' and there is a condition inside
# the constructor that if age is below 18 then the object will not be created.

object2 = Sample("Tom", 13)
# This will also not create the object as age is below 18

object3 = Sample(age=20)  # This object will be created
print(f"User's name is {object3.name} and age is {object3.age}")


# _____________________________________________________________________________________

# @classmethod and @staticmethod
# (Both of these decorators are mostly not used.)


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod  # A class method to create a Person object by birth year.
    def fromBirthYear(cls, name, year):
        return cls(name, 2023 - year)

    @staticmethod  # A static method to check if a Person is adult or not.
    def isAdult(age):
        return age > 18


person1 = Person("Raj", 21)
person2 = Person.fromBirthYear("Rahul", 1998)

print(person1.age)
print(person2.age)

# print the result
print(Person.isAdult(22))

# _____________________________________________________________________________________

"""
Sample code:

class NameOfClass:
    class_object_attribute = 'value'

    def __init__(self, param1, param2):
        self.param1 = param1
        self.param2 = param2

    def method(self):
        code
    
    @classmethod
    def cls_method(cls, param1, param2):
        code
    
    @staticmethod
    def stc_method(param1, param2):
        code

obj = className()

"""
# _____________________________________________________________________________________

# There are 4 pillars of OOP:
# 1) Encapsulation: Encapsulation is a mechanism of wrapping the data (variables/attributes/properties) and code acting on the data (methods) together as a single unit.
# 2) Abstraction: Abstraction is defined as a process of hiding unnecessary information from the user.
# 3) Inheritance: Inheritance allows us to define a class(child class) that inherits all the methods and properties from another class(parent class).
# 4) Polymorphism:

"""
Very Important Note:
1) Python, unlike some other programming languages like Java or C++, does not have explicit keywords for
   declaring 'public' or 'private' variables or methods. Instead, Python relies on a naming convention to
   indicate the visibility of variables and methods.

2) For private attributes and methods, developers typically prefix the name with a single underscore (_) or also 
   double underscore (__).

3) However, it's essential to note that this is just a convention, and it doesn't make the attributes or methods
 completely private. Python does not enforce strict access control, so you can still access them if needed.

4) If you want to indicate that an attribute or method should be considered private and not accessed directly,
   it's a convention for developers to use a single underscore prefix (Ex: _private_variable).
"""


# Example:
class Person:
    def __init__(self, name, mobile_no):
        self._name = name  # This is considered as private variable/attribute
        self._mobile_no = mobile_no

    def _private_method(self):  # This is considered as private method
        print("This method should not be  accessed!")


# _____________________________________________________________________________________


# Inheritance:
class User:
    def sign_in(self):
        print("Logged in!")


class Wizard(User):
    def __init__(self, name, power):
        self.name = name
        self.power = power

    def attack(self):
        print(f"Attacking with the power of {self.power}")


class Archer(User):
    def __init__(self, name, num_of_arrows):
        self.name = name
        self.num_of_arrows = num_of_arrows

    def attack(self):
        print(f"Attacking with arrows. Number of arrows left - {self.num_of_arrows}")


wizard1 = Wizard("Merlin", 50)
archer1 = Archer("Robin", 120)
wizard1.sign_in()
archer1.sign_in()
wizard1.attack()
archer1.attack()

# We can check if a given instance is of a particular class or not by using the isinstance() function:
print(isinstance(wizard1, Wizard))
print(isinstance(wizard1, User))
print(isinstance(wizard1, object))
# object class is the main base class which acts as a parent class in python. Every other class inherits object class.
# _____________________________________________________________________________________

# Polymorphism
# As we can see that we have implemented attack() method multiple times, but based on which object calls the
# method, it performs differently.


class User:
    def sign_in(self):
        print("Logged in!")

    def attack(self):
        print("Do nothing!")


class Wizard(User):
    def __init__(self, name, power):
        self.name = name
        self.power = power

    def attack(self):
        print(f"Attacking with the power of {self.power}")


class Archer(User):
    def __init__(self, name, num_of_arrows):
        self.name = name
        self.num_of_arrows = num_of_arrows

    def attack(self):
        print(f"Attacking with arrows. Number of arrows left - {self.num_of_arrows}")


wizard1 = Wizard("Merlin", 60)
archer1 = Archer("Robin", 85)


# So we can see that based on the object that we pass in the parameter of the below function,
# it gives different outputs.
def perform_attack(char):
    return char.attack()


perform_attack(wizard1)
perform_attack(archer1)

# _____________________________________________________________________________________


# We can also pass a method of parent class inside the method of a child class OR
# we can say that we can also pass a method inside another method
class User:
    def sign_in(self):
        print("Logged in!")

    def attack(self):
        print("Do nothing!")


class Wizard(User):
    def __init__(self, name, power):
        self.name = name
        self.power = power

    def attack(self):
        User.attack(self)  # This is parent class method
        print(f"Attacking with the power of {self.power}")


wizard1 = Wizard("Merlin", 60)
wizard1.attack()

# Similarly we can also pass a method inside another method of the same class
# _____________________________________________________________________________________

# super() function:
# The super function is used to access methods of the immediate parent class and access their attributes.

# As we know that the child class objects can access the methods of parent class, but how the objects can access the attributes of
# parent class, so this is done by calling the __init__ method of parent class inside the __init__ method of child class.


class User:
    def __init__(self, email):
        self.email = email

    def sign_in(self):
        print("Logged in!")


class Wizard(User):
    def __init__(self, name, power, email):
        # User.__init__(self, email) or
        super().__init__(email)
        # While using super() there is no need to pass 'self' inside parameter
        self.name = name
        self.power = power

    def attack(self):
        User.attack(self)  # This is parent class method
        print(f"Attacking with the power of {self.power}")


wizard1 = Wizard("Merlin", 60, "merlin24@gmail.com")
print(wizard1.email)
# So using super() method we are able to access the parent class attribute.


# We can check that the object have access to which functionalities/methods.
# To do this we use dir(). It returns all the functions available for an instance.
print(dir(wizard1))

# _____________________________________________________________________________________


# Excercise:
# We are extending the functionalities of built-in List class into our SuperList class
class SuperList(list):
    def __len__(self):  # We can modify the dunder methods/magic methods
        return 1000


superlist1 = SuperList()

print(len(superlist1))
superlist1.append(5)
print(superlist1[0])
# So as we can see that our SuperList class object 'superlist1' can also access the List class methods


# _____________________________________________________________________________________
# Multiple Inheritance:
class User:
    def sign_in(self):
        print("Logged In!")


class Wizard(User):
    def __init__(self, name, power):
        self.name = name
        self.power = power

    def attack(self):
        print(f"Attacking with the power of {self.power}!")


class Archer(User):
    def __init__(self, name, arrows):
        self.name = name
        self.arrows = arrows

    def arrow_attack(self):
        print(f"Attacking with {self.arrows} arrows!")


class Hybrid(Wizard, Archer):
    def __init__(self, name, power, arrows):
        Wizard.__init__(self, name, power)
        Archer.__init__(self, name, arrows)


h1 = Hybrid("Pikachu", 60, 75)
h1.sign_in()
h1.attack()
h1.arrow_attack()
# _____________________________________________________________________________________


# How python determines the order of the execution of methods or attributes in cases like inheritance?
# (It uses MRO i.e Method Resolution Order)
# We can check the order using the 'mro' method or __mro__ dunder method:
class A:
    num = 10


class B(A):
    pass


class C(A):
    num = 1


class D(B, C):
    pass


print(D.num)
print(D.mro())
print(D.__mro__)
