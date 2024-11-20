

def sumar(x, y):
    return x + y

def restar(x, y):
    return x - y

def multiplicar(x, y):
    return x , y

def dividir(x, y):
    if y == 0:
        return "Error: No se puede dividir entre cero."
    return x / y
def potencia (x,y):
    return x ** y

def calculadora():
    print("Selecciona la operación:")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Potencia")

    while True:
        seleccion = input("Ingresa el número de la operación (1/2/3/4/5): ")

        if seleccion in ['1', '2', '3', '4','5']:
            num1 = float(input("Ingresa el primer número: "))
            num2 = float(input("Ingresa el segundo número: "))

            if seleccion == '1':
                print(f"{num1} + {num2} = {sumar(num1, num2)}")
            elif seleccion == '2':
                print(f"{num1} - {num2} = {restar(num1, num2)}")
            elif seleccion == '3':
                print(f"{num1}  {num2} = {multiplicar(num1, num2)}")
            elif seleccion == '4':
                print(f"{num1} / {num2} = {dividir(num1, num2)}")
            elif seleccion == '5':
                print(f"{num1} ** {num2} = {potencia(num1, num2)}")    
        else:
            print("Selección no válida. Por favor, elige una operación válida.")

        otra_vez = input("¿Quieres hacer otra operación? (sí/no): ")
        if otra_vez.lower() != 'sí':
            break

calculadora()
