"""17 - Faça um Programa para um caixa eletrônico. O programa deverá perguntar ao usuário a
 valor do saque e depois informar quantas notas de cada valor serão fornecidas. As
  notas disponíveis serão as de 1, 5, 10, 50 e 100 reais. O valor mínimo é de 10
   reais e o máximo de 600 reais. O programa não deve se preocupar com a quantidade
    de notas existentes na máquina.
Exemplo 1: Para sacar a quantia de 256 reais, o programa fornece duas notas de 100,
 uma nota de 50, uma nota de 5 e uma nota de 1;
Exemplo 2: Para sacar a quantia de 399 reais, o programa fornece três notas de 100,
 uma nota de 50, quatro notas de 10, uma nota de 5 e quatro notas de 1.

"""
import re


saque = int(input('Qual é o valor do saque: '))
if saque < 10 and saque > 600:
    print('O saque deve ser entre R$ 10,00 e R$ 600,00')
else:
    notas100 = saque // 100
    print(notas100)
    notas50 = (saque % 100) // 50
    print(notas50)
    notas10 = saque % 100 % 50 // 10
    print(notas10)
    notas5 = saque % 100 % 50 % 10 // 5
    print(notas5)
    notas1 = saque % 100 % 50 % 10 % 5 // 1
    print(notas1)
    print(f'Será impresso {notas100} notas de R$ 100,00,\
 {notas50} notas de R$ 50,00,\
 {notas10} notas de R$ 10,00,\
 {notas5} notas de R$ 5,00 e {notas1} notas de R$ 1,00')