

class Dog:

    legs = 4

    def __init__(self,name, age):
        self.name = name
        self.age = age

    @classmethod
    def talk(cls):
        print("Woof Woof")

    @classmethod
    def factory(cls):
        return cls("Chanchito",4)


Dog.talk()
dog_1 = Dog("Toby",5)
dog_2 = Dog("Danger",3)
dog_3 = Dog.factory()
print(dog_3.name,dog_3.age)