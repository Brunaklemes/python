"""
2 - Faça um Programa que leia um vetor de 10 números reais e mostre-os na ordem inversa.
"""
lista = []
for i in range(10):
    numero = float(input("Digite um número: "))
    lista.insert(0,numero)
print(lista)
print(lista[::-1])
