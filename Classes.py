class Dog:
    energy = "very energetic"

    def speak(self):
        print("woof")

bilbo_waggins = Dog()
print(bilbo_waggins.energy)
bilbo_waggins.speak()

tilly = Dog()
print("Tilly the dog is", tilly.energy)
tilly.speak()

# Moving on to the further class exercises... 

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

John = Student("John", "21")
Jane = Student("Jane", "22")

print(getattr(John, "age"))

class Instrument:
    def __init__(self, name, sound):
        self.name = name
        self.sound = sound

Trumpet = Instrument("Trumpet", "brassy")

print(getattr(Trumpet, "sound"))


class Athlete:
    def __init__(self, name):
        self.name = name


class Footballer(Athlete):
    def __init__(self, name, team):
        super(Footballer, self).__init__(name)
        self.team = team

Player_1 = Footballer("Jason", "Leeds United")

print(hasattr(Player_1, "age"))