from multiprocessing.sharedctypes import Value
try:
    precio = float(input("Introduce el precio del producto a comprar: "))
except ValueError:
    precio = 0
if (precio>0):
    try:
        opcion = int(input("¿Qué tipo de producto quieres comprar? 1. Carnicería 2. Bebidas: "))
        if opcion == 1:
            if (precio<=100):
                desc = 0.15
            else:
                desc = 0.25
        elif opcion == 2:
            if (precio<=100):
                desc = 0.20
            else:
                desc = 0.30
        else:
            print("Opción no valida")
        precio = precio - precio*desc
        print(f"Tu producto tiene un precio final de: {precio:.2f} pesos con un descuento del {desc*100:.2f}%")
    except ValueError:
        print("Error, el tipo de artículo no es válido")
else:
    print('Error, precio no válido o dato inválido')