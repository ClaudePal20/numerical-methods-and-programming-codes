#PROGRAMA PARA SOLICITAR LA CANTIDAD DEL SUELDO DE UNA PERSONA
# SI LOS INGRESOS ESTAN ENTRE 0 Y 5000 = APLICAR 3% DE IMPUESTOS
# SI LOS INGRESOS ESTAN ENTRE 5001 Y 10001 = APLICAR 5% DE IMPUESTOS
# ''                ''  ENTRE 10001 Y 15001 = APLICAR 7% DE IMPUESTOS
# ''                ''  EN 15001 PARA ARRIBA = APLICAR 10% DEI MPUESTOS
try:
    sueldo = int(input("Captura lo que gana la persona:"))
    if sueldo>=0:
        if sueldo<=5000: #sueldo entre 0 y 5000 pesos:
            impuesto = sueldo*0.03
        elif sueldo<=10000:
            impuesto = sueldo*0.05
        elif sueldo<=15000:
            impuesto = sueldo*0.07
        else:
            impuesto = sueldo*0.1
        print(f"El impuesto a pagar es = {impuesto:.2f}")
    else:
        print("Error, la cantidad es negativa")
except ValueError:
    print("Valor no válido, solo usar valores int")