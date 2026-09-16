#Declarar
soma: float = 0.0

#Inicio
for i in range(1, 15):
    termo = i / (i ** 2)
    if i % 2 == 0:
        soma -= termo
    else:
        soma += termo
    #Fim-para
print(f"A soma da série é: {soma}")
#Fim