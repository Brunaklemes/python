"""5 - Altere o programa anterior permitindo ao usuário informar as populações e as taxas 
de crescimento iniciais. Valide a entrada e permita repetir a operação.
"""
while True:
    pop_a = int(input('Qual é a quantidade da população "A": '))
    pop_b = int(input('Qual é a quantidade da população "B": '))
    taxa_a = float(input('Taxa de crescimento da população "A": '))
    taxa_b = float(input('Taxa de crescimento da população "B": '))
    taxa_a = taxa_a / 100
    taxa_b = taxa_b / 100
    ano = 0
    while pop_a < pop_b:
        ano += 1
        pop_a = pop_a * taxa_a + pop_a
        pop_b = pop_b * taxa_b + pop_b
    print(ano,pop_a,pop_b)
    if pop_a >= pop_b:
        continuar = input('Deseja informar novos valores? S - Sim ou N - Não: ')
        continuar = continuar.upper()
        if continuar == 'S':
            continue
        else:
            print('Fim')
            break
