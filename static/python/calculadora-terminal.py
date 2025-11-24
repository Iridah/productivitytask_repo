# calculadora_terminal.py
# CUMPLIMIENTO: Sentencias Condicionales (if/elif/else) y Sentencias Iterativas

import math

## Funciones de Operaciones
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
        return "Error: Argumentos no válidos para el logaritmo (arg > 0, base > 0 y != 1)."
    return math.log(numero) / math.log(base) 

## Función Principal con Control de Flujo Explícito
def calculadora_menu():
    
    while True: # Sentencia Iterativa
        print("\n--- Calculadora Avanzada (Terminal - Clásica) ---")
        print("1. Suma")
        print("2. Resta")
        print("3. Multiplicación")
        print("4. División")
        print("5. Potenciación (a^b)")
        print("6. Raíz Cuadrada (√a)")
        print("7. Logaritmo en Base (log_b(a))")
        print("8. Salir")
        
        opcion = input("Seleccione una opción (1-8): ")
        
        if opcion == '8':
            print("¡Hasta pronto!")
            break
        
        # Bloque de Sentencias Condicionales
        elif opcion in ('1', '2', '3', '4', '5', '7'): # Operaciones BINARIAS
            try:
                num1 = float(input("Ingrese el primer número: "))
                num2 = float(input("Ingrese el segundo número: "))
                
                if opcion == '1':
                    resultado = sumar(num1, num2)
                elif opcion == '2':
                    resultado = restar(num1, num2)
                elif opcion == '3':
                    resultado = multiplicar(num1, num2)
                elif opcion == '4':
                    resultado = dividir(num1, num2)
                elif opcion == '5':
                    resultado = potenciar(num1, num2)
                elif opcion == '7':
                    resultado = logaritmo_base(num1, num2)
                
                    print(f"El resultado es: {resultado}")
                
            except ValueError:
                print("Error: Por favor, ingrese números válidos.")
        
        elif opcion == '6': # Operación UNARIA (Manejada aparte)
            try:
                num1 = float(input("Ingrese el número: "))
                resultado = raiz_cuadrada(num1)
                print(f"El resultado es: {resultado}")
            except ValueError:
                print("Error: Por favor, ingrese un número válido.")
                
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    calculadora_menu()