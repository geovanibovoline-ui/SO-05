#Declarar
hora_inicial: int = 0
minutos_iniciais: int = 0
hora_final: int = 0
minutos_finais: int = 0

#Inicio
hora_inicial = int(input("Digite a hora inicial: "))
minutos_iniciais = int(input("Digite os minutos iniciais: "))
hora_final = int(input("Digite a hora final: "))
minutos_finais = int(input("Digite os minutos finais: "))
soma_horas = hora_final - hora_inicial
soma_minutos = minutos_finais - minutos_iniciais
if soma_horas < 0:
    soma_horas += 24
if soma_minutos < 0:
    soma_horas -= 1
    soma_minutos += 60
else:
    if soma_horas == 0 and soma_minutos == 0:
        soma_horas = 24
        #Fim-se
#Fim-se
print(f"O jogo durou {soma_horas} hora(s) e {soma_minutos} minuto(s).")
#Fim