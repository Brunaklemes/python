'''
10. Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros
quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para
cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam
R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem compradas e o
preço total.

'''
from math import ceil


metro = float(input('Quantos metros quadrado: '))
lata18Litros = 80.00
tinta = metro / 3
qtidade_lata = tinta / 18
qtidade_lata = ceil(qtidade_lata)
valor_final = qtidade_lata * lata18Litros
print(f'Precisa de {qtidade_lata} latas e vai pagar R${valor_final:.2f}')




