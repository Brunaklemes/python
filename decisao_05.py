'''
5 - Faça um programa que pergunte o preço de três produtos e informe qual produto você 
deve comprar, sabendo que a decisão é sempre pelo mais barato.

'''
prod1 = float(input('Digite o valor do produto 01: '))
prod2 = float(input('Digite o valor do produto 02: '))
prod3 = float(input('Digite o valor do produto 03: '))

if prod1 < prod2 and prod1 < prod3:
    print('Compre o produto 01, é mais barato')
elif prod2 < prod1 and prod2 < prod3:
    print('Compre o produto 02, é mais barato')
else:
    print('Compre o produto 03, é mais barato')