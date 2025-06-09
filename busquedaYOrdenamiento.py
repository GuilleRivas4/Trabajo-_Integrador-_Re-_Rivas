import time
import random

# Generamos una lista aleatoria de 100 elementos
datos = random.sample(range(1, 1000), 100)
objetivo = datos[50]  # Elegimos un valor que sabemos que está

# -----------------------------
# ALGORITMOS DE BÚSQUEDA
# -----------------------------

# Búsqueda lineal: recorre todos los elementos uno por uno
def busqueda_lineal(lista, objetivo):
    for i in range(len(lista)):
        if lista[i] == objetivo:
            return i
    return -1

# Búsqueda binaria: requiere lista ordenada, divide y conquista
def busqueda_binaria(lista, objetivo):
    minimo = 0
    maximo = len(lista) - 1
    while minimo <= maximo:
        medio = (minimo + maximo) // 2
        if lista[medio] == objetivo:
            return medio
        elif lista[medio] < objetivo:
            minimo = medio + 1
        else:
            maximo = medio - 1
    return -1

# -----------------------------
# ALGORITMOS DE ORDENAMIENTO
# -----------------------------

# Bubble Sort: comparación de pares adyacentes
def bubble_sort(lista):
    copia = lista.copy()
    n = len(copia)
    for i in range(n):
        for j in range(0, n - i - 1):
            if copia[j] > copia[j + 1]:
                copia[j], copia[j + 1] = copia[j + 1], copia[j]
    return copia

# Quick Sort: elige una referencia y divide la lista
def quick_sort(lista):
    if len(lista) <= 1:
        return lista
    else:
        referencia = lista[0]
        menores = [x for x in lista[1:] if x <= referencia]
        mayores = [x for x in lista[1:] if x > referencia]
        return quick_sort(menores) + [referencia] + quick_sort(mayores)

# -----------------------------
# FUNCIÓN PARA MEDIR TIEMPO
# -----------------------------

def medir_tiempo(funcion, *args):
    inicio = time.time()
    resultado = funcion(*args)
    fin = time.time()
    duracion = fin - inicio
    return resultado, duracion

# -----------------------------
# PRUEBAS Y RESULTADOS
# -----------------------------

print("LISTA ORIGINAL (primeros 10 valores):", datos[:10])

# ORDENAMIENTO
orden_bubble, t_bubble = medir_tiempo(bubble_sort, datos)
orden_quick, t_quick = medir_tiempo(quick_sort, datos)

print(f"\nBubble Sort (Tiempo): {t_bubble:.6f} segundos")
print(f"Quick Sort (Tiempo): {t_quick:.6f} segundos")

# BÚSQUEDA
# Búsqueda lineal sobre lista desordenada
_, t_lineal = medir_tiempo(busqueda_lineal, datos, objetivo)

# Búsqueda binaria sobre lista ordenada
_, t_binaria = medir_tiempo(busqueda_binaria, orden_quick, objetivo)

print(f"\nBúsqueda Lineal (Tiempo): {t_lineal:.6f} segundos")
print(f"Búsqueda Binaria (Tiempo): {t_binaria:.6f} segundos")
