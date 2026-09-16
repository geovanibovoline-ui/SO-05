#Declare
numero_voltas: int = 0
extensao_pista: float = 0.0
tempo_total: float = 0.0

#Inicio
numero_voltas = int(input("Digite o número de voltas: "))
extensao_pista = float(input("Digite a extensão da pista (em metros): "))
tempo_total = float(input("Digite o tempo total (em segundos): "))
velocidade_media = (numero_voltas * extensao_pista) / tempo_total
kilometros_por_hora = velocidade_media * 3.6
print(f"A velocidade média é: {kilometros_por_hora:.2f} km/h")
#Fim