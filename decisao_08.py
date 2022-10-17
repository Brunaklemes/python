"""
8 - As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores 
e lhe contraram para desenvolver o programa que calculará os reajustes.
Faça um programa que recebe o salário de um colaborador e o reajuste segundo o
 seguinte critério, baseado no salário atual:
salários até R$ 280,00 (incluindo) : aumento de 20%
salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe
 na tela:
o salário antes do reajuste;
o percentual de aumento aplicado;
o valor do aumento;
o novo salário, após o aumento.
"""
salario_atual = float(input("Digite seu salário atual: "))

if salario_atual <= 280:
    aumento = salario_atual * 0.20
    salario_novo = salario_atual + aumento
    print(f'O salario atual é {salario_atual:.2f}, o aumento aplicado será de 20% sendo {aumento:.2f},\
 o valor do novo salário será {salario_novo:.2f}')

elif salario_atual >280 and salario_atual<= 700:
    aumento = salario_atual * 0.15
    salario_novo = salario_atual + aumento
    print(f'O salario atual é {salario_atual:.2f}, o aumento aplicado será de 15% sendo {aumento:.2f},\
 o valor do novo salário será {salario_novo:.2f}')

elif salario_atual >700 and salario_atual <= 1500:
    aumento = salario_atual * 0.10
    salario_novo = salario_atual + aumento
    print(f'O salario atual é {salario_atual:.2f}, o aumento aplicado será de 10% sendo {aumento:.2f},\
 o valor do novo salário será {salario_novo:.2f}')

else:
    aumento = salario_atual * 0.05
    salario_novo = salario_atual + aumento
    print(f'O salario atual é {salario_atual:.2f}, o aumento aplicado será de 5% sendo {aumento:.2f},\
 valor do novo salário será {salario_novo:.2f}')