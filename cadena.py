def radix_sort_lsd_strings(strings):
    max_len = max(len(s) for s in strings)
    strings = [s.rjust(max_len) for s in strings]

    for digit in reversed(range(max_len)):
        buckets = [[] for _ in range(256)]
        for s in strings:
            index = ord(s[digit])
            buckets[index].append(s)
        strings = [item for sublist in buckets for item in sublist]

    return [s.strip() for s in strings]


# Entrada según el documento
entrada = ["radix", "prueba", "la", "sort"]

# Mostrar antes y después del ordenamiento
print("Antes de ordenar:", entrada)
salida = radix_sort_lsd_strings(entrada)
print("Después de ordenar:", salida)
