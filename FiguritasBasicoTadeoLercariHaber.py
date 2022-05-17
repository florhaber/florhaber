import random

totalFigus = 6
album=[]
nRepeticiones= 5
lcuantasFigusMeFaltan=[]
albumCompleto=[]

def generoAlbumVacio(totalFigus):
    cLista=[0]*totalFigus
    return cLista

def comprarFigus(totalFigus):
    return random.randint(0,totalFigus-1)


def estaLleno(album):
    for i in range(totalFigus):
        if album[i]==0:
            return False
    return True

def cuantasFigusMeFaltan(totalFigus):
    #Trato de completar el album, pensando que no me va a salir ninguna figu repetida
    iTotalFigus=0
    while True:
        iTotalFigus+=1
        figuQueToca=comprarFigus(totalFigus)
        if album[figuQueToca]==0:
            album[figuQueToca]=1       
        bestaLleno=estaLleno(album)
        if bestaLleno:
            return iTotalFigus


def promedio(lista):
    acum = 0
    for i in range(len(lista)):
        acum = lista[i] + acum
    return acum//len(lista)


#Pruebo mis funciones
#genero la lista representando q no tengo figus en el album
album=generoAlbumVacio(totalFigus)

#Y sino cuantas figus me faltan?
icuantasFigusMeFaltan=cuantasFigusMeFaltan(totalFigus)
#Ahora veo como me quedo el album
print("Compre " + str(icuantasFigusMeFaltan) + " figus para completar el album")

#Ejecuto para la repeticion
for i in range(nRepeticiones): 
    album=generoAlbumVacio(totalFigus)    
    lcuantasFigusMeFaltan.append(cuantasFigusMeFaltan(totalFigus))
    
 
print(lcuantasFigusMeFaltan)
elPromedio=round(promedio(lcuantasFigusMeFaltan),0)
print ("Teniendo en cuenta un album con " + str(totalFigus) + " y " + str(nRepeticiones) + " repticiones," )
print("el promedio de figuritas que tuve que comprar para completar el album  fue de " + str(elPromedio) + " figuritas ")

