"""22 - Altere o programa de cálculo dos números primos, informando, caso o número não seja
 primo, por quais número ele é divisível.
"""

numero = int(input('Digite um numero: '))
cont = 0
divisiveis = []

for divisao in range(1, numero + 1, 1):    
    if numero % divisao == 0:
        divisiveis.append(divisao)
        cont += 1


if cont > 2:
    print(f'O {numero} NÃO é primo, pois ele é divísivel por {divisiveis}')
else:
    print(f'O {numero} É primo')

