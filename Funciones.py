def Factorial(n):
    f=1
    for i in range(1,n+1):
        f*=i
    return f


def taylor(Vv, Rt, x):
    Ea=100
    Va=1
    i=1
    Er= ErrorVerdadero(Vv,Va)
    tabla = [[Va,Er,Ea]]
    while Ea > Rt:
        Va_ant = Va
        Va += (x**i)/Factorial(i)
        Er = ErrorVerdadero(Vv,Va)
        Ea = ErrorAproximado(Va,Va_ant)
        tabla.append([Va,Er,Ea])
        i+=1
    return tabla

def imprimetabla(tabla):
    for renglon in tabla:
        print(renglon)

def RangoTolerancia(n):
    return 0.5*10**(2-n)

def ErrorVerdadero(Vv,Va):
    return abs((Vv-Va)/Vv)*100

def ErrorAproximado(Va,Va_ant):
    return abs((Va-Va_ant)/Va)*100
#def f(x):
    #return ((x**2)-2)
def f(x):
    return ((x**3)-5)
#Para sacar xr
def xr_regla_falsa(xi,xu):
    xr = xu-(f(xu)*(xi-xu))/(f(xi)-f(xu))
    return xr
def imprimirmatriz(tabla):
    numren = len(tabla)
    for x in range (numren):
        print(tabla[x])
def regla_false(Vv,xi,xu,rt):
    Ea = 100
    xr_ant = False
    #Nueva tabla para introducir los datos
    tabla = []
    lista = []
    numren = 0
    while (Ea>rt):
        xr = xr_regla_falsa(xi,xu)
        Ev = ErrorVerdadero(Vv,xr)
        if (xr_ant is not False):
            Ea = ErrorAproximado(xr,xr_ant)
        lista.append([xi,xu,xr,Ev,Ea])
        tabla.append(lista)
        if ((f(xi)*f(xr))<0):
            xu = xr
        else:
            xi = xr
        xr_ant=xr
        numren += 1
    return tabla