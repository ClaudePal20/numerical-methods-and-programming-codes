bandera = True
contador = 0
acumulador = 0
while (bandera == True):
    try:
        numero = int(input("Introduce un número entero (sólo positivos/mayores a cero): "))
        while (numero<=0):
            numero = int(input("Introduciste un número no válido, introduce un número entero de nuevo (sólo positivos/mayores a cero): "))
    except ValueError:
        print("Introduciste un carácter diferente al pedido")
        continue
    acumulador = acumulador + numero
    contador+=1
    opc = input(f"¿Deseas capturar otro número?, introduce 's' o 'S' para continuar, introduce otra tecla para finalizar la captura: ")
    if opc !='s' and opc !='S':
        bandera = False
promedio = acumulador/contador
print(f"El promedio de los numeros es de {promedio:.2f}")