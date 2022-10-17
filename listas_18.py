"""18 - Sua organização acaba de contratar um estagiário para trabalhar no Suporte
 de Informática, com a intenção de fazer um levantamento nas sucatas 
 encontradas nesta área. A primeira tarefa dele é testar todos os cerca 
 de 200 mouses que se encontram lá, testando e anotando o estado de cada
  um deles, para verificar o que se pode aproveitar deles.
Foi requisitado que você desenvolva um programa para registrar este 
levantamento. O programa deverá receber um número indeterminado de entradas,
 cada uma contendo: um número de identificação do mouse o tipo de defeito:
necessita da esfera;
necessita de limpeza; a.necessita troca do cabo ou conector; a.quebrado ou 
inutilizado Uma identificação igual a zero encerra o programa. Ao final o
 programa deverá emitir o seguinte relatório:
Quantidade de mouses: 100

Situação                        Quantidade              Percentual
1- necessita da esfera                  40                     40%
2- necessita de limpeza                 30                     30%
3- necessita troca do cabo ou conector  15                     15%
4- quebrado ou inutilizado              15                     15%

"""

situacao = [[1," - necessita da esfera"], [2," - necessita de limpeza"],
[3," - necessita troca do cabo ou conector"],[4," - quebrado ou inutilizado"]]
cont = 0 
qtde_mouse = 0

entrada = 1

while entrada != 0: 
    entrada = int(input("Digite o código do mouse: "))
    if entrada == 0:
          break
    defeito = int(input(f"Identifique o defeito: 1 - Necessita da esfera, \
    2 - Necessita de limpeza, 3- necessita troca do cabo ou conector, 4-quebrado \
    ou inutilizado: "))
    for indice in range(len(situacao)):
        if situacao[indice][0] == defeito :
          situacao[indice].append(1)
          situacao[indice].append(entrada)
          break
   
    qtde_mouse+=1

defeitos = []

for indice in range(len(situacao)):
    total = (len(situacao[indice])-2)/2
    porc = (total / qtde_mouse) * 100
    defeitos.append([total])
    defeitos[indice].append(porc)

print(defeitos)

print(f'Quantidade de mouses: {qtde_mouse}\n\
Situação                                    Quantidade              Percentual\n\
{situacao[0][0], situacao[0][1]}            {defeitos[0][0]}    {defeitos[0][1]} \n\
{situacao[1][0], situacao[1][1]}            {defeitos[1][0]}    {defeitos[1][1]} \n\
{situacao[2][0], situacao[2][1]}      {defeitos[2][0]}    {defeitos[2][1]} \n\
{situacao[3][0], situacao[3][1]}            {defeitos[3][0]}    {defeitos[3][1]}')