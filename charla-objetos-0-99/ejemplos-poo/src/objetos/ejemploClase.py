class Animal:

    __count = 0

    @classmethod
    def __add_one(cls):
        Animal.__count += 1

    @classmethod
    def count(cls):
        return Animal.__count

    def __init__(self, name):
        self.__name = name
        Animal.__add_one()

    def say_hello(self):
        print("Hi I'm {0}".format(self.__name))


if __name__ == "__main__":

    doggy = Animal("Doggy")
    michi = Animal("Michi")

    doggy.say_hello()
    michi.say_hello()

    print(f"Total: {Animal.count()}")

