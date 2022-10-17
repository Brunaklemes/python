"""
17 - Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário.
 Ex.:
 5!=5.4.3.2.1=120
 """

numero = int(input('Digite o número: '))
lista = []
for i in range(numero,0,-1):
    lista.append(i)

cont = 0
ind1 = 1
final = len(lista)

while cont < final:
    if cont == 0:
        mult = lista[cont] * lista[ind1]
        ind1 += 1
        cont += 1
    else:
        mult = mult * lista[ind1]
        ind1 += 1
    
    cont += 1
print(mult)
