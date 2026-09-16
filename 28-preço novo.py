#Declarar
venda_mensal: float = 0.0
preco_atual: float = 0.0

#Inicio
venda_mensal = float(input("Digite a venda mensal média: "))
preco_atual = float(input("Digite o preço atual: R$ "))
if venda_mensal < 500 and preco_atual < 30:
    preco_novo = preco_atual * 1.10
elif venda_mensal >= 500 and venda_mensal < 1000 and preco_atual >= 30 and preco_atual < 80:
    preco_novo = preco_atual * 1.15
elif venda_mensal >= 1000 and preco_atual >= 80:
    preco_novo = preco_atual * 0.95
else:
    preco_novo = preco_atual
print(f"Preço novo: R$ {preco_novo:.2f}")
#Fim