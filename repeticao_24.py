"""24 - Faça um programa que calcule o mostre a média aritmética de N notas.
"""

valor = 1
cont = 1
soma =0
while valor != 0:
    valor = float(input("Digite uma nota: (obs: quando quiser encerrar digite '0'):"))
    soma += valor
    cont+=1
media = soma/cont
print(f"A média das {cont} notas digitadas é {media:.2f}")

