class Presidente:

    instancia = None

    @staticmethod
    def get_instancia():

        if Presidente.instancia:
            return Presidente.instancia
        else:
            Presidente.instancia = Presidente()
            return Presidente.instancia


if __name__ == "__main__":

    pres1 = Presidente().get_instancia()
    pres2 = Presidente().get_instancia()
    pres3 = Presidente().get_instancia()

    print(pres1)
    print(pres2)
    print(pres3)
