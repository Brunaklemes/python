"""14 - Faça um Programa que peça uma data no formato dd/mm/aaaa e determine se a mesma é
 uma data válida.
"""
dia = int(input("Digite o dia: "))
mes = int(input("Digite o mês: "))
ano = int(input("Digite o ano: "))

if dia >=1 and dia <= 31 and mes >= 1 and mes <=12 and ano > 0 and ano < 10000:
    print("Está data é válida")
else:
    print("Data inválida!")