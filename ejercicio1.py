import random

def generar_codigos():
    return [random.randint(1000, 9999) for _ in range(20)]

def generar_ventas(codigos):
    return list(map(lambda _: {
        'codigo_producto': random.choice(codigos),
        'cantidad_vendida': random.randint(1, 20),
        'precio_venta': round(random.uniform(10000, 100000), 2)
    }, range(50)))

def mostrar_datos(ventas):
    if not ventas:
        print("La lista está vacía")
        return
    print("==========================")
    print("CÓDIGO\tCANTIDAD\tPRECIO")
    print("==========================")
    list(map(lambda v: print(f"{v['codigo_producto']}\t{v['cantidad_vendida']}\t\t{v['precio_venta']:.2f}"), ventas))
    print("===================================================")

def totalizar_ventas(ventas):
    agrupadas = {}
    for venta in ventas:
        codigo = venta['codigo_producto']
        if codigo not in agrupadas:
            agrupadas[codigo] = []
        agrupadas[codigo].append(venta)

    return list(map(
        lambda kv: {
            'codigo_producto': kv[0],
            'cantidad_vendida': sum(v['cantidad_vendida'] for v in kv[1]),
            'precio_venta': round(sum(v['precio_venta'] for v in kv[1]) / len(kv[1]), 2)
        },
        agrupadas.items()
    ))

def main():
    codigos = generar_codigos()
    ventas_originales = generar_ventas(codigos)
    print("\nLISTA DE VENTAS ORIGINALES:")
    mostrar_datos(ventas_originales)
    ventas_totalizadas = totalizar_ventas(ventas_originales)
    print("\nLISTA DE VENTAS TOTALIZADAS:")
    mostrar_datos(ventas_totalizadas)

if __name__ == "__main__":
    main()
