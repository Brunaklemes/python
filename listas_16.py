'''
16 - Utilize uma lista para resolver o problema a seguir. Uma empresa paga seus
vendedores com base em comissões. O vendedor recebe $200 por semana mais 9
por cento de suas vendas brutas daquela semana. Por exemplo, um vendedor que
teve vendas brutas de $3000 em uma semana recebe $200 mais 9 por cento de $3000,
ou seja, um total de $470.
Escreva um programa (usando um array de contadores)
que determine quantos vendedores receberam salários nos seguintes intervalos
de valores:
$200 - $299
$300 - $399
$400 - $499
$500 - $599
$600 - $699
$700 - $799
$800 - $899
$900 - $999
$1000 em diante
Desafio: Crie ma fórmula para chegar na posição da lista a partir do salário,
sem fazer vários ifs aninhados.
'''
valores = [[200,299], [300,399], [400,499], [500,599], [600,699], [700,799], [800,899], [900,999],[1000,+1000]]
fixo = 200
venda = 0
comissao = 0.09
valor_salario = []
while venda != -1:
    venda = float(input('Digite o total das vendas: '))
    if not venda == -1:
        venda = venda * comissao + fixo
        valor_salario.append(venda)

cont_salarios = 0
cont_valores = 0
while cont_salarios < len(valor_salario):
    for indice in valores:
        if valor_salario[cont_salarios] <= valores[cont_valores][1]:
           valores[cont_valores].append(1)
           break
        if valor_salario[cont_salarios] > valores[8][0]:
            valores[8].append(1)
            break
        cont_valores += 1
    cont_salarios += 1
    cont_valores = 0
print(valores)

limite = len(valores)
cont_indice = 0
cont_indice2 = 1
cont_resultado = 0
while cont_resultado < limite:
    total = len(valores[cont_indice])-2
    print(f'A empresa deverá pagar a {total} vendedores o entre {valores[cont_indice][0]},00 \
e {valores[cont_indice][1]},00')
    cont_indice+=1
    cont_resultado+=1