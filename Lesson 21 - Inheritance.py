class Animal:
    def __init__(self,sound,legs=4):
        self.sound = sound
        self.legs = 4
    def make_sound(self):
        print(self.sound)

class Cat(Animal):
    def __init__(self):
        super().__init__("meow")


class Dog(Animal):
    def __init__(self):
        super().__init__("woof")

    def make_sound(self):
        print(self.sound,self.sound)

cat = Cat()
cat.make_sound()
print(cat.legs)

dog = Dog()
dog.make_sound()
print(dog.legs)