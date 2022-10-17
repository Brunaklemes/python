"""
19 - Faça um Programa que peça um número e informe se o número é inteiro ou decimal. 
Dica: utilize uma função de arredondamento.
"""
numero = float(input('Digite um núemro: '))

if numero % 1 == 0:
    print(f'O número {round(numero)} é inteiro')
else:
    print(f'O número {numero:.2f} é decimal')



