import pandas as pd
import numpy as np

def preprocesar_datos(df):
    """
    Función para preprocesamiento completo de datos
    """
    # Crear copia del DataFrame
    df_clean = df.copy()
    
    # Manejar valores nulos
    df_clean = df_clean.dropna()
    
    # Eliminar duplicados
    df_clean = df_clean.drop_duplicates()
    
    # Resetear índice
    df_clean = df_clean.reset_index(drop=True)
    
    return df_clean

# Ejemplo de uso
if __name__ == "__main__":
    # Datos de ejemplo
    data = {
        'columna1': [1, 2, None, 4, 4],
        'columna2': ['A', 'B', 'C', 'C', 'D']
    }
    df = pd.DataFrame(data)
    print("Datos originales:")
    print(df)
    
    df_procesado = preprocesar_datos(df)
    print("\nDatos preprocesados:")
    print(df_procesado)