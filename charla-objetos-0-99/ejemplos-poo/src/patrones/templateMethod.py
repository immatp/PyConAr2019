from time import sleep


class Corredor:

    def __init__(self, nombre):
        self.__nombre = nombre

    def movete(self):
        self.caminar()
        self.descanzar()

    def caminar(self):
        print("2 pasos")

    def descanzar(self):
        raise NotImplementedError


class Perro(Corredor):

    def caminar(self):
        super(Perro, self).caminar()
        print("2 pasos")

    def descanzar(self):
        print("Espero 2s")
        sleep(2)


class Humano(Corredor):

    def movete(self):
        self.descanzar()
        super(Humano, self).movete()

    def descanzar(self):
        print("Espero 1s")
        sleep(1)


if __name__ == "__main__":

    perro = Perro("Manchita")
    humano = Humano("Pepe")

    perro.movete()
    humano.movete()
