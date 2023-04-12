# oops is programming paradigm that uses class and object , it aims is to implement real world entities like inheritence,polymorphism,encapsulation, etc .. it basically bind the data and the first 
# Main concepts are :
# Class
# objects
# Polymorphism
# Encapsulation
# Data Abstraction

#class: A class is collection of objects.
# class Class_Name:
# statement



#statement
#creating a empty class:
class Dog:
    pass

# object has state and behaviour it is like real life entity
# obj= Dog()
#__int__ method is similar like constructors . It is runs when object of the class is instantiated..

# creating class and object with class and static attributes
class Dog:
    attr="mammal"# class variable
    def __init__(self,name) :
        self.name=name
Rodger=Dog("alsasian")
Tommy=Dog("doberman")
ginny=Dog("german shepard")
print(Rodger.name)
print(Tommy.name)
print(ginny.name)
print(Rodger.__class__.attr)# accessing the class variable
print(Tommy.__class__.attr)


# creating class and  object with methods:
class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def myfunc(abc):
        print("hello my name is"+abc.name)
p1=Person("Sohini",56)# creating the object
p1.myfunc()



    






        


 


