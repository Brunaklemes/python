"""15 - Faça um Programa que leia um número inteiro menor que 1000 e imprima a quantidade
 de centenas, dezenas e unidades do mesmo.
Observando os termos no plural a colocação do "e", da vírgula entre outros. Exemplo:
326 = 3 centenas, 2 dezenas e 6 unidades
12 = 1 dezena e 2 unidades Testar com: 326, 300, 100, 320, 310,305, 301, 101, 311, 
111, 25, 20, 10, 21, 11, 1, 7 e 16
"""

numero = int(input('Digite um número menor que 1000: '))
if numero < 1000:
    centena = numero // 100
    resto_cent = numero % 100
    dezena = resto_cent // 10
    resto_dez = numero % 10
    unidade = resto_dez

    if centena != 1:
        unidade_cent = 'centenas'
    else:
        unidade_cent = 'centena'

    if dezena != 1:
        unidade_dez = 'dezenas'
    else:
        unidade_dez = 'dezena'

    if unidade != 1:
        unidade_uni = 'unidades'
    else:
        unidade_uni = 'unidade'

    print(f'{centena} {unidade_cent}, {dezena} {unidade_dez} e {unidade} {unidade_uni}')
else:
    print('O número é maior que 1000')


