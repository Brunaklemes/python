"""
5 - Faça um Programa que leia 20 números inteiros e armazene-os num vetor. Armazene
 os números pares no vetor PAR e os números IMPARES no vetor impar. Imprima os
  três vetores.
"""
cont = 1
vetor = []
vetor_impar = []
vetor_par = []
while cont < 21:
    num = int(input('Digite o numero: '))
    vetor.append(num)
    if num % 2 == 0:
          vetor_par.append(num)
    else:
      vetor_impar.append(num)
    cont += 1
print(f'Vetor completo {vetor}, o vetor par {vetor_par} e o vetor impar {vetor_impar}.')