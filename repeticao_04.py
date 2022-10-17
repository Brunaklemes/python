"""4 - Supondo que a população de um país A seja da ordem de 80000 habitantes com uma
 taxa anual de crescimento de 3% e que a população de B seja 200000 habitantes
 com uma taxa de crescimento de 1.5%. Faça um programa que calcule e escreva o 
 número de anos necessários para que a população do país A ultrapasse ou iguale
  a população do país B, mantidas as taxas de crescimento.
"""

pop_a = 10
pop_b = 20
ano = 0

while pop_a < pop_b:
      ano += 1
      pop_a = pop_a * 0.04 + pop_a
      pop_b = pop_b * 0.02 + pop_b

print(ano,pop_a,pop_b)