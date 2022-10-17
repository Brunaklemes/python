"""
8 - Faça um Programa que peça a idade e a altura de 5 pessoas, armazene cada
 informação no seu respectivo vetor. Imprima a idade e a altura na ordem inversa a 
 ordem lida.
"""
limite = int(input("Quantas pessoas serão: "))
idades = []
alturas = []
for numero in range(limite):
    idade = int(input("Digite sua idade: "))
    altura = float(input("Digite sua altura: "))
    idades.append(idade)
    alturas.append(altura)

print(f"As alturas digitadas foram {alturas[::-1]}\t e as idades são {idades[::-1]}")