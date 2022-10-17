"""6 - Faça um Programa que peça as quatro notas de 10 alunos, calcule e armazene num
 vetor a média de cada aluno, imprima o número de alunos com média maior ou igual 
 a 7.0.
 """    
alunos = 0
medias_alunos = []
for n in range (10):
    soma = 0
    for num in range (4):
        nota = float(input("Digite uma nota: "))
        soma+=nota
    media=soma/4
    medias_alunos.append(media)
    if media >=7:
        alunos +=1
print(f"As médias alcançadas são {medias_alunos} e {alunos} \
alunos alcançaram média = ou superior a 7.0.")