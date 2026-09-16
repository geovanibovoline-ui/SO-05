#Declarar
graos: int = 0
casas: int = 0

#Inicio
for i in range(64):
    graos = 2 ** i
    casas += graos
    #Fim-para
print(f"Total de graos: {casas}")
#Fim