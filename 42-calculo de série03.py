#Declarar
soma: float = 0.0

#Inicio
for i in range(1, 51):
    soma += i / (2 * i - 1)
    #Fim-para
print(f"O resultado da série é: {soma:.4f}")
#Fim