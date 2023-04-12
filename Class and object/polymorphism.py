# polymorphism means have many form. Polymorphism means the same function name with the diferent uses
class Bird:
    def intro(self):
        print("There are many types of birds")
    def flight(self):
        print("not all birds are fly")
class sparrow(Bird):
    def flight(self):
        print("Sparrows can fly")
class ostrich(Bird):
    def flight(self):
        print("osctrich cannot fly")
obj=Bird()
obj1=sparrow()
obj2=ostrich()
obj.intro()
obj.flight()
obj1.intro()
obj1.flight()
obj2.intro()
obj2.flight()
        