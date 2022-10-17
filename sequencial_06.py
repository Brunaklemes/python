'''
6. Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a 
temperatura em graus Celsius.
C = 5 * ((F-32) / 9).
'''
fahre = float(input('Qual é a temperatura em Fahrenheit: '))
celsius = 5 * ((fahre-32) / 9)
print(f'A temperatura em graus celsius é {celsius:.1f}')