'''
9 - Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos 
são do Imposto de Renda, que depende do salário bruto (conforme tabela abaixo) e 3%
 para o Sindicato e que o FGTS corresponde a 11% do Salário Bruto, mas não é
  descontado (é a empresa que deposita). O Salário Líquido corresponde ao Salário
   Bruto menos os descontos. O programa deverá pedir ao usuário o valor da sua hora 
   e a quantidade de horas trabalhadas no mês.
Desconto do IR:
Salário Bruto até 900 (inclusive) - isento
Salário Bruto até 1500 (inclusive) - desconto de 5%
Salário Bruto até 2500 (inclusive) - desconto de 10%
Salário Bruto acima de 2500 - desconto de 20% Imprima na tela as informações, 
dispostas conforme o exemplo abaixo. No exemplo o valor da hora é 5 e a quantidade
 de hora é 220.
        Salário Bruto: (5 * 220)        : R$ 1100,00
        (-) IR (5%)                     : R$   55,00  
        (-) INSS ( 10%)                 : R$  110,00
        FGTS (11%)                      : R$  121,00
        Total de descontos              : R$  165,00
        Salário Liquido                 : R$  935,00
'''
hora_trabalhada = int(input('Qtas horas de trabalho: '))
valor_hora = float(input('Qual é o valor da hora: '))
ir = 0

salario_bruto = valor_hora * hora_trabalhada
sindicato = salario_bruto * 0.03
fgts = salario_bruto * 0.11
inss = salario_bruto * 0.10

if salario_bruto <= 900:
    total_desc = inss + sindicato
    salario_liquido = salario_bruto - total_desc
    print(f'Salário Bruto: ({valor_hora} * {hora_trabalhada})      : R$ {salario_bruto:.2f}\n\
(-) IR (isento)                 : R$ 00,00\n\
(-) INSS (10%)                  : R$ {inss:.2f}\n\
(-) SINDICATO (03%)             : R$ {sindicato:.2f}\n\
FGTS (11%)                      : R$ {fgts:.2f}\n\
Total de descontos              : R$ {total_desc:.2f}\n\
Salário Liquido                 : R$ {salario_liquido:.2f}')
elif salario_bruto > 900 and salario_bruto <= 1500:
    ir = salario_bruto * 0.05
    total_desc = inss + sindicato + ir
    salario_liquido = salario_bruto - total_desc
    print(f'Salário Bruto: ({valor_hora} * {hora_trabalhada})      : R$ {salario_bruto:.2f}\n\
(-) IR (05%)                    : R$ {ir}\n\
(-) INSS (10%)                  : R$ {inss:.2f}\n\
(-) SINDICATO (03%)             : R$ {sindicato:.2f}\n\
FGTS (11%)                      : R$ {fgts:.2f}\n\
Total de descontos              : R$ {total_desc:.2f}\n\
Salário Liquido                 : R$ {salario_liquido:.2f}')
elif salario_bruto > 1500 and salario_bruto <= 2500:
    ir = salario_bruto * 0.10
    total_desc = inss + sindicato + ir
    salario_liquido = salario_bruto - total_desc
    print(f'Salário Bruto: ({valor_hora} * {hora_trabalhada})      : R$ {salario_bruto:.2f}\n\
(-) IR (10%)                    : R$ {ir}\n\
(-) INSS (10%)                  : R$ {inss:.2f}\n\
(-) SINDICATO (03%)             : R$ {sindicato:.2f}\n\
FGTS (11%)                      : R$ {fgts:.2f}\n\
Total de descontos              : R$ {total_desc:.2f}\n\
Salário Liquido                 : R$ {salario_liquido:.2f}')
else:
    ir = salario_bruto * 0.20
    total_desc = inss + sindicato + ir
    salario_liquido = salario_bruto - total_desc
    print(f'Salário Bruto: ({valor_hora} * {hora_trabalhada})      : R$ {salario_bruto:.2f}\n\
(-) IR (20%)                    : R$ {ir}\n\
(-) INSS (10%)                  : R$ {inss:.2f}\n\
(-) SINDICATO (03%)             : R$ {sindicato:.2f}\n\
FGTS (11%)                      : R$ {fgts:.2f}\n\
Total de descontos              : R$ {total_desc:.2f}\n\
Salário Liquido                 : R$ {salario_liquido:.2f}')