matrizA=[]
def imprimirmatriz(A):
    noreng = len(A)
    for x in range (noreng):
        print(A[x])
def llenarmatriz(B):
    numren = int(input("Introduce la cantidad de renglones: "))
    numcol = int(input("Introduce la cantidad de columnas: "))
    for x in range(numren):
        lista=[]
        for y in range(numcol):
            valor = int(input(f"introduce datos dentro de la celda [{x+1}][{y+1}]: "))
            lista.append(valor)
        B.append(lista)
    imprimirmatriz(B)
    return(B)
def traspuesta(C):
    numren = len(C)
    numcol = len(C[0])
    matrizC=[]
    for x in range (numcol):
        lista=[]
        for y in range (numren):
            numero = C[y][x]
            lista.append(numero)
        matrizC.append(lista)
    imprimirmatriz(matrizC)
def matrizdesplazadaabajo(D):
    numren = len(D)
    matrizD=[]
    r=0
    while(r<numren):
        matrizD.append(D[r-1])
        r+=1
    imprimirmatriz(matrizD)
def matriznumerosdesplazadosaladerecha(E):
    numren = len(E)
    numcol = len(E[0])
    matrizE=[]
    r=0
    while(r<numren):
        lista3=[]
        c=0
        while(c<numcol):
            valor=E[r][c-1]
            lista3.append(valor)
            c+=1
        matrizE.append(lista3)
        r+=1
    imprimirmatriz(matrizE)

llenarmatriz(matrizA)
print("\ntraspuesta")
traspuesta(matrizA)
print("\ndesplazada hacia abajo")
matrizdesplazadaabajo(matrizA)
print("\ndesplazada a la derecha")
matriznumerosdesplazadosaladerecha(matrizA)