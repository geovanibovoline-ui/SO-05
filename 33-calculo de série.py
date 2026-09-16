#Declarar
N: int = 0
soma: float = 0.0

#Inicio
n = int(input("Digite um número inteiro N: "))
for i in range(1, n + 1):
    soma += 1 / i
    #Fim-para
print(f"O resultado da série para N = {n} é: {soma:.4f}")
#Fim