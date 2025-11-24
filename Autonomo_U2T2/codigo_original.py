import time

def es_primo(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def encontrar_primos_en_rango(inicio, fin):
    primos = []
    for num in range(inicio, fin + 1):
        if es_primo(num):
            primos.append(num)
    return primos

if __name__ == "__main__":
    inicio = time.time()
    primos = encontrar_primos_en_rango(1, 100000)
    fin = time.time()
    tiempo_total = fin - inicio
    print(f"Números primos encontrados: {len(primos)}")
    print(f"Tiempo total de ejecución: {tiempo_total:.3f} segundos")