from clase import conjunto
if __name__=='__main__':
    listaA=conjunto()
    listaB=conjunto()
    listaC=conjunto()
    for i in 5:
        carga = int(input("Ingrese numero a cargar"))
        listaA[i]=carga
    for i in 5:
        carga = int(input("Ingrese numero a cargar"))
        listaB[i]=carga
    
    for i in range(len(listaA)):
        if listaA[i]!=listaB[i]:
            listaC[i]+=listaA[i]
    for i in range(len(listaA)):
        if listaA[i]!=listaB[i]:
            listaC[i]+=listaB[i]
    for i in range(len(listaC)):
        print(listaC[i])        