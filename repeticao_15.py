"""15 - A série de Fibonacci é formada pela seqüência 1,1,2,3,5,8,13,21,34,55,... Faça
um programa capaz de gerar a série até o n−ésimo termo.
"""
final = int(input('Até qual tamanho quer consultar a lista de Fibonacci: '))
cont1 = 0
cont2 = 1
cont3 = 0
fibonacci = [1]
tamanho = len(fibonacci)

while tamanho < final:
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