#Declarar
altura_Ana: float = 1.10
altura_Maria: float = 1.50
ano: int = 0

#Inicio
for ano in range(1, 100):
    altura_Ana += 0.03
    altura_Maria += 0.02
    if altura_Ana > altura_Maria:
        print(f"Ana ultrapassou Maria no ano {ano}.")
        break
    #Fim-para
#Fim