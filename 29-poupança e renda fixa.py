#Declarar
valor: float = 0.0

#Inicio
tipo = int(input("Digite o tipo de investimento (1 - Poupança / 2 - Renda Fixa): "))
valor = float(input("Digite o valor do investimento: R$ "))
if tipo == 1:
    valor_corrigido = valor * 1.03
    print(f"Valor corrigido em 30 dias: R$ {valor_corrigido:.2f}")
elif tipo == 2:
    valor_corrigido = valor * 1.05
    print(f"Valor corrigido em 30 dias: R$ {valor_corrigido:.2f}")
else:
    print("Tipo de investimento inválido.")
    #Fim-se
#Fim