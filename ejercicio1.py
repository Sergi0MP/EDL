import random
from collections import namedtuple

Venta = namedtuple('Venta', ['codigo_producto', 'cantidad_vendida', 'precio_venta'])

class ListaVentas:
    def __init__(self): 
        self.ventas = []

    def agregar_venta(self, codigo_producto, cantidad_vendida, precio_venta):
        nueva_venta = Venta(codigo_producto, cantidad_vendida, precio_venta)
        self.ventas.append(nueva_venta)

def poblar_datos(lista):
    codigos_productos = [random.randint(1000, 9999) for _ in range(20)]

    for _ in range(50):
        codigo = random.choice(codigos_productos)
        cantidad = random.randint(1, 20)
        precio = round(random.uniform(10000, 100000), 2)
        lista.agregar_venta(codigo, cantidad, precio)

def mostrar_datos(lista):
    if not lista.ventas:
        print("La lista está vacía")
        return

    print("==========================")
    print("CÓDIGO\tCANTIDAD\tPRECIO")
    print("==========================")

    for venta in lista.ventas:
        print(f"{venta.codigo_producto}\t{venta.cantidad_vendida}\t\t{venta.precio_venta:.2f}")

    print("===================================================")

def suma_ventas(lista_entrada, lista_salida):
    if not lista_entrada.ventas:
        return

    productos_totalizados = {}

    for venta in lista_entrada.ventas:
        codigo = venta.codigo_producto
        if codigo not in productos_totalizados:
            productos_totalizados[codigo] = {
                'cantidad_total': 0,
                'suma_precio': 0.0,
                'cantidad_ventas': 0
            }
        productos_totalizados[codigo]['cantidad_total'] += venta.cantidad_vendida
        productos_totalizados[codigo]['suma_precio'] += venta.precio_venta
        productos_totalizados[codigo]['cantidad_ventas'] += 1

    for codigo, datos in productos_totalizados.items():
        promedio_precio = round(datos['suma_precio'] / datos['cantidad_ventas'], 2)
        lista_salida.agregar_venta(codigo, datos['cantidad_total'], promedio_precio)

def main():
    lista_entrada = ListaVentas()
    lista_salida = ListaVentas()

    poblar_datos(lista_entrada)
    print("\nLISTA DE VENTAS ORIGINALES:")
    mostrar_datos(lista_entrada)

    suma_ventas(lista_entrada, lista_salida)
    print("\nLISTA DE VENTAS TOTALIZADAS:")
    mostrar_datos(lista_salida)

if __name__ == "__main__":  
    main()