"""19 - Altere o programa anterior para que ele aceite apenas números entre 0 e 1000.
"""
limite = int(input("Digite quantos numeros terá essa sequência: "))
soma= 0
cont = 1
lista = []

while cont <= limite:
    valor = int(input("Digite um valor a ser somado, entre 0 a 1000: "))
    if valor < 0 or valor > 1000:
        valor = int(input('Digitou um valor errado, digite novamente um valor entre 0 a 1000: '))
    else: 
        soma += valor
        cont+=1
        lista.append(valor)

print(lista)
maximo = max(lista)
minimo = min(lista)

print("A soma dos valores digitados é: ",soma)
print(f'O maior número é {maximo}')
print(f'O menor número é {minimo}')