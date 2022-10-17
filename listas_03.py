"""
3 - Faça um Programa que leia 4 notas, mostre as notas e a média na tela.
"""
cont = 1
soma_nota = 0
notas = []
while cont < 5:
    nota = float(input('Digite a nota: '))
    notas.append(nota)
    soma_nota += nota
    media = soma_nota / cont
    cont += 1
print(f'As notas são {notas} e a média é {media:.2f}')