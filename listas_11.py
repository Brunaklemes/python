"""
11 - Altere o programa anterior, intercalando 3 vetores de 10 elementos cada.
"""
vetor1 = []
vetor2 = []
vetor3 = []
vetor4 = []

for valor in range(30):
    numero = int(input("Digite um numero: "))
    if valor<10:
        vetor1.append(numero)
    elif valor >= 10 and valor < 20:
        vetor2.append(numero)
    else:
        vetor3.append(numero)
print(vetor1, '\t', vetor2, '\t', vetor3 )

for indice in range(10):
    vetor4.append(vetor1[indice]), vetor4.append(vetor2[indice]), vetor4.append(vetor3[indice]) 
print(vetor4)