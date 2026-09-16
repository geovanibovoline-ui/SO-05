#Declarar
base: int = 0
exponente: int = 0

#Inicio
base = int(input("Digite a base: "))
exponente = int(input("Digite o expoente: "))
valor_potencia: int = base ** exponente
print(f"{base} elevado a {exponente} é igual a {valor_potencia}")
#Fim