"""18 - Faça um programa que, dado um conjunto de N números, determine o menor valor, o
 maior valor e a soma dos valores.
"""
limite = int(input("Digite quantos numeros terá essa sequência: "))

soma= 0
cont = 1
lista = []
while cont <= limite:
    valor = int(input("Digite um valor a ser somado: "))
    soma += valor
    cont+=1
    lista.append(valor)

print(lista)
maximo = max(lista)
minimo = min(lista)
print("A soma dos valores digitados é: ",soma)
print(f'O maior número é {maximo}')
print(f'O menor número é {minimo}')