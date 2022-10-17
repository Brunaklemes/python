'''
1 - Faça um Programa que peça dois números e imprima o maior deles e outro 
programa que peça um valor e mostre na tela se o valor é positivo ou negativo.
'''
num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))
num3 = int(input('Digite um número: '))

print('Programa 01')
if num1 > num2:
    print(f'O número {num1} é maior que o número {num2}')
else:
    print(f'O número {num2} é maior que o número {num1}')
print()
print('Programa 02')
if not num3 < 0:
    print(f'O número {num3} é positivo')
else:
    print(f'O número {num3} é negativo')