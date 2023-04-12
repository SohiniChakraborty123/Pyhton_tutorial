#Inheritence is the capability  of one class derived from another class.
#single Inheritence
# Multilevel Inheritence
# Multilple Inheritence
# Hierarchical Inheritence

#  Inheritence:
class A:
    x="parent class variable"
class B(A):
    pass
obj1=B()
class PC:
    def fun1(self):
        print("")
print(obj1.x)

# single Inheritence:

class Brands:
    brand_name1="Amazon"
    brand_name2="Ebay"
    brand_name3="OLX"
class Products(Brands):
    prod_1="Online Ecommerce Store"
    prod_2= "Online Store"
    prod_3="Online Buy Sell Store"
obj1=Products()
print(obj1.brand_name1+obj1.prod_1)
print(obj1.brand_name2+obj1.prod_2)
print(obj1.brand_name3+obj1.prod_3)


# Another Single inheritence example with method
class Dog:
    def bark():
        print("dog is barking")
class puppies(Dog):
    def speak():
        print("puppies are speaking ")
obj=puppies()# object creatblee with reference varia
Dog.bark()# call the function use the class name
puppies.speak()

# MORE EXAMPLE :
class Parent_class():
    def __init__(self,name,id):
        self.name=name
        self.id=id
    def Employee_detail(self):
        return self.name,self.id
    def Employee_check(self):
        if self.id> 50000:
           return print("valid employee")
        else:
            return print("invalid employee")
class derived_class(Parent_class):
    def End(self):
        print("end of program")
employee1=Parent_class("sohini",900060)
print(employee1.Employee_detail(),employee1.Employee_check())
employee2=derived_class("Arka",895670)
print(employee2.Employee_detail,employee2.Employee_check)


# If a single child class is created from multiple parent class that concept is known as multiple inheritence
class mother():
    mothername1=""
    def mother1(self):
        print(self.mothername1)
class father():
    fathername1=""
    def father1(self):
        print(self.fathername1)

class son(mother,father):
    def parents(self):
        print("The father name is",self.fathername1)
        print("The mother name is",self.mothername1)
s1=son()
s1.fathername1="Ujan"
s1.mothername1="Hiya"
s1.parents()

# multilevel inheritence is when a child class is derived from parent class and that this child class will be the parent class of another child class. This concept is known as multilevel inheritence

class Manager():
    def final_review(self):
        print("Final review")
class Reviewer(Manager):
    def review(self):
        print("Reviewing")
class writer(Reviewer):
    def writer(self):
        print("Write the codes")
o=writer()
o.final_review()
o.review()
o.writer()

# hirerchical inheritence:
# when there is one parent class and from this there are more than child classes are derived
class abc:
    def func_1(self):
        print("Ist Function is working here")
class efg(abc):
    def func_2(self):
        print("2nd Function is working")
class xyz(abc):
    def func_3(self):
        print("3rd Function is working")
# we need to create the object of both child class with different reference variable
ref1=efg()
ref1.func_2()
ref2=xyz()
ref2.func_3()
ref1.func_1()