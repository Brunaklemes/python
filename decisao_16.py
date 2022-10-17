"""16 -  Faça um Programa que peça um número correspondente a um determinado ano e em 
seguida

informe se este ano é ou não bissexto.
"""
ano = int(input("Digite um ano: "))
resto = ano % 4
restoquatrocentos = ano % 400

dividido_cem = ano%100

if resto == 0:
    if dividido_cem > 0:
        print("Este ano é bissexto!")
    else:
        print("Este ano não é bissexto!")
else:
    if restoquatrocentos == 0:
        print("Este ano é bissexto!")
    else:
        print("Não é bissexto")