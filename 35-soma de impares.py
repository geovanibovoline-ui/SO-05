#Declarar
Num1: int = 0
Num2: int = 0
soma_impares: int = 0

#Inicio
Num1 = int(input("Digite o primeiro número inteiro: "))
Num2 = int(input("Digite o segundo número inteiro: "))
maior: int = max(Num1, Num2)
menor: int = min(Num1, Num2)
print(f"O maior número entre {Num1} e {Num2} é: {maior}")
print(f"O menor número entre {Num1} e {Num2} é: {menor}")
for i in range(menor, maior + 1):
    if i % 2 != 0:
        soma_impares += i
        #Fim-para
print(f"A soma dos números ímpares entre {menor} e {maior} é: {soma_impares}")
#Fim