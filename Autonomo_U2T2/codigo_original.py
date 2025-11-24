import time

def es_primo(num):
    if num < 2:
        return False # Los numeros menores que 2 no son primos
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False # si existe un divisor, no es primo
    return True # Si no se encontraron divisores, es primo

def encontrar_primos(inicio, fin):
    primos = [] # Almacena los numeros primos encontrados
    for num in range(inicio, fin + 1):
        if es_primo(num):
            primos.append(num) # Agrega a la lista si es primo
    return primos # imprime la lista de nuemeros primos encontrados

if __name__ == "__main__":
    inicio = time.time() # Marca el tiempo de inicio
    primos =  encontrar_primos(1, 100000)
    fin = time.time()  # Marca el tiempo de fin
    tiempo_total = fin - inicio # Calcula el tiempo total de ejecución
    print(f"Números primos encontrados: {len(primos)}")
    print(f"Tiempo total de ejecución: {tiempo_total:.3f} segundos")