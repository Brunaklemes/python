'''
24 - O Hipermercado Tabajara está com uma promoção de carnes que é imperdível. Confira:
                      Até 5 Kg           Acima de 5 Kg
File Duplo      R$ 4,90 por Kg          R$ 5,80 por Kg
Alcatra         R$ 5,90 por Kg          R$ 6,80 por Kg
Picanha         R$ 6,90 por Kg          R$ 7,80 por Kg
Para atender a todos os clientes, cada cliente poderá levar apenas um dos tipos de 
carne da promoção, porém não há limites para a quantidade de carne por cliente. Se
compra for feita no cartão Tabajara o cliente receberá ainda um desconto de 5% sobre
o total da compra. Escreva um programa que peça o tipo e a quantidade de carne 
comprada pelo usuário e gere um cupom fiscal, contendo as informações da compra:
tipo e quantidade de carne, preço total, tipo de pagamento, valor do desconto e
valor a pagar.

'''
carne = input("Qual carne deseja comprar: F - Filé Duplo, A - Alcatra ou P - Picanha? ")
quantidade = int(input("Quantos kilos? "))
pagamento = input("Será pago no cartão Tabajara? S-Sim ou N-Não: ")
carne,pagamento =carne.upper(), pagamento.upper()

if carne == "F":
    tipo = "Filé Duplo"
    if quantidade <= 5: 
        valor = quantidade * 4.9
    else:
        valor = quantidade * 5.8
elif carne == "A":
    tipo = "Alcatra"
    if quantidade <= 5: 
        valor = quantidade * 5.9
    else:
        valor = quantidade * 6.8
elif carne == "P":
    tipo = "Picanha"
    if quantidade <= 5: 
        valor = quantidade * 6.9
    else:
        valor = quantidade * 7.8
else:
    print("Você digitou um tipo inválido!")

if pagamento == "S":
    desconto = valor*0.05
    valor_final= valor - desconto
    print (f"Será comprada a carne {tipo}, \
{quantidade} kg, o valor é de R$ {valor:.2f}, será aplicado o desconto de R$ {desconto:.2f} \
e o valor a pagar será de R$ {valor_final:.2f}.")
else: 
    print (f"Será comprada a carne {tipo}, \
{quantidade} kg, valor a pagar de R$ {valor:.2f}, sem desconto.")
