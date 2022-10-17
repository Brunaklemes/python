"""
18 - Faça um Programa que peça um número inteiro e determine se ele é par ou impar. Dica:
 utilize o operador módulo (resto da divisão).


"""
numero = int(input("Digite um numero: "))
resto = numero % 2

if resto == 0:
    print("Esse número é par!")
else:
    print("Esse número é impar!")


