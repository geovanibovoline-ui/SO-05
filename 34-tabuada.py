#Declarar
Num: int = 0
tabuada: int = 0

#Inicio
Num = int(input("Digite um número para ver a tabuada: "))
for  i in range(1, 11):
    #Fim-para
    tabuada = Num * i
    print(f"{Num} x {i} = {tabuada}")
#Fim