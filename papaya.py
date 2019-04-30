lista=[]
def largodepalabra(lista):
    palabra = ""
    largo = 0
    for i in lista:
        if (len(i) > largo ):
            palabra= i
            largo = len(i)
    return palabra        
    
    
for i in range(4):
     print("ingrese una palabra")
     palabra=input()
     lista.append(palabra)
print("la palabra mas larga es",largodepalabra(lista))

for i in lista:
     palabrainvertida = i[::-1]
     print(palabrainvertida)
     


 
     

