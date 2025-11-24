# profiling_optimizado.py
import cProfile
import pstats
from codigo_optimizado import encontrar_primos_optimizado

def main():
    encontrar_primos_optimizado(100000)

if __name__ == "__main__":
    # Ejecutar profiling
    profiler = cProfile.Profile()
    profiler.enable()
    
    main()
    
    profiler.disable()
    
    # Guardar resultados en un archivo
    with open('profiling_optimizado.txt', 'w') as f:
        stats = pstats.Stats(profiler, stream=f)
        stats.sort_stats('cumulative')
        stats.print_stats()
    
    print("Profiling del código optimizado guardado en 'profiling_optimizado.txt'")