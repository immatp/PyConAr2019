class Animal:

    def __init__(self, name):
        self.__name = name

    def say_hello(self):
        print("Hello")


class Dog(Animal):

    def say_hello(self):
        print("Guau guau!!!")


class Cat(Animal):

    def __init__(self,name):
        print("Cat constructor")
        super(Cat, self).__init__(name)

    def say_hello(self):
        print("Miau miau!!!")


if __name__ == "__main__":

    doggy = Dog("Toby")
    michi = Cat("Vigotes")

    doggy.say_hello()
    michi.say_hello()
