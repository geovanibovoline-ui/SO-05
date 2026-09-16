#Declarar
Num: int = 0

#Inicio
def fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    serie = [0, 1]
    while len(serie) < n:
        proximo_termo = serie[-1] + serie[-2]
        serie.append(proximo_termo)    
    return serie
Num = int(input("Digite o número de termos (N): "))
resultado = fibonacci(Num)
print(f"Série de Fibonacci até o {Num}º termo:")
print(resultado)
#Fim