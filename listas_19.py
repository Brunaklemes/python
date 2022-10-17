"""
19 - Após reuniões envolvendo a diretoria executiva, a diretoria financeira e
 os representantes do sindicato laboral, chegou-se a seguinte forma de cálculo:
a.Cada funcionário receberá o equivalente a 20% do seu salário bruto de
 dezembro; a.O piso do abono será de 100 reais, isto é, aqueles funcionários
  cujo salário for muito baixo, recebem este valor mínimo; Neste momento, não
   se deve ter nenhuma preocupação com colaboradores com tempo menor de casa, 
   descontos, impostos ou outras particularidades. Seu programa deverá permitir
    a digitação do salário de um número indefinido (desconhecido) de salários. 
    Um valor de salário igual a 0 (zero) encerra a digitação. Após a entrada
     de todos os dados o programa deverá calcular o valor do abono concedido
      a cada colaborador, de acordo com a regra definida acima. Ao final, o 
      programa deverá apresentar:
O salário de cada funcionário, juntamente com o valor do abono;
O número total de funcionário processados;
O valor total a ser gasto com o pagamento do abono;
O número de funcionário que receberá o valor mínimo de 100 reais;
O maior valor pago como abono; A tela abaixo é um exemplo de execução do programa,
 apenas para fins ilustrativos. Os valores podem mudar a cada execução do programa.
Projeção de Gastos com Abono
============================ 
 
Salário: 1000
Salário: 300
Salário: 500
Salário: 100
Salário: 4500
Salário: 0
 
Salário    - Abono     
R$ 1000.00 - R$  200.00
R$  300.00 - R$  100.00
R$  500.00 - R$  100.00
R$  100.00 - R$  100.00
R$ 4500.00 - R$  900.00
 
Foram processados 5 colaboradores
Total gasto com abonos: R$ 1400.00
Valor mínimo pago a 3 colaboradores
Maior valor de abono pago: R$ 900.00

"""
salario, todos_salarios = -1, []
while salario != 0:
      salario = float(input('Digite o valor do salário: '))
      if salario == 0:
            break
      todos_salarios.append([salario])
cont, abono_fixo, fixo_recebidos, abono_total = 0, 100.0, 0, 0

for indice in todos_salarios:
      if todos_salarios[cont][0] < 1000:
            todos_salarios[cont].append(abono_fixo)
            fixo_recebidos += 1
            abono_total += abono_fixo
      else:
            abono_variavel = todos_salarios[cont][0] * 0.2
            todos_salarios[cont].append(abono_variavel)
            abono_total += abono_variavel
      cont += 1
abono_max = max(todos_salarios)

print()
print('Salário     -     Abono')
for indice in range(len(todos_salarios)):
      print(f'R$ {todos_salarios[indice][0]:.2f}     -     R$ {todos_salarios[indice][1]:.2f}')
print()
print(f'Foram processados {len(todos_salarios)} colaboradores\n\
Total gasto com com abonos: R$ {abono_total:.2f}\n\
Valor mínimo pago a {fixo_recebidos} colaboradores\n\
Maior valor de abono pago: R$ {abono_max[1]:.2f}')

'''
import re
a = "a           b                    c"
a = re.sub("\s+", " ", a)
'''