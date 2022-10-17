"""16 - A série de Fibonacci é formada pela seqüência 0,1,1,2,3,5,8,13,21,34,55,... 
Faça um programa que gere a série até que o valor seja maior que 500.
"""
final = 500
cont1 = 0
cont2 = 1
cont3 = 0
fibonacci = [1]
tamanho = len(fibonacci)
novo_item = 0

while novo_item <= final:
    if cont3 == 0:
        novo_item = fibonacci[cont3]
        fibonacci.append(novo_item)
        cont3 += 1

    else:
        novo_item = fibonacci[cont1] + fibonacci[cont2]
        fibonacci.append(novo_item)
        cont1 += 1
        cont2 += 1
    tamanho = len(fibonacci)

print(fibonacci)