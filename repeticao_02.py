"""2 - Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual
 ao nome do usuário, mostrando uma mensagem de erro e voltando a pedir as informações.
"""

usuario = input("Digite o usuário: ")
senha = input("Digite sua senha: ")

while usuario == senha:
    print("Você digitou algo errado!Tente novamente")
    usuario = input("Digite o usuário: ")
    senha = input("Digite sua senha: ")
print("Você está logado!")