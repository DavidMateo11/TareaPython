"""
Descripción: Programa para gestionar un registro de usuario y
realizar una conversión de metros a pies.
"""


def ejecutar_programa():
    # --- Identificadores en snake_case y Tipos de Datos ---
    nombre_usuario = "Alex"  # String
    edad_usuario = 22  # Integer
    estatura_metros = 1.75  # Float
    es_estudiante = True  # Boolean

    # --- Lógica: Conversión de unidades ---
    # Multiplicamos los metros por el factor de conversión
    estatura_pies = estatura_metros * 3.28084

    # --- Mostrar Resultados en Consola ---
    print("--- Datos del Registro ---")
    print(f"Usuario: {nombre_usuario}")
    print(f"Edad: {edad_usuario} años")
    print(f"Estatura: {estatura_metros} m")

    print("\n--- Resultado del Cálculo ---")
    print(f"La estatura en pies es: {estatura_pies:.2f} ft")

    # Condicional simple para verificar mayoría de edad
    if edad_usuario >= 18:
        print(f"Estado: {nombre_usuario} es mayor de edad.")
    else:
        print(f"Estado: {nombre_usuario} es menor de edad.")


# Inicio del programa
if __name__ == "__main__":
    ejecutar_programa()