"""
10 - Faça um Programa que leia dois vetores com 10 elementos cada. Gere um terceiro 
vetor de 20 elementos, cujos valores deverão ser compostos pelos elementos
 intercalados dos dois outros vetores.
"""
vetor1 = []
vetor2 = []

for valor in range(20):
    numero = int(input("Digite um numero: "))
    if valor<10:
        vetor1.append(numero)
    else:
        vetor2.append(numero)
print(vetor1)
print(vetor2)

vetor3 = []

for indice in range(10):
    vetor3.append(vetor1[indice])
    vetor3.append(vetor2[indice])

print(vetor3)