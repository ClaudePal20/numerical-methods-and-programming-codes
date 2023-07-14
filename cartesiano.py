try:
    x = int(input("Introduce el valor de 'x': "))
    y = int(input("Introduce el valor de 'y': "))
    if x == 0 and y == 0:
        print(f"El punto ({x},{y}) está en el origen")
    elif x == 0:
        print(f"El punto ({x},{y}) está en el eje de ordenadas")
    elif y == 0:
        print(f"El punto ({x},{y}) está en el eje de abscisas")
    elif x > 0 and y > 0:
        print(f"El punto ({x},{y}) está en el cuadrante 1")
    elif x < 0 and y > 0:
        print(f"El punto ({x},{y}) está en el cuadrante 2")
    elif x < 0 and y < 0:
        print(f"El punto ({x},{y}) está en el cuadrante 3")
    elif x > 0 and y < 0:
        print(f"El punto ({x},{y}) está en el cuadrante 4")
except ValueError:
    print("Oops! El valor debe ser tipo entero")