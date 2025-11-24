import time
import math
import numpy as np

def es_primo_optimizado(n):
    if n<2:
        return False
    if n==2:
        return True
    if n%2==0:
        return False

    limite = int(math.sqrt(n))+1
    for i in range(3, limite, 2):
        if n%i==0:
            return False
    return True

def encontrar_primos_optimizado(rango_max):
    primos = []
    for num in range(2, rango_max):
        if es_primo_optimizado(num):
            primos.append(num)
    return primos

if __name__ == "__main__":
    inicio = time.time()
    primos = encontrar_primos_optimizado(100000)
    fin = time.time()
    tiempo_ejecucion = fin - inicio
    print(f"Números primos encontrados: {len(primos)} numeros primos")
    print(f"Tiempo de ejecución: {tiempo_ejecucion:.4f} segundos")
    print(f"Primeros 10 números primos: {primos[:10]}")
    print(f"Últimos 10 números primos: {primos[-10:]}")
