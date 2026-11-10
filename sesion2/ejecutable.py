'''Metodos especiales de comparación'''
class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

    def __eq__(self, other):
        return self.precio == other.precio

    def __lt__(self, other):
        return self.precio < other.precio


p1 = Producto("Producto 1", 1000)
p2 = Producto("Producto 2", 2000)

print(p1 == p2)  # False
print(p1 < p2)   # True
print(p2<p1)

class Milista:
    def __init__(self):
        self.elementos = []

    def __getitem__(self, key):
        try:
            return self.elementos[key]
        except IndexError:
            return "No encontrado"

    def __setitem__(self, key, value):
        if key >= len(self.elementos):
            self.elementos.extend([None] * (key - len(self.elementos) + 1))
        self.elementos[key] = value
    
    def __delitem__(self, key):
        try:
            self.elementos[key] = None
        except IndexError:
            print("No encontrado")


lista = Milista()
lista[0] = "Python"
print(lista[0])  # Python
del lista[0]
print(lista[0])  # No encontrado


class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)

    def __repr__(self):
        return f"Vector({self.x}, {self.y})"


v1 = Vector(1, 2)
v2 = Vector(3, 4)
print(v1 + v2)  # Vector(4, 6)
print(v1 - v2)  # Vector(-2, -2)


#Cuenta bancaria
class CuentaBancaria:
    def __init__(self, titular, saldo=0):
        self.titular = titular
        self.saldo = saldo

    def __add__(self, other):
        nuevo_saldo = self.saldo + other.saldo
        return CuentaBancaria(f"{self.titular} y {other.titular}", nuevo_saldo)

    def __str__(self):
        return f"Cuenta de {self.titular} con saldo: {self.saldo}"

    '''def depositar(self, cantidad):
        if cantidad > 0:
            self.saldo += cantidad
            print(f"{self.titular} Tiene un saldo de: {self.saldo}")
        else:
            print("Cantidad a depositar debe ser positiva.")

    def retirar(self, cantidad):
        if 0 < cantidad <= self.saldo:
            self.saldo -= cantidad
            print(f"{self.titular} Tiene un saldo de: {self.saldo}")
        else:
            print("Cantidad a retirar inválida o insuficiente saldo.")  '''

cuenta1 = CuentaBancaria("Juan", 1000)
cuenta2 = CuentaBancaria("Maria", 500)

cuenta_combinada = cuenta1 + cuenta2
print(cuenta_combinada)  # Cuenta de Juan con saldo: 1500


#Ejercicio de control de inventario
class Inventario:
    def __init__(self):
        self.productos = {}

    def __getitem__(self, nombre):
        return self.productos.get(nombre, "Producto no encontrado")

    def __setitem__(self, nombre, cantidad):
        if cantidad < 0:
            print("La cantidad no puede ser negativa.")
        else:
            self.productos[nombre] = cantidad

    def __delitem__(self, nombre):
        if nombre in self.productos:
            del self.productos[nombre]
        else:
            print("Producto no encontrado")

    def __str__(self):
        return f"Inventario: {self.productos}"


inventario = Inventario()
inventario["manzanas"] = 50
inventario["naranjas"] = 30
print(inventario["manzanas"])  # 50
print(inventario["naranjas"])  # 30
del inventario["manzanas"]
print(inventario)  # Producto no encontrado