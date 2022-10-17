"""22 - Um posto está vendendo combustíveis com a seguinte tabela de descontos:
Álcool:
até 20 litros, desconto de 3% por litro
acima de 20 litros, desconto de 5% por litro
Gasolina:
até 20 litros, desconto de 4% por litro
acima de 20 litros, desconto de 6% por litro Escreva um algoritmo que leia o número
 de litros vendidos, o tipo de combustível (codificado da seguinte forma: A-álcool,
  G-gasolina), calcule e imprima o valor a ser pago pelo cliente sabendo-se que o
   preço do litro da gasolina é R$ 2,50 o preço do litro do álcool é R$ 1,90.
"""

litros = float(input("Digite a quantidade de combustível abastecido: "))
tipo = input("Digite o tipo de combustível: A-álcool ou G-gasolina: ")

gasolina = 2.5
alcool = 1.9
if tipo == "G":
       if litros <= 20:
             gasolina = gasolina - (gasolina*0.04)
             total = litros * gasolina
             print(f"O valor a ser pago é {total:.2f}")
       else :
             gasolina = gasolina - (gasolina*0.06)
             total = litros * gasolina
             print(f'{gasolina}')
             print(f"O valor a ser pago é {total:.2f}")
if tipo == "A":
       if litros <= 20:
             alcool = alcool - (alcool*0.03)
             total = litros * alcool
             print(f"O valor a ser pago é {total:.2f}")
       else :
             alcool = alcool - (alcool*0.05)
             total = litros * alcool
             print(f"O valor a ser pago é {total:.2f}")

