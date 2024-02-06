# HACIENDO 5/02/2024
# Hecho 6/02/2024

from os import system


class Personas:

    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido


class Cliente(Personas):

    def __init__(self, nombre, apellido, num_cuenta, balance):

        super().__init__(nombre, apellido)
        self.num_cuenta = num_cuenta
        self.balance = balance

    # Mostrar mensaje
    def __str__(self):
        return f'El cliente {self.nombre} {self.apellido} con numero de cuenta: {self.num_cuenta}' \
               f' tiene un balance de: {self.balance}'

    # Depositar dinero
    def depocitar(self, cantidad):
        self.balance = self.balance + cantidad

    # Retirar dinero
    def retirar(self, cantidad):

        if cantidad > self.balance:
            print('No puedes reritar, fondos insuficientes...')
        else:
            self.balance = self.balance - cantidad


def crear_cliente():
    nombres = input('¿Cual es tu nombre?: ')
    apellidos = input('¿Cual es tu apellido?: ')
    num_cuentas = input('¿Cual es tu numero de cuenta?: ')
    balances = int(input('¿Cual es tu balance hasta ahora?: '))

    return nombres, apellidos, num_cuentas, balances


def inicio(cliente):

    # Creación del menú para correr el programa

    op = 0

    print('¿Qué deseas hacer?: ')
    print('1. Ver balance')
    print('2. Depositar dinero')
    print('3. Retirar dinero')
    print('4. Salir')

    while op not in range(1, 5):
        print('')
        op = int(input('Escoge una opción: '))
        print('')
        system('cls')

    while op != 4:

        if op == 1:
            print(cliente)
        elif op == 2:
            depocito = int(input('Cuanto vas a depocitar?: '))
            cliente.depocitar(depocito)
        elif op == 3:
            depocito = int(input('Cuanto vas a retirar?: '))
            cliente.retirar(depocito)

        print('')
        print('¿Qué deseas hacer?: ')
        print('1. Ver balance')
        print('2. Depositar dinero')
        print('3. Retirar dinero')
        print('4. Salir')
        print('')
        op = int(input('Escoge una opción: '))
        system('cls')

    print('Saliendo...')


# Función
nombre, apellido, num_cuenta, balance = crear_cliente()
# Objeto
cliente = Cliente(nombre, apellido, num_cuenta, balance)

inicio(cliente)
