"""
8 - Faça um programa que leia 5 números e informe a soma e a média dos números.
"""
soma = 0
cont = 0

while cont < 5:
    n = int(input("Digite um número: "))
    soma += n
    cont += 1

media = soma/cont

print(f"A soma dos números é {soma}, e a média é {media}. ")