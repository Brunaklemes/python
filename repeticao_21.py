"""21 - Faça um programa que peça um número inteiro e determine se ele é ou não um número 
primo. Um número primo é aquele que é divisível somente por ele mesmo e por 1.
"""

numero = int(input('Digite um numero: '))
cont = 0

for divisao in range(1, numero + 1, 1):    
    if numero % divisao == 0:
        cont += 1
if cont > 2:
    print(f'O {numero} NÃO é primo')
else:
    print(f'O {numero} É primo')
    

