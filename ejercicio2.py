import random

MAX_EMPLEADOS = 10
SUELDO_BASICO = 0
DEDUCCIONES = 1
NETO_PAGAR = 2


class Nomina:
    def __init__(self):  
        self.identificaciones = [0] * MAX_EMPLEADOS
        self.nombres = [""] * MAX_EMPLEADOS
        self.datos_nomina = [[0.0 for _ in range(3)] for _ in range(MAX_EMPLEADOS)]
        self.cantidad_empleados = 0

    def poblar_datos(self):
        nombres_disponibles = [
            "Juan", "Ana", "Carlos", "María", "Pedro", "Laura", "Damaris",
            "Albita", "Pedrito", "Juanita", "Pachita", "Ricardo"
        ]

        self.cantidad_empleados = MAX_EMPLEADOS
        for i in range(self.cantidad_empleados):
            self.identificaciones[i] = random.randint(1000, 9999)
            self.nombres[i] = random.choice(nombres_disponibles)
            self.datos_nomina[i][SUELDO_BASICO] = random.randint(1_000_000, 4_000_000)

            porcentaje_deduccion = 0.1 + random.random() * 0.1
            self.datos_nomina[i][DEDUCCIONES] = round(
                self.datos_nomina[i][SUELDO_BASICO] * porcentaje_deduccion
            )

            self.datos_nomina[i][NETO_PAGAR] = (
                self.datos_nomina[i][SUELDO_BASICO] - self.datos_nomina[i][DEDUCCIONES]
            )

    def ordenar_por_identificacion(self):
        for i in range(self.cantidad_empleados - 1):
            min_index = i
            for j in range(i + 1, self.cantidad_empleados):
                if self.identificaciones[j] < self.identificaciones[min_index]:
                    min_index = j
            if min_index != i:
                self.intercambiar(i, min_index)

    def buscar_empleado(self, identificacion):
        inicio = 0
        fin = self.cantidad_empleados - 1
        while inicio <= fin:
            medio = inicio + (fin - inicio) // 2
            if self.identificaciones[medio] == identificacion:
                return medio
            elif self.identificaciones[medio] < identificacion:
                inicio = medio + 1
            else:
                fin = medio - 1
        return -1

    def ordenar_por_nombre(self):
        self.quick_sort(0, self.cantidad_empleados - 1)

    def quick_sort(self, inicio, fin):
        if inicio < fin:
            pivote_index = self.particion(inicio, fin)
            self.quick_sort(inicio, pivote_index - 1)
            self.quick_sort(pivote_index + 1, fin)

    def particion(self, inicio, fin):
        pivote = self.nombres[fin]
        i = inicio - 1
        for j in range(inicio, fin):
            if self.nombres[j] <= pivote:
                i += 1
                self.intercambiar(i, j)
        self.intercambiar(i + 1, fin)
        return i + 1

    def intercambiar(self, i, j):
        self.identificaciones[i], self.identificaciones[j] = self.identificaciones[j], self.identificaciones[i]
        self.nombres[i], self.nombres[j] = self.nombres[j], self.nombres[i]
        self.datos_nomina[i], self.datos_nomina[j] = self.datos_nomina[j], self.datos_nomina[i]

    def mostrar_datos(self):
        print("\n======= NÓMINA DE EMPLEADOS =======")
        encabezado = f"{'ID':^10}│{'NOMBRE':^20}│{'SUELDO BÁSICO':^20}│{'DEDUCCIONES':^15}│{'NETO A PAGAR':^18}"
        print(encabezado)
        print("─" * len(encabezado))
        for i in range(self.cantidad_empleados):
            print(f"{self.identificaciones[i]:^10}│"
                  f"{self.nombres[i]:<20}│"
                  f"${self.datos_nomina[i][SUELDO_BASICO]:>19,.2f}│"
                  f"${self.datos_nomina[i][DEDUCCIONES]:>14,.2f}│"
                  f"${self.datos_nomina[i][NETO_PAGAR]:>17,.2f}")
        print("─" * len(encabezado))

    def mostrar_empleado(self, pos):
        if 0 <= pos < self.cantidad_empleados:
            print("\n========= DATOS DEL EMPLEADO =========")
            print(f"{'Identificación':<20}: {self.identificaciones[pos]}")
            print(f"{'Nombre':<20}: {self.nombres[pos]}")
            print(f"{'Sueldo Básico':<20}: ${self.datos_nomina[pos][SUELDO_BASICO]:,.2f}")
            print(f"{'Deducciones':<20}: ${self.datos_nomina[pos][DEDUCCIONES]:,.2f}")
            print(f"{'Neto a Pagar':<20}: ${self.datos_nomina[pos][NETO_PAGAR]:,.2f}")
            print("======================================")
        else:
            print("Empleado no encontrado")


if __name__ == "__main__":  
    nomina = Nomina()

    nomina.poblar_datos()

    print("DATOS INICIALES:")
    nomina.mostrar_datos()

    nomina.ordenar_por_identificacion()
    print("\nDATOS ORDENADOS POR IDENTIFICACIÓN:")
    nomina.mostrar_datos()

    id_buscar = nomina.identificaciones[3]
    print(f"\nBuscando empleado con ID: {id_buscar}")
    pos = nomina.buscar_empleado(id_buscar)
    nomina.mostrar_empleado(pos)

    id_no_existe = 9999
    print(f"\nBuscando empleado con ID: {id_no_existe}")
    pos = nomina.buscar_empleado(id_no_existe)
    if pos == -1:
        print("Empleado no encontrado")
    else:
        nomina.mostrar_empleado(pos)

    nomina.ordenar_por_nombre()
    print("\nDATOS ORDENADOS POR NOMBRE:")
    nomina.mostrar_datos()