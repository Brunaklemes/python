"""
13 - Faça um programa que calcule as raízes de uma equação do segundo grau, na forma ax2
 + bx + c. O programa deverá pedir os valores de a, b e c e fazer as consistências,
  informando ao usuário nas seguintes situações:
Se o usuário informar o valor de A igual a zero, a equação não é do segundo grau e
 o programa não deve fazer pedir os demais valores, sendo encerrado;
Se o delta calculado for negativo, a equação não possui raizes reais. Informe ao
 usuário e encerre o programa;
Se o delta calculado for igual a zero a equação possui apenas uma raiz real; 
informe-a ao usuário;
Se o delta for positivo, a equação possui duas raiz reais; informe-as ao usuário;

"""
a = int(input('Digite o primeiro valor: '))
if a == 0:
      print('Não é uma equação do 02° grau!!!')
else:
      b = int(input('Digite o segundo valor: '))
      c = int(input('Digite o terceiro valor: '))
      delta = b ** 2 - 4 * a * c
      if delta < 0:
            print('Não possui raizes!!!!')
      elif delta == 0:
            print('Possui uma raiz!!!')
      else:
            raizdelta = delta ** 0.5
            x1 = (- b + raizdelta) / (2 * a)
            x2 = (- b - raizdelta) / (2 * a)
            print(f'{x1:.2f}, {x2:.2f}')