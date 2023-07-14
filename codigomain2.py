from codigofunciones import *
import pandas as pd
Vv = 5**(1/3)
xi = 1
xu = 2
n = 2
rt = RangoTolerancia(n)

tabla1 = regla_false(Vv,xi,xu,rt)
print("xi, xu, xr, Ev, Ea")
tabladevalores1 = imprimirmatriz(tabla1)

# print("********************")
# print("xi, xu, xr, Ev, Ea")
# tabla2 = regla_false(Vv2,xi,xu,rt)
# tabladevalores2 = imprimirmatriz(tabla2)
# #Usamos la misma funcion para desplegar tablas pero ahora con nuestra tabla

