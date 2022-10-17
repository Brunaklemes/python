"""7 - Faça um programa que leia 5 números e informe o maior número.

"""
n1 = int(input('Digite o numero 1: '))
n2 = int(input('Digite o numero 2: '))
n3 = int(input('Digite o numero 3: '))
n4 = int(input('Digite o numero 4: '))
n5 = int(input('Digite o numero 5: '))
ind = 0
lista = [n1, n2, n3, n4, n5]
while lista:
    if lista[ind] >= lista[0] and  lista[ind] >= lista[1] and lista[ind] >= lista[2] and lista[ind] >= lista[3] and lista[ind] >= lista[4]:
        print(f'O numero maior é {lista[ind]}')
    else:
        ind += 1
        continue
    break


