#Un triangulo por lo general puede tener sus 3 lados diferentes (escaleno), 2 iguales (isósceles) o todos iguales (equilátero).
#Hay que entender algunas reglas, ningún lado puede ser igual o mayor que la suma de las medidas de sus otros 2 lados. 
#Si por ejemplo en un triángulo, tenemos un lado que mide 5cm y otro 4cm, el último no puede medir 9cm o mas puesto que la suma de sus medidas 
# es el máximo que se puede utilizar para formar otro
#También podríamos decir, que es imposible que 2 lados formen un ángulo mayor o igual a 180° pero en esta ocasión solo lo basaremos con sus medidas.
try:
    a = float(input("Dame el valor del primer cateto: "))
    b = float(input("Dame el valor del segundo cateto: "))
    c = float(input("Dame el valor del tercer cateto: "))
    if (a<=0 or b<=0 or c<=0):
        print("Error, alguno de los lados son negativos o cero")
    elif (a+b<=c or a+c<=b or b+c<=a):
        print("Los lados introducidos no pueden formar un triángulo")
    else:
        if (a==b and a==c):
            print("Los lados introducidos forman un triángulo equilátero (todos sus lados son iguales)")
        elif (a==b or b==c or c==a):
            print("Los lados introducidos forman un triángulo isósceles (tiene dos lados iguales y uno diferente al resto)")
        else:
            print("Los lados introducidos forman un triángulo escaleno (todos sus lados son diferentes)")
except ValueError:
    print("El dato introducido no es un número")