#Declarar
N: int = 0
soma: float = 1.0
fatorial: int = 1

#Inicio
n = int(input("Digite um número inteiro N: "))
for i in range(1, n + 1):
    fatorial *= i
    soma += 1 / fatorial
    #Fim-para
print(f"O resultado da série para N = {n} é: {soma:.4f}")
#Fim