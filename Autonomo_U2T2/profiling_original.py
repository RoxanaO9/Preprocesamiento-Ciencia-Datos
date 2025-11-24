# profiling_original.py
import cProfile
import pstats
from codigo_original import encontrar_primos

def main():
    encontrar_primos(1, 100000)  # Dos parámetros

if __name__ == "__main__":
    # Ejecutar profiling
    profile = cProfile.Profile()
    profile.enable()
    
    main()
    
    profile.disable()
    
    # Guardar resultados en un archivo
    with open("profiling_original.txt", 'w') as f:
        stats = pstats.Stats(profile, stream=f)
        stats.sort_stats('cumulative')
        stats.print_stats()