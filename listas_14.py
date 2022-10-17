"""
14 - Utilizando listas faça um programa que faça 5 perguntas para uma pessoa sobre 
um crime. As perguntas são:
"Telefonou para a vítima?"
"Esteve no local do crime?"
"Mora perto da vítima?"
"Devia para a vítima?"
"Já trabalhou com a vítima?" O programa deve no final emitir uma classificação 
sobre a participação da pessoa no crime. Se a pessoa responder positivamente a
 2 questões ela deve ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice"
  e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente".
"""
perguntas = ["Telefonou para a vitima? S-Sim ou N-Não: ",
"Esteve no local do crime ? S-Sim ou N-Não: ",
'Mora perto da vítima? (Sim) ou N (Não): ',
'Devia para a vítima? (Sim) ou N (Não): ',
'Já trabalhou com a vítima? (Sim) ou N (Não): ']

soma = 0
for indice in perguntas:
  resposta = input(indice)
  resposta = resposta.upper()
  if resposta == "S":
    soma+=1

classificacao = ["Inocente","Suspeita","Cúmplice","Assassino"]

if soma == 2:
      print(classificacao[1])
elif soma >= 3 and soma <=4:
      print(classificacao[2])
elif soma == 5:
      print(classificacao[3])
else:
      print(classificacao[0])


