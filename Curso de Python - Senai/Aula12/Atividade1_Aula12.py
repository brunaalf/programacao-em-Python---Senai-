## Exercícios com funções:

#variáveis locais, globais e parâmetros

# ***1****CRIE UMA FUNÇÃO PARA COMPARAR 2 NÚMEROS (par ou impar). UTILIZE VARIÁVEIS LOCAIS.***

# num1 = int(input("Digite um número: "))
# num2 = int(input("Digite outro número: "))

# def compara():
    
#     if num1 % 2 == 0:
#         print (f"O primeiro numero digitado {num1}, é PAR")
#     else: 
#         print (f"O primeiro numero digitado {num1}, é ÍMPAR")
        
#     if num2 % 2 == 0:
#         print (f"O segundo numero digitado {num2}, é PAR")
#     else: 
#         print (f"O segundo numero digitado {num2}, é PAR")

# compara()
               

# ***2****CRIE UMA FUNÇÃO PARA MULTIPLICAR 3 NUMEROS.***

# var1 = int(input("Digite o primeiro número"))
# var2 = int(input("Digite o segundo número"))
# var3 = int(input("Digite o terceiro"))

# def mult ():
#     result = (var1 * var2 *var3) 
#     print (f"O resultado da Multiplicação é: {result}")

# mult()

# ***3***CRIE UMA FUNÇÃO PARA DESCOBRIR O VALOR ELEVADO DE UM NÚMERO.***


# ***4***CRIE UMA FUNÇÃO PARA MOSTRAR UMA MENSAGEM PERSONALIZADA NA TELA, SE O USUÁRIO  DIGITAR, 18 ANOS.***

# idade = int(input("Digite sua idade"))

# def dezoito(): 
#     if idade == 18: 
#         print ("Uau, agora você já é MAIOR DE IDADE")
#     elif idade < 18: 
#         print ("Você aida é menor")
#     else: 
#         print ("Você é macaco velho")

# dezoito()


# ***5***DESENVOLVA UMA FUNÇÃO PARA DESCOBRIR A IDADE DE UMA PESSOA.***

# data = int(input("Digite o ano que você nasceu"))

# def idade (): 
#     ano = 2025 - data
#     print (f"Você tem {ano} anos")
# idade ()

# ***6****DESENVOLVA UMA FUNÇÃO PARA VER SE O BRASIL GANHOU A COPA DE 1999.***

# ano = int(input(f"Qual ano o Brasil ganhou uma copa?\n1 - 1998 \n2 - 1999 \n3 - 2000: "))

# lista = [1998, 1999, 2000]
# opções = [1,2,3]

# def result ():
#     if ano == 2:
#         print ("Acertou")
#     else: 
#         print ("errou feio")
# result()

# ***7***DESENVOLVA UM SISTEMA DE RESTAURANTE, ONDE O CLIENTE TEM OPÇÃO DE ESCOLHER ENTRE SALADA, MACARRONADA, SANDUICHE, SORVETE.***  

# ***1 - Função -  cumprimentar o cliente***

# ***2 - Função - restaurante***

# ***3 - Sugestão utilize listas  e loops***



def cumprimento (): 
    print ("Bem vindo ao nosso restaurante COMA-SEM-PARAR")
cumprimento()

def restaurante():
    comida = int(input("\nEscolha o seu pedido, \n 1 - salada,\n 2 - macarronada,\n 3 - sanduiche,\n 4 - sorvete ==> "))
    lista = ["salada", "macarronada", "sanduiche", "sorvete"]
    if comida in [1, 2, 3, 4]:
        print (f'Ok, você escolheu a opção, {lista[comida-1]}')

    confirma = int(input("Gostaria de confirmar seu pedido? 1 - sim, 2 - não ==> "))
    if confirma == 1: 
        print ("Ok, pedido realizado")
    elif confirma == 2: 
        print ("Certo, refaça seu pedido! VOLTE SEMPRE!")

    while confirma == 2: 
        cumprimento ()
        restaurante()
        break

restaurante()
    
    