#Declarar
Num1: int = 0
Num2: int = 0

#Inicio
Num1 = int(input("Digite o primeiro número: "))
Num2 = int(input("Digite o segundo número: "))
diferenca: int = Num2 - Num1
for i in range(Num1, Num2 + 1):
    primo: bool = True
    for j in range(2, i):
        if i % j == 0:
            primo = False
            break
    if primo and i > 1:
        print(f"{i} é primo")
    #Fim-se
    #Fim-para
#Fim