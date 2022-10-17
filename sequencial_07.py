'''
07 - Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
o produto do dobro do primeiro com metade do segundo .
a soma do triplo do primeiro com o terceiro.
o terceiro elevado ao cubo.

'''
a = int(input('Digite um valor inteiro: '))
b = int(input('Digite outro valor inteiro: '))
c = float(input('Digite um valor real: '))

dobro = (a * 2) * (b / 2)
soma = a * 3 + c
cubo = c ** 3
print(f'O produto é {dobro:.2f}\na soma é {soma:.2f}\no cubo é {cubo:.2f}')

