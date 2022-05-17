import random
figus_total = 699
figus_paquete = 5
n_repeticiones = 100
iIdeal=850
lIdeal=[]
debug=False

#Implemento las funciones 
    
def generar_paquete (figus_total, figus_paquete):
    lPaquete=[]
    for i in range(figus_paquete):
        lPaquete.append(random.randint (1, figus_total))
    return lPaquete 

def cuantos_paquetes (figus_total, figus_paquete):
    iPaquetes=0
    incompleto=True
    album=[]
    while incompleto:
        
        iPaquetes+=1
        if debug:print("iteracion ", iPaquetes)
        lpaquete=generar_paquete(figus_total, figus_paquete)
        if debug:print("lpaquete q me toco" , lpaquete)
        
        album.extend(lpaquete)
        if debug:print("como queda el album dsp del extend" , album)
        
        #Elimino duplicados
        convert_list_to_set = set(album)
        new_list = list(convert_list_to_set)
        #ordeno la lista completa de figus
        new_list.sort()
        
        if debug:print("new_list",new_list)
        incompleto=False
        for i in range(len(new_list)):
            if (i+1) != new_list[i]:
                incompleto=True
                if debug:print("incompleto me falta la figu " , (i+1))
                break
        
    return iPaquetes, new_list

def promedio(lista):
    acum = 0
    for i in range(len(lista)):
        acum = lista[i] + acum
    return acum//len(lista)

def probabilidad(veces, total):
    return veces/total

iQpaq , ListaCompleta =cuantos_paquetes (figus_total, figus_paquete)
if debug:print (iQpaq)
if debug:print (ListaCompleta)


#Codigo principal
for i in range(n_repeticiones):
    ListaCompleta=[]
    lDeseada=[]
    #lacumula=[]
    iQpaq=0
    iQpaq , ListaCompleta =cuantos_paquetes (figus_total, figus_paquete)
    #print("Cantidad de paquetes por la iteracion" , iQpaq)
    lacumula.append(iQpaq)
    if iQpaq >= iIdeal:
        lIdeal.append(iQpaq)

#print ("lista q acumula" , lacumula)
iPromedioPaq = promedio(lacumula)
print("promedio de paquetes" , iPromedioPaq)
fProbabilidad=probabilidad(len(lIdeal),len(lacumula))
print("Probabilidad de completar el album con menos de ", iIdeal, "paquetes es : ", fProbabilidad)
