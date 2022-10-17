'''
11.Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros
 quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para
  cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam 
  R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços
 em 3 situações:
comprar apenas latas de 18 litros;
comprar apenas galões de 3,6 litros;
misturar latas e galões, de forma que o desperdício de tinta seja menor. Acrescente
 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias.
'''

from math import ceil

metro = float(input('Quantos metros quadrado: '))
lata18Litros = 80.00
galao3Litros = 25.00
# Apenas latas de 18 litros
tinta = (metro / 6)
qtidade_lata = tinta / 18
qtidade_galao = tinta / 3.6
qtidade_lata = ceil(qtidade_lata)
qtidade_galao = ceil(qtidade_galao)

tinta_acrescimo = tinta + (metro / 6) * 0.10
qtidade_acrescimo_lata = tinta_acrescimo // 18
qtidade_acrescimo_galao = (tinta_acrescimo % 18)/3.6
qtidade_acrescimo_galao = ceil(qtidade_acrescimo_galao) 

valor_lata = qtidade_lata * lata18Litros
valor_galao = qtidade_galao * galao3Litros
valor_misto = qtidade_acrescimo_galao * galao3Litros + qtidade_acrescimo_lata*lata18Litros

print(f'Na compra de apenas latas, serão necessárias {qtidade_lata} latas, e o valor será R$ {valor_lata:.2f}')
print(f'Na compra de apenas latas, serão necessárias  {qtidade_galao} galões, e o valor será R$ {valor_galao:.2f}')
print(f'Na compra mista serão {qtidade_acrescimo_lata} latas e {qtidade_acrescimo_galao} galões e o valor será R$ {valor_misto:.2f}')