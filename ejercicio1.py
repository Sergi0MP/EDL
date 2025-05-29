import random

class Producto:
    def __init__(self, codigo, cantidad, precio):
        self.codigo = codigo
        self.cantidad = cantidad
        self.precio = precio

def poblar_datos(lista):
    codigos = [1020, 1023, 1025, 1020, 1030, 1023, 1025, 1050, 1025, 1023]
    cantidades = [8, 8, 7, 10, 5, 2, 5, 1, 8, 1]
    precios = [18, 18, 17, 18, 10, 20, 15, 2, 15, 20]
    for i in range(len(codigos)):
        lista.append(Producto(codigos[i], cantidades[i], precios[i]))

def mostrar_datos(lista):
    for prod in lista:
        print(f"Código: {prod.codigo}, Cantidad: {prod.cantidad}, Precio: {prod.precio}")

def quicksort(lista, inicio, fin):
    if inicio < fin:
        pivote = particion(lista, inicio, fin)
        quicksort(lista, inicio, pivote - 1)
        quicksort(lista, pivote + 1, fin)

def particion(lista, inicio, fin):
    pivote = lista[fin].codigo
    i = inicio - 1
    for j in range(inicio, fin):
        if lista[j].codigo <= pivote:
            i += 1
            lista[i], lista[j] = lista[j], lista[i]
    lista[i + 1], lista[fin] = lista[fin], lista[i + 1]
    return i + 1

def suma_ventas(lista_entrada, lista_salida):
    i = 0
    while i < len(lista_entrada):
        codigo_actual = lista_entrada[i].codigo
        total_cantidad = 0
        total_precio = 0
        cantidad_productos = 0

        while i < len(lista_entrada) and lista_entrada[i].codigo == codigo_actual:
            total_cantidad += lista_entrada[i].cantidad
            total_precio += lista_entrada[i].precio
            cantidad_productos += 1
            i += 1

        promedio_precio = round(total_precio / cantidad_productos, 2)
        lista_salida.append(Producto(codigo_actual, total_cantidad, promedio_precio))

def main():
    lista_entrada = []
    lista_salida = []
    poblar_datos(lista_entrada)
    print("Ventas originales:")
    mostrar_datos(lista_entrada)

    quicksort(lista_entrada, 0, len(lista_entrada) - 1)
    suma_ventas(lista_entrada, lista_salida)

    print("\nVentas totalizadas:")
    mostrar_datos(lista_salida)

main()
