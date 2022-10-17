"""23 - Uma fruteira está vendendo frutas com a seguinte tabela de preços:
                      Até 5 Kg           Acima de 5 Kg
Morango         R$ 2,50 por Kg          R$ 2,20 por Kg
Maçã            R$ 1,80 por Kg          R$ 1,50 por Kg
Se o cliente comprar mais de 8 Kg em frutas ou o valor total da compra ultrapassar 
R$ 25,00, receberá ainda um desconto de 10% sobre este total. Escreva um algoritmo 
para ler a quantidade (em Kg) de morangos e a quantidade (em Kg) de maças adquiridas
 e escreva o valor a ser pago pelo cliente.
"""
maca = int(input('Quantos quilos de MAÇA? '))
morango = int(input('Quantos quilos de MORANGO? '))

if maca <= 5:
    valor_maca = maca * 1.8
else:
    valor_maca = maca * 1.5
if morango <= 5:
    valor_morango = morango * 2.5
else:
    valor_morango = morango * 2.2

total_quilos = morango + maca
total_valor = valor_maca + valor_morango
print(total_valor)
if total_quilos > 8 or total_valor > 25:
    valor_final = total_valor - (total_valor * 0.1)
    print(f'O valor a pagar com desconto é R$ {valor_final:.2f}')
else:
    print(f'O valor a pagar é R$ {total_valor:.2f}')
