"""
7 - Faça um Programa que leia um vetor de 5 números inteiros, mostre a soma, a
 multiplicação e os números.
"""
vetor = []
for indice in range(5):
    numero = int(input('Digite o número: '))
    vetor.append(numero)
soma = 0
mult = 1
for indice in range(len(vetor)):
    soma += vetor[indice]
    mult *= vetor[indice] 
print(f'Os valores do vetor são {vetor}, a soma é {soma} e a multiplicação é {mult}')