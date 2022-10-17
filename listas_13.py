"""
13 - Faça um programa que receba a temperatura média de cada mês do ano e armazene-as
 em uma lista. Após isto, calcule a média anual das temperaturas e mostre todas
  as temperaturas acima da média anual, e em que mês elas ocorreram (mostrar o 
  mês por extenso: 1 – Janeiro, 2 – Fevereiro, . . . ).
"""
meses = ['1-Janeiro', '2-Fevereiro', '3-Março', '4-Abril', '5-Maio', '6-Junho', '7-Julho', '8-Agosto', '9-Setembro', '10-Outubro', 
'11-Novembro', '12-Dezembro']
cont = 0
temperaturas = []
soma = 0

while cont < len(meses):
    tempera = float(input(f'Qual é a temperatura do mês de {meses[cont]}: '))
    temperaturas.append(tempera)
    soma += tempera
    cont += 1

media = soma / (cont)

cont = 0
for indice in temperaturas:
      if indice > media:
          print(f'A temperatura do mês de {meses[cont]} foi de {indice} e esta acima da média de {media:.2f}')
      cont += 1