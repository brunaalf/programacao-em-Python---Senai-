# 1 - Faça um programa, utilizando ***while***, que mostre na tela os números de 0 a 1000.

# num = 0
# while num < 1000:
#     num = num + 1
#     print (num)


# 2 -  Faça um sistema, utilizando ***while e listas***, que permita o usuário escrever o nome de 10 pessoas e os mostre na tela.

# lista = []

# qtd = int(input("digite a quantidade de nomes até 10: "))
# if qtd <= 10: 
#  for n in range (0, qtd):
#   nomes = input('nome:')
#   lista.append(nomes)
# print ('Os nomes adicionados são:', lista)


## ***ATIVIDADE 2***

# Crie um sistema de notas alunos, com as seguintes operações:
# ***Utilize While ou for***
#  **Sistema de notas de alunos**
# - ***Visão do professor***
# - Acesso a conta com condicionais
# - 3 chances de acessar o sistema
# - Após errar 3 x mensagem que diga que a conta bloqueada (senha incorreta)
# - Inserir notas (se Senha correta)
# - Fazer a média
# - Utilize ***loops for, while, condicionais, variáveis, listas, tuplas ou dicionários…***

print ("bem vindo as nosso sistema escolar")

login_certo = "fulano@"
senha_correta = 1234

login_maquina = str(input("Digite seu login"))
senha_maquina = int(input("Digite sua senha de 4 digitos"))

if senha_maquina == senha_correta and login_maquina == login_certo:
    print ("Bem-Vindo Fulado")

else:
    for n in range (1,4):

        login_maquina = str(input("Digite seu login"))
senha_maquina = int(input("Digite sua senha de 4 digitos"))

if senha_maquina == senha_correta and login_maquina == login_certo:
    print ("Bem-Vindo Fulado") 
    senha_maquina != senha_correta and login_maquina != login_certo
    print ("senha incorreta")

    