#Declarar
Num1: int = 0

#Inicio
Num1 = int(input("Digite um número inteiro: "))
fatorial: int = 1
for i in range(1, Num1 + 1):
    fatorial *= i
    print(f"O fatorial de {i} é {fatorial}")
    #Fim-para
#Fim