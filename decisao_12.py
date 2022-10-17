"""
12 - Faça um Programa que peça os 3 lados de um triângulo. O programa deverá informar
 se os valores podem ser um triângulo. Indique, caso os lados formem um triângulo,
  se o mesmo é: equilátero, isósceles ou escaleno.
Dicas:
Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que 
o terceiro;
Triângulo Equilátero: três lados iguais;
Triângulo Isósceles: quaisquer dois lados iguais;
Triângulo Escaleno: três lados diferentes;

"""

lado1 = int(input("Digite o primeiro lado: "))
lado2 = int(input("Digite o segundo lado: "))
lado3 = int(input("Digite o terceiro lado: "))

soma1 = lado1 + lado2
soma2 = lado1 + lado3
soma3 = lado2 + lado3
soma4 = lado3 + lado2

if soma1 > lado3 and soma2 > lado2 and soma3 > lado1 and soma4 > lado1:
      if lado1 == lado2 and lado1 == lado3:
          print("Esse triângulo é Equilátero!")
      elif lado1 == lado2 or lado1==lado3 or lado2==lado3:
          print("Esse triângulo é Isósceles!")
      else:
          print("Esse triângulo é escaleno!")
else:
      print("Não é um triângulo")