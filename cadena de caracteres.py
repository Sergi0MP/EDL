def quick_sort(names, ids, sueldos, deducciones, netos, inicio, fin):
    if inicio < fin:
        pivote_index = particion(names, ids, sueldos, deducciones, netos, inicio, fin)
        quick_sort(names, ids, sueldos, deducciones, netos, inicio, pivote_index - 1)
        quick_sort(names, ids, sueldos, deducciones, netos, pivote_index + 1, fin)

def particion(names, ids, sueldos, deducciones, netos, inicio, fin):
    pivote = names[fin]
    i = inicio - 1
    for j in range(inicio, fin):
        if names[j].lower() <= pivote.lower(): 
            i += 1
            intercambiar(names, ids, sueldos, deducciones, netos, i, j)
    intercambiar(names, ids, sueldos, deducciones, netos, i + 1, fin)
    return i + 1

def intercambiar(names, ids, sueldos, deducciones, netos, i, j):
    names[i], names[j] = names[j], names[i]
    ids[i], ids[j] = ids[j], ids[i]
    sueldos[i], sueldos[j] = sueldos[j], sueldos[i]
    deducciones[i], deducciones[j] = deducciones[j], deducciones[i]
    netos[i], netos[j] = netos[j], netos[i]

def busqueda_binaria_cadena(names, target):
    izquierda = 0
    derecha = len(names) - 1
    target = target.lower()

    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        nombre_actual = names[medio].lower()

        if nombre_actual == target:
            return medio
        elif nombre_actual < target:
            izquierda = medio + 1
        else:
            derecha = medio - 1
    return -1

def main():

    identificaciones = [1040, 1010, 1050, 1020, 1035]
    nombres          = ["Juanita", "Pachita", "Albita", "Pedrito", "Damaris"]
    sueldos_basicos  = [1_600_000, 2_000_000, 3_500_000, 1_600_000, 2_000_000]
    deducciones      = [100_000, 200_000, 500_000, 100_000, 200_000]
    netos            = [1_500_000, 1_800_000, 3_000_000, 1_500_000, 1_800_000]

    quick_sort(nombres, identificaciones, sueldos_basicos, deducciones, netos, 0, len(nombres) - 1)

    clave = input("Ingrese el nombre del empleado a buscar: ").strip()

    pos = busqueda_binaria_cadena(nombres, clave)

    
    if pos == -1:
        print("Empleado no encontrado")
    else:
        print("\n=== DATOS DEL EMPLEADO ===")
        print(f"Nombre         : {nombres[pos]}")
        print(f"Identificación : {identificaciones[pos]}")
        print(f"Sueldo Básico  : ${sueldos_basicos[pos]:,}")
        print(f"Deducciones    : ${deducciones[pos]:,}")
        print(f"Neto a Pagar   : ${netos[pos]:,}")

if __name__ == "__main__":
    main()