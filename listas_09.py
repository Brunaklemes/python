"""
9 - Faça um Programa que leia um vetor A com 10 números inteiros, calcule e mostre a
soma dos quadrados dos elementos do vetor.
"""
limite = int(input('Digite o número de vezes: '))
vetor = []
soma = 0
for indice in range (limite):
    numero = int(input('Digite o numero: '))
    vetor.append(numero)
    quadrado = vetor[indice] ** 2
    soma += quadrado
print(f'O vetor é {vetor} e a soma dos quadrados é {soma}')
