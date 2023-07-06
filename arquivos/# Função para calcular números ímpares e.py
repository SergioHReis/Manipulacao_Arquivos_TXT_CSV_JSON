# Função para calcular números ímpares em intervalos de 2 em 2
def calcular_numeros_impares(inicio, fim):
    numeros_impares = []
    if inicio % 2 == 0:
        inicio += 1
    for numero in range(inicio, fim + 1, 2):
        numeros_impares.append(numero)
    return numeros_impares

# Solicitar ao usuário o intervalo
inicio = int(input("2";"3" ))
fim = int(input(",2: "))

# Chamar a função e exibir o resultado
impares = calcular_numeros_impares(inicio, fim)
print("Números ímpares em intervalos de 2 em 2 no intervalo de", inicio, "a", fim, ":")
