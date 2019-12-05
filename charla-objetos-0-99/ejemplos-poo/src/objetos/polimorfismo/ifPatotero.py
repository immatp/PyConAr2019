class CuentaBancaria:

    def __init__(self, numero_de_cuenta, titular_cuenta, saldo, tipo_cuenta):
        self.__numeroDeCuenta = numero_de_cuenta
        self.__titularCuenta = titular_cuenta
        self.__saldo = saldo
        self.__tipoCuenta = tipo_cuenta

    def saldo(self):
        return self.__saldo

    def depositar(self, cantidad):
        self.__saldo += cantidad

    def retirar(self, cantidad):

        if self.__tipoCuenta == "cuentaSueldo":
            self.__saldo = self.__saldo - cantidad - 5

        elif self.__tipoCuenta == "cuentaCorriente":
            self.__saldo = self.__saldo - cantidad - 20


if __name__ == "__main__":

    cuenta_jose = CuentaBancaria(3410, "Jose Sanchez", 100, "cuentaSueldo")
    cuenta_juan = CuentaBancaria(3411, "Juan Perez", 100, "cuentaCorriente")

    cuenta_jose.retirar(10)
    cuenta_juan.retirar(10)

    print("Saldo Jose: {0}".format(cuenta_jose.saldo()))
    print("Saldo JUan: {0}".format(cuenta_juan.saldo()))
