"""
21 - Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas 
são:
"Telefonou para a vítima?"
"Esteve no local do crime?"
"Mora perto da vítima?"
"Devia para a vítima?"
"Já trabalhou com a vítima?" O programa deve no final emitir uma classificação sobre
 a participação da pessoa no crime. Se a pessoa responder positivamente a 2 questões 
 ela deve ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice" e 5 como
  "Assassino". Caso contrário, ele será classificado como "Inocente".

"""
per_1 = input('Telefonou para a vítima? S (Sim) ou N (Não): ')
per_2 = input('Esteve no local do crime? (Sim) ou N (Não): ')
per_3 = input('Mora perto da vítima? (Sim) ou N (Não): ')
per_4 = input('Devia para a vítima? (Sim) ou N (Não): ')
per_5 = input('Já trabalhou com a vítima? (Sim) ou N (Não): ')
cont = 0
per_1, per_2, per_3, per_4, per_5 = per_1.upper(), per_2.upper(), per_3.upper(), per_4.upper(), per_5.upper()

if per_1 == 'S':
  cont += 1
if per_2 == 'S':
  cont += 1
if per_3 == 'S':
  cont += 1
if per_4 == 'S':
  cont += 1
if per_5 == 'S':
  cont += 1

if cont == 2:
  print('Suspeito')
elif cont > 2 and cont <5:
  print('Cúmplice')
elif cont == 5:
  print('Assassino')
else:
  print('Inocente')