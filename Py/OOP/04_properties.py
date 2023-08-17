
class Dog:

    legs = 4

    def __init__(self,name, age):
        self.name = name
        self.age = age

    def talk(self):
        print("Woof Woof")
        print(f"{self.name} says Woof Woof")


dog_1 = Dog("Resortes",8)
print(dog_1.name)
print(dog_1.age)
dog_1.talk()
print(dog_1.legs)
