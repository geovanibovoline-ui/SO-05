#Declarar
Num1: float = 0.0
Num2: float = 0.0

#Inicio
Num1 = float(input("Digite o primeiro número real: "))
Num2 = float(input("Digite o segundo número real: "))
if Num1 > Num2:
    maior: float = Num1
else:
    maior: float = Num2
    #Fim-se
print("O maior número é:", maior)
#Fim