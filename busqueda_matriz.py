def buscar_valor(matriz, valor_buscado):
    for i, fila in enumerate(matriz):
        for j, valor in enumerate(fila):
            if valor == valor_buscado:
                return (i, j)
    return None

# Matriz bidimensional
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

valor_buscado = 5
resultado = buscar_valor(matriz, valor_buscado)

if resultado:
    print(f"Valor encontrado en la posición: {resultado}")
else:
    print("Valor no encontrado.")

