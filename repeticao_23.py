"""23 - Faça um programa que mostre todos os primos entre 1 e N sendo N um número inteiro
 fornecido pelo usuário. O programa deverá mostrar também o número de divisões que 
 ele executou para encontrar os números primos. Serão avaliados o funcionamento, o
  estilo e o número de testes (divisões) executados.
"""

numero = int(input('Digite um numero: '))
contador = 2
divisoes = 0
primos = [] 
while contador <= numero:
      cont = 0

      for divisao in range(1, contador + 1, 1):
          divisoes += 1
          if contador % divisao == 0:
              cont += 1
              
      if cont < 3:
          primos.append(contador)
      contador += 1
print(f'O total de divisões foram {divisoes} e os numeros primos são {primos}')