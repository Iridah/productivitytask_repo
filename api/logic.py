# calculadora_web.py
# CUMPLIMIENTO: Estructuras de Datos (Diccionario) y Funciones de primera clase

import math

## Funciones de Operaciones (Mismas que arriba)
def sumar(a, b): return a + b
def restar(a, b): return a - b
def multiplicar(a, b): return a * b
def dividir(a, b): 
    if b == 0:
        return "Error: La división por cero es indefinida en el ámbito de los números naturales, racionales y reales."
    return a / b
def potenciar(base, exponente): return base ** exponente
def raiz_cuadrada(numero): 
    if numero < 0:
        return "Error: Raíz cuadrada de número negativo."
    return math.sqrt(numero)
def logaritmo_base(numero, base):
    if numero <= 0 or base <= 0 or base == 1:
        return "Error: Argumentos no válidos para el logaritmo."
    return math.log(numero) / math.log(base) 

## Función Principal Refactorizada
def calculadora_menu():
    
    # ESTRUCTURA DE DATOS: Diccionario de Operaciones Binarias
    OPERACIONES_BINARIAS = {
        '1': sumar,
        '2': restar,
        '3': multiplicar,
        '4': dividir,
        '5': potenciar,
        '7': logaritmo_base
    }

    while True: # Sentencia Iterativa
        # --- MENÚ COMPLETO ---
        print("1. Suma")
        print("2. Resta")
        print("3. Multiplicación")
        print("4. División")
        print("5. Potenciación (a^b)")
        print("6. Raíz Cuadrada (√a)")
        print("7. Logaritmo en Base (log_b(a))")
        print("8. Salir")
        # -------------------------------
        
        opcion = input("Seleccione una opción (1-8): ")
        
        if opcion == '8':
            print("¡Hasta pronto!")
            break
        
        elif opcion == '6':
            # Opción UNARIA (Se maneja fuera del diccionario)
            try:
                num1 = float(input("Ingrese el número: "))
                resultado = raiz_cuadrada(num1)
                print(f"El resultado es: {resultado}")
            except ValueError:
                print("Error: Por favor, ingrese un número válido.")

        elif opcion in OPERACIONES_BINARIAS:
            # Opción BINARIA (Usa la estructura de datos)
            try:
                num1 = float(input("Ingrese el primer número: "))
                num2 = float(input("Ingrese el segundo número: "))
                
                # Ejecuta la función obtenida del diccionario
                funcion_a_llamar = OPERACIONES_BINARIAS[opcion]
                resultado = funcion_a_llamar(num1, num2)
                
                print(f"El resultado es: {resultado}")
                
            except ValueError:
                print("Error: Por favor, ingrese números válidos.")
                
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    calculadora_menu()