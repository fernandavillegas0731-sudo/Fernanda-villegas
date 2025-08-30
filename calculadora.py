# 📌 Calculadora en Python
# Autor: Fernanda Calderón Villegas
# Descripción: Mini programa que permite realizar operaciones básicas.

def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        return "Error: No se puede dividir entre 0"
    return a / b

def calculadora():
    print("=== CALCULADORA BÁSICA ===")
    print("Opciones: sumar, restar, multiplicar, dividir, salir")

    while True:
        opcion = input("\n¿Qué operación deseas realizar?: ").lower()

        if opcion == "salir":
            print("👋 Gracias por usar la calculadora, hasta pronto!")
            break

        if opcion in ["sumar", "restar", "multiplicar", "dividir"]:
            try:
                num1 = float(input("Ingresa el primer número: "))
                num2 = float(input("Ingresa el segundo número: "))
            except ValueError:
                print("❌ Error: Debes ingresar valores numéricos.")
                continue

            if opcion == "sumar":
                print(f"✅ Resultado: {sumar(num1, num2)}")
            elif opcion == "restar":
                print(f"✅ Resultado: {restar(num1, num2)}")
            elif opcion == "multiplicar":
                print(f"✅ Resultado: {multiplicar(num1, num2)}")
            elif opcion == "dividir":
                print(f"✅ Resultado: {dividir(num1, num2)}")
        else:
            print("❌ Opción no válida. Intenta de nuevo.")

if __name__ == "__main__":
    calculadora()
