"""
15 - Faça um programa que leia um número indeterminado de valores, correspondentes 
a notas, encerrando a entrada de dados quando for informado um valor igual a -1
 (que não deve ser armazenado). Após esta entrada de dados, faça:
Mostre a quantidade de valores que foram lidos;
Exiba todos os valores na ordem em que foram informados, um ao lado do outro;
Exiba todos os valores na ordem inversa à que foram informados, um abaixo do outro;
Calcule e mostre a soma dos valores;
Calcule e mostre a média dos valores;
Calcule e mostre a quantidade de valores acima da média calculada;
Calcule e mostre a quantidade de valores abaixo de sete;
Encerre o programa com uma mensagem;
"""
nota = 0
todas_notas = []
soma = 0
while not nota == -1:
    nota = float(input('Digite o valor da nota (Se desejar encerrar digite "-1"): '))
    if not nota == -1:
        soma += nota
        todas_notas.append(nota)
qtide = len(todas_notas)
media = soma / qtide
print(f'A qtde de notas lidas foram {qtide}')
print(f'As notas digitadas foram {todas_notas}')
for indice in todas_notas:
    print(todas_notas[qtide-1])
    qtide -= 1
qtide = len(todas_notas)
print(f'A soma das notas é {soma}')
print(f'A media das notas é {media:.2f}')
notas_acima = []
notas_abaixo = []
for indice in todas_notas:
    if indice > media:
        notas_acima.append(indice)
    if indice < 7:
        notas_abaixo.append(indice)
print (f'As notas acima da média são: {notas_acima}')
print (f'As notas abaixo de 7 são: {notas_abaixo}')