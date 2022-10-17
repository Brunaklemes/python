"""20 - Altere o programa de cálculo do fatorial, permitindo ao usuário calcular o fatorial
 várias vezes e limitando o fatorial a números inteiros positivos e menores que 16.


 17 - Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário.
 Ex.:
 5!=5.4.3.2.1=120
"""
while True:
    numero = int(input('Digite um número de 0 a 16: '))
    if numero >= 0 and numero < 16:
        lista = []
        for i in range(numero,0,-1):
            lista.append(i)

        cont = 0
        ind1 = 1
        final = len(lista)

        while cont < final:
            if cont == 0:
                mult = lista[cont] * lista[ind1]
                ind1 += 1
                cont += 1
            else:
                mult = mult * lista[ind1]
                ind1 += 1
            cont += 1
        print(mult)
    else:
        print(input("Você digitou errado, digite um número de 0 a 16: "))
        break

    continuar = input("Você deseja continuar: S-Sim, N-Não? ")
    continuar = continuar.upper()
    if continuar == "N":
        break
   

