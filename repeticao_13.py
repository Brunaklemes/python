"""13 - Faça um programa que peça dois números, base e expoente, calcule e mostre o primeiro
número elevado ao segundo número. Não utilize a função de potência da linguagem.

"""
base = int(input('Digite o valor da base para cálculo: '))
expoente = int(input('Digote o valor do expoente: '))
multiplicao = base
cont = 1
while cont < expoente:
    operacao = base * multiplicao
    base = operacao
    cont += 1
print(operacao)