"""10 - Faça um programa que receba dois números inteiros e gere os números inteiros que 
estão no intervalo compreendido por eles.
"""

n1 = int(input("Digite um número: "))
n2 = int(input("Digite outro número: "))

if n1 > n2:
    n2+=1
    for i in range(n2,n1):
        print(i)
else:
    n1+=1
    for i in range(n1,n2):
        print(i)
