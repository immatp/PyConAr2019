class CuentaBancaria:

    def __init__(self, numero_cuenta, titular_cuenta, saldo):
        self.__numero_cuenta = numero_cuenta
        self.__titularCuenta = titular_cuenta
        self._saldo = saldo

    def saldo(self):
        return self._saldo

    def depositar(self, cantidad):
        self._saldo += cantidad

    def retirar(self,cantidad):
        self._saldo = self._saldo - cantidad


class CuentaSueldo(CuentaBancaria):

    def retirar(self, cantidad):
        self._saldo = self._saldo - cantidad - 5


class CuentaCorriente(CuentaBancaria):

    def retirar(self, cantidad):
        self._saldo = self._saldo - cantidad - 20


if __name__ == "__main__":

    cuenta_jose = CuentaSueldo(3410, "Jose Sanchez", 100)
    cuenta_juan = CuentaCorriente(3411, "Juan Perez", 100)

    cuenta_jose.retirar(10)
    cuenta_juan.retirar(10)

    print("Saldo Jose: {0}".format(cuenta_jose.saldo()))
    print("Saldo Juan: {0}".format(cuenta_juan.saldo()))
