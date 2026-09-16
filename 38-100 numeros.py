#Declarar
Num: int = 0
organisação_numeros: int = 0

#Inicio
Num = int(input("Digite um número inteiro: "))
for i in range(0, 100):
    numeros_sequenciais = Num + i
    print(f"Os números sequenciais são: {numeros_sequenciais}")
    if i == 0:
        maior_numero = numeros_sequenciais
        menor_numero = numeros_sequenciais
    else:
        if numeros_sequenciais > maior_numero:
            maior_numero = numeros_sequenciais
        if numeros_sequenciais < menor_numero:
            menor_numero = numeros_sequenciais
print(f"O maior número é: {maior_numero}")
print(f"O menor número é: {menor_numero}")
#Fim