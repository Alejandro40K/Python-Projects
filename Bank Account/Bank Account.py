"""
Proyecto: Cuenta bancaria
Nombre: Alejandro Orozco Romo
Fecha: 29/06/2025
Versión:0.1
"""

# LIBRERIAS

from os import system

# VARIABLES

confirmacion_accion = 0
finalizar_programa = False
cliente_actual = 0
menu = 0

# CLASES
class Persona:
    def __init__(self,nombre,apellido):
        self.nombre = nombre
        self.apellido = apellido

class Cliente(Persona):

    def __init__(self,nombre,apellido,numero_cuenta,balance):
        super().__init__(nombre, apellido)
        self.numero_cuenta = numero_cuenta
        self.balance = balance

    def __str__(self):
        return f" Cliente {self.nombre} {self.apellido}\n Balance de cuenta {self.numero_cuenta}: ${self.balance}\n "

    def depositar(self):
        monto_deposito = float(input("Ingresa una cantidad para depositar: "))
        self.balance += monto_deposito
        print(f"Se han depositado correctamente {monto_deposito}. Nuevo balance: {self.balance}")
        return self.balance

    def retirar(self):
        monto_retiro = float(input("Ingresa una cantidad para retirar: "))
        if  self.balance >= monto_retiro:
            self.balance -= monto_retiro
            print(f"Se han retirado correctamente {monto_retiro}. Nuevo balance: {self.balance}")
        else:
            print("Fondos insuficientes")
        return self.balance

# FUNCIONES
def crear_cliente():
    print("*"*50)
    print("ingrese los siguente datos")
    print("""
    - Nombre
    - Apellido
    - Numero de cuenta
    - Balance inicial (saldo)
    """)
    print("*"*50)
    nombre = input("Ingresa tu nombre: ")
    apellido = input("Ingresa tu apellido: ")
    numero_cuenta = input("Ingresa tu número de cuenta: ")
    balance = float(input("Ingresa tu blance actual: "))
    #cliente = Cliente(nombre,apellido,numero_cuenta,balance)
    return  Cliente(nombre,apellido,numero_cuenta,balance)

def inicio():

    #system('cls')
    #cliente_actual = crear_cliente()
    print("*" * 50)
    print("Bienvenido a su cuenta bancaria")
    print('*' * 50)
    print('\n')

    #print(cliente_actual)

    eleccion_menu = 'x'
    while not eleccion_menu.isnumeric() or int(eleccion_menu) not in range(1,5):
        print("Elige un opción:")
        print("""
        [1] - Crear cliente
        [2] - Depositar
        [3] - Retirar
        [4] - Salir 
        """)
        eleccion_menu = input()
    return int(eleccion_menu)


# CODIGO PRINCIPAL

while not finalizar_programa:
    menu = inicio()

    if menu == 1:
        cliente_actual = crear_cliente()
        print(cliente_actual)

    elif menu == 2:
        if cliente_actual:
            cliente_actual.depositar()
        else:
            print("Primero debes crear un cliente.")

    elif menu == 3:
        if cliente_actual:
            cliente_actual.retirar()
        else:
            print("Primero debes crear un cliente.")

    elif menu == 4:
        confirmacion_accion = int(input("¿Deseas salir? Presiona 1 para confirmar: "))
        if confirmacion_accion == 1:
            print("Ha salido de su cuenta")
            finalizar_programa = True
        else:
            pass
    else:
        print("Opcion no valida")





