calif1 = int(input("Dame la primera calificación. (Sin decimales, máximo 3 dígitos o 100 puntos): "))
print("")
calif2 = int(input("Dame la segunda calificación. (Sin decimales, máximo 3 dígitos o 100 puntos): "))
print("")
calif3 = int(input("Dame la tercera calificación. (Sin decimales, máximo 3 dígitos o 100 puntos): "))
print("")
promedio = (calif1+calif2+calif3)/3
if promedio<60:
    print ("Lamentable, reprobaste.")
else:
    print("Felicidades, aprobaste.")
