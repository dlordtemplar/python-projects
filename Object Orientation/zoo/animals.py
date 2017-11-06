#############################
# UTILITIES                 #
#############################

'''
e.g. a function that reads in the images
'''


#############################
# ANIMALS                   #
#############################

'''
The classes representing animals.
First, define the class hierarchy.
Then think of what the classes have in common,
this functionality goes in the superclass.
Then think of what is special about the subclass,
this goes into the subclass.

Hints: Some methods can be applied to all animals
(e.g., visit(), eat()), some only apply to a particular
animal (e.g., swim()).

Which attributes do the objects have?
--> Design your __init__ methods accordingly.
'''


class Animal():
    def __init__(self, name, path):
        self.name = name
        self.path = path

    def visit(self):
        print("Visiting\t" + self.name)
        with open(self.path) as printFile:
            for line in printFile:
                print(line.rstrip())
        print("NAME:", self.name)
        print("INFORMATION:")
        print("Animal <can eat(), sleep()>")

    def eat(self):
        print("I am a " + self.name + " and I am ~~~~ EATING!! ~~~~")

    def sleep(self):
        print("I am a " + self.name + " and - yawn... ~~~~ ZZZzzzz ~~~~")

    def __str__(self):
        return self.name


class Mammal(Animal):
    def visit(self):
        Animal.visit(self)
        print("\t|\n\t---- Mammal")


class Rodent(Mammal):
    def visit(self):
        Mammal.visit(self)
        print("\t\t|\n\t\t---- Rodent <can gnaw()>")

    def gnaw(self):
        print("I am a " + self.name + " and I am *** GNAWING ****")


class Bird(Animal):
    def visit(self):
        Animal.visit(self)
        print("\t|\n\t---- Bird <can fly()>")

    def fly(self):
        print("I am a " + self.name + " and I am ~~~~ FLYING!! ~~~~")


class LandBird(Bird):
    def visit(self):
        Bird.visit(self)
        print("\t\t|\n\t\t---- Land Bird")


class WaterBird(Bird):
    def visit(self):
        Bird.visit(self)
        print("\t\t|\n\t\t---- Water Bird <can swim()>")

    def swim(self):
        print("I am a " + self.name + " and I am ~~~~ SWIMMING!! ~~~~")


class Fish(Animal):
    def visit(self):
        Animal.visit(self)
        print("\t|\n\t---- Fish <can swim()>")

    def swim(self):
        print("I am a " + self.name + " and I am ~~~~ SWIMMING!! ~~~~")
