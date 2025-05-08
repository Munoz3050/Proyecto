from abc import ABC, abstractmethod
from datetime import datetime

# Clase base Persona
class Persona(ABC):
    def __init__(self, nombre, ID):
        self.nombre = nombre
        self.ID = ID

    @abstractmethod
    def mostrar_info(self):
        pass

# Clase Empleado, hereda de Persona
class Empleado(Persona):
    def __init__(self, nombre, ID, turno):
        super().__init__(nombre, ID)
        self.turno = turno

    def mostrar_info(self):
        print(f"Empleado: {self.nombre}, ID: {self.ID}, Turno: {self.turno}")

    def registrar_ingreso(self):
        print("Ingreso registrado.")

    def registrar_salida(self):
        print("Salida registrada.")

    def generar_factura(self, cliente, monto):
        return Factura(1, cliente, monto)

# Clase Administrador, hereda de Persona
class Administrador(Persona):
    def __init__(self, nombre, ID):
        super().__init__(nombre, ID)

    def mostrar_info(self):
        print(f"Administrador: {self.nombre}, ID: {self.ID}")

    def registrar_gasto(self, tipo, monto):
        return Gasto(tipo, monto)

# Clase Cliente
class Cliente:
    def __init__(self, nombre, cedula, telefono):
        self.nombre = nombre
        self.cedula = cedula
        self.telefono = telefono

    def mostrar_info(self):
        print(f"Cliente: {self.nombre}, Cédula: {self.cedula}, Teléfono: {self.telefono}")

# Clase Factura
class Factura:
    def __init__(self, numero, cliente, costo):
        self.numero = numero
        self.cliente = cliente
        self.fecha = datetime.now().strftime("%Y-%m-%d")
        self.hora_entrada = "07:00"
        self.hora_salida = "17:00"
        self.costo = costo

    def mostrar_detalle(self):
        print(f"Factura No: {self.numero}, Cliente: {self.cliente.nombre}, Costo: {self.costo}")

    def calcular_costo(self):
        return self.costo

# Clase Gasto
class Gasto:
    def __init__(self, tipo, monto):
        self.tipo = tipo
        self.monto = monto
        self.fecha = datetime.now().strftime("%Y-%m-%d")

    def mostrar_detalle(self):
        print(f"Gasto tipo: {self.tipo}, monto: {self.monto}")

# Clase Moto
class Moto:
    def __init__(self, placa, marca, color, cilindraje):
        self.placa = placa
        self.marca = marca
        self.color = color
        self.cilindraje = cilindraje

    def estacionar(self):
        print("Moto estacionada.")

    def retirar(self):
        print("Moto retirada.")

# Clase Parqueadero
class Parqueadero:
    def __init__(self, nombre, direccion, capacidad):
        self.nombre = nombre
        self.direccion = direccion
        self.capacidad = capacidad

# Clase EspacioEstacionamiento
class EspacioEstacionamiento:
    def __init__(self, numero):
        self.numero = numero
        self.ocupado = False

    def asignar_moto(self, moto):
        self.ocupado = True
        print(f"Moto asignada al espacio {self.numero}")

    def liberar_espacio(self):
        self.ocupado = False
        print(f"Espacio {self.numero} liberado.")

    def espacio_mensualidad(self):
        print("Espacio reservado para mensualidad.")

# Clase Mensualidad
class Mensualidad:
    def __init__(self, cliente, moto, fecha_inicio, fecha_fin, costo):
        self.cliente = cliente
        self.moto = moto
        self.fecha_inicio = fecha_inicio
        self.fecha_fin = fecha_fin
        self.costo = costo

    def pagar_mensualidad(self):
        print("Mensualidad pagada.")

    def espacio_mensualidad(self):
        print("Espacio asignado por mensualidad.")

# Función principal para probar el funcionamiento
def main():
    cliente = Cliente("Juan Perez", "123456789", "3001234567")
    moto = Moto("ABC123", "Yamaha", "Rojo", 150)
    empleado = Empleado("Carlos", "EMP001", "Mañana")
    admin = Administrador("Laura", "ADM001")

    factura = empleado.generar_factura(cliente, 5000)
    factura.mostrar_detalle()

    gasto = admin.registrar_gasto("Luz", 20000)
    gasto.mostrar_detalle()

    espacio = EspacioEstacionamiento(1)
    espacio.asignar_moto(moto)
    espacio.liberar_espacio()

    mensualidad = Mensualidad(cliente, moto, "2024-05-01", "2024-05-31", 100000)
    mensualidad.pagar_mensualidad()

    parqueadero = Parqueadero("Mi Parqueadero", "Cra 1 #2-34", 50)

if __name__ == "__main__":
    main()
