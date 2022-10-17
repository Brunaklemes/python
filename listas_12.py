"""
12 - Foram anotadas as idades e alturas de 30 alunos. Faça um Programa que determine
 quantos alunos com mais de 13 anos possuem altura inferior à média de altura
  desses alunos.
"""

limite = int(input("Digite quantos alunos foram considerados: "))

soma = 0
alturas = []
idades = []
cont = 0

for alunos in range(limite):
    altura = float(input("Digite a altura do aluno: "))
    idade = int(input("Digite a idade de cada aluno: "))
    soma+=altura
    media=soma/limite
    alturas.append(altura)
    idades.append(idade)

print(alturas, '\t' , idades)

alunos = 0

while cont < limite:
      if alturas[cont] < media and idades[cont] == 13:
            alunos+=1
      cont+=1
      
print(f"{alunos} alunos com 13 possuem altura inferior à media {media:.2f}")
          





