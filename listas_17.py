"""
17 - Em uma competição de salto em distância cada atleta tem direito a cinco saltos. 
O resultado do atleta será determinado pela média dos cinco valores restantes. 
Você deve fazer um programa que receba o nome e as cinco distâncias alcançadas
 pelo atleta em seus saltos e depois informe o nome, os saltos e a média dos 
 saltos. O programa deve ser encerrado quando não for informado o nome do atleta.
  A saída do programa deve ser conforme o exemplo abaixo:
Atleta: Rodrigo Curvêllo
 
Primeiro Salto: 6.5 m
Segundo Salto: 6.1 m
Terceiro Salto: 6.2 m
Quarto Salto: 5.4 m
Quinto Salto: 5.3 m

Resultado final:
Atleta: Rodrigo Curvêllo
Saltos: 6.5 - 6.1 - 6.2 - 5.4 - 5.3
Média dos saltos: 5.9 m
"""
nome = input('Digite o nome do atleta: ')
nome_saltos = []
cont = 0
while not nome == '-1':
    nome_saltos.append([nome])
    for indice in range(1,6,1):
        saltos = float(input(f'Digite o salto {indice}: '))
        nome_saltos[cont].append(saltos)
    cont += 1
    nome = input('Digite o nome do atleta: ')

for indice in range(len(nome_saltos)):
    soma = 0
    for indice2 in range(1, len(nome_saltos[indice]), 1):
        soma += nome_saltos[indice][indice2]
    media = soma/indice2
    nome_saltos[indice].insert(1, media)


for indice in range(len(nome_saltos)):
    print(f'Atleta: {nome_saltos[indice][0]}')
    print()
    print(f'Primeiro Salto: {nome_saltos[indice][2]} m\nSegundo Salto: {nome_saltos[indice][3]} m\n\
Terceiro Salto: {nome_saltos[indice][4]} m\nQuarto Salto: {nome_saltos[indice][5]} m\nQuinto Salto: {nome_saltos[indice][6]} m')
    print()
    print(f'Resultado Final:\nAtleta: {nome_saltos[indice][0]}\nSaltos: {nome_saltos[indice][2:]}\nMédia dos santos: {nome_saltos[indice][1]}')
    print()