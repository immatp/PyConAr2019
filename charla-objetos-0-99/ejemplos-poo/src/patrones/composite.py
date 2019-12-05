class Hoja:

    def __init__(self, cantidad):
        self.__cantidad = cantidad

    def cantidad(self):
        return self.__cantidad


class Nodo:

    def __init__(self, componentes):
        self.__componentes = componentes

    def cantidad(self):
        cantidad = 0
        for componente in self.__componentes:
            cantidad += componente.cantidad()
        return cantidad


if __name__ == "__main__":

    rIzq = Hoja(3)
    rDer = Nodo([Hoja(1), Hoja(2)])
    rCentro = Nodo([Hoja(3), Nodo([Hoja(1), Hoja(2)])])
    raiz = Nodo([rIzq, rCentro, rDer])

    print("Peso total: {0}".format(str(raiz.cantidad())))



