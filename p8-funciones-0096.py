print("Samuel Martinez NC 0096")
print("+-+-+-+-EJEMPLO 1+-+-+-+-")
def suma(a, b):
    return a + b
resultado = suma(4, 5)
print(resultado)  # Salida: 9
print("+-+-+-EJEMPLO 2+-+-+-")
# Ejemplo con return
def suma(a, b):
    resultado = a + b
    return resultado
resultado = suma(5, 3)
print(resultado)  # Salida: 8
print("+-+-+-EJEMPLO3+-+-+-")
def calcular_area_rectangulo(base, altura):
    area = base * altura  # Calcula el área
    return area           # Devuelve el resultado
# Llamada a la función
resultado = calcular_area_rectangulo(10, 5)
print(f"El área del rectángulo es: {resultado}")
print("+-+-+-EJEMPLO 4+-+-+-")
def Suma (num1 = 2, num2 = 3):
    return (num1 + num2)
#En este caso al llamarla sin especificar argumentos, serán asignados los que están por defecto.
resultado = Suma()
print(resultado)
#Y la salida será entonces: 5
print("+-+-+-EJEMPLO 5+-+-+-")
# Definición de la función con PARÁMETROS
def calcular_area(base, altura):
    return base * altura
# Llamada a la función con ARGUMENTOS
area = calcular_area(5, 3)  # Argumentos: base=5, altura=3
print(f"El área del rectángulo es: {area}")  # Salida: El área del rectángulo es: 15
print("Samuel Martinez NC 0096")