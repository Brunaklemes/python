"""14 - Faça um programa que peça 10 números inteiros, calcule e mostre a quantidade de
 números pares e a quantidade de números impares.
"""
cont = 0
lista = []
par = 0
impar = 0

while cont < 10:
    numero = int(input("Digite um número: "))
    lista.append(numero)
    resto = lista[cont]%2
    if resto == 0:
        par+=1
    else:
        impar+=1
    cont += 1
print(lista, par, impar)
