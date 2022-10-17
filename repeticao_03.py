"""3 - Faça um programa que leia e valide as seguintes informações:
Nome: maior que 3 caracteres;
Idade: entre 0 e 150;
Salário: maior que zero;
Sexo: 'f' ou 'm';
Estado Civil: 's', 'c', 'v', 'd';
"""
nome = input('Digite um nome: ')
idade = int(input('Digite uma idade: '))
salario = float(input('Digite o salário: '))
sexo = input('Digite o sexo - f (feminino) ou m (masculino): ')
estado_civil = input('Digite o estado civil - s (solteiro), c (casado), v (viuvo) ou d (divorciado): ')

qtde_letras = len(nome)
sexo, estado_civil = sexo.lower(), estado_civil.lower()

while True:
    if qtde_letras <= 3:
        nome = input('Digitou um nome muito pequeno, digite novamente: ')
        qtde_letras = len(nome)
    elif idade < 0 or idade > 150:
        idade = int(input('Digitou a idade errada, digite novamente: '))
    elif salario < 0:
        salario = float(input('Digitou o salario errado, digite novamente: '))
    elif sexo != 'f' and sexo != 'm':
        sexo = input('Digitou o sexo errado, digite novamente - f (feminino) ou m (masculino): ')
        sexo = sexo.lower()
    elif estado_civil != 's' and estado_civil != 'c' and estado_civil != 'v' and estado_civil != 'd':
        estado_civil = input('Digitou errado, digite novamente o estado civil - s (solteiro), c (casado), v (viuvo) ou d (divorciado): ')
        estado_civil = estado_civil.lower()
    else:
        print(f'Todos os dados estão corretos: {nome} / {idade} / {salario} / {sexo} / {estado_civil}')
        break