def bubble_sort(fila):
    n = len(fila)
    for i in range(n):
        for j in range(0, n-i-1):
            if fila[j] > fila[j+1]:
                fila[j], fila[j+1] = fila[j+1], fila[j]

# Matriz bidimensional
matriz = [
    [9, 3, 1],
    [6, 5, 2],
    [7, 8, 4]
]

# Ordenar la segunda fila (índice 1)
print("Matriz original:")
for fila in matriz:
    print(fila)

bubble_sort(matriz[1])

print("\nMatriz después de ordenar la segunda fila:")
for fila in matriz:
    print(fila)
