#Declarar
dado1: int = 0
dado2: int = 0
probabilidade: float = 0.0

#Inicio
for dado1 in range(1, 7):
    for dado2 in range(1, 7):
        if dado1 + dado2 == 7:
            probabilidade += 1
            #Fim-se
            #Fim-para
    print(f"Probabilidade de sair 7: {probabilidade/36:.2%}")
#Fim