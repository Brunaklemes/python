"""
11 - Altere o programa anterior para mostrar no final a soma dos números.
"""

n1 = int(input("Digite um número: "))
n2 = int(input("Digite outro número: "))
soma = 0
if n1 > n2:
    n2+=1
    for i in range(n2,n1):
        soma += i
        print(i)
    print(soma)
else:
    n1+=1
    for i in range(n1,n2):
        soma += i
        print(i)
    print(soma)