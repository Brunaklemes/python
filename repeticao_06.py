"""
6- Faça um programa que imprima na tela os números de 1 a 20, um abaixo do outro. Depois
 modifique o programa para que ele mostre os números um ao lado do outro.
"""

for n in range(20):
    print(n)

lista2 = []
for n in range(1, 21, 1):
    nova_lista2= lista2.append(n)
print(f'resultado for {lista2}')



x = 1
lista1 = []

while x<= 20:
    nova_lista1 = lista1.append(x)
    x+=1
print(lista1)

    