"""
20 - Faça um Programa que leia 2 números e em seguida pergunte ao usuário qual operação
 ele deseja realizar. O resultado da operação deve ser acompanhado de uma frase que 
 diga se o número é:
par ou ímpar;
positivo ou negativo;
inteiro ou decimal.
"""


numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))

operacao = input("Qual operação quer utilizar? +(SOMA), * (MULTIPLICAÇÃO), - (SUBTRAÇÃO), / (DIVISÃO): ")

if operacao == "+":
    resultado = numero1 + numero2
elif operacao == "*":
    resultado = numero1 * numero2
elif operacao == "-":
    resultado =  numero1 - numero2
else:
    resultado =  numero1 / numero2

if resultado % 2 == 0:
    par_impar = "par"
else:
    par_impar = "ímpar" 

if resultado % 1 == 0:
    int_float = "inteiro"
else:
    int_float = "decimal"

if resultado <0:
    pos_neg = "negativo"
else:
    pos_neg = "positivo"

print(f'O {resultado:.2f} é um número {par_impar}, {int_float} e {pos_neg}.')