# ## Desafio 1
#-----------------------------------------------------------
# VOCÊ É UM DEV E PRECISA CRIAR UM SISTEMA PARA UMA ESCOLA. 
# SISTEMA DE NOTAS DE ALUNOS QUE MOSTRE COM ESTATISTICA A MODA E A MEDIA E DESVIO DE PADRÃO, DAS NOTAS DE ALUNOS DE UM COLÉGIO, ALÉM DE MOSTRAR MENOR E A  MAIOR NOTA, 
# SEPARE EM FUNÇÕES DIFERENTES 
# 1 -  ***VOCÊ CRIAR SEUS PRÓPRIOS MÓDULOS***
# 2 - ***OU USAR STATISTICS *****
#-----------------------------------------------------------

import statistics as st

lista_notas = []
notas = []
notas = int(input("Digite a nota: "))
lista_notas.append(notas)
resp = input("Deseja inserir outra nota?")

while resp == "sim": 
    notas = int(input("Digite a nota: "))
    lista_notas.append(notas)
    resp = input("Deseja inserir outra nota?: ")


def media ():
    media = st.mean(lista_notas)
    print ("A média das notas é de:", {media})


def moda(): 
   moda = st.mode(lista_notas)
   print ("A moda das notas é de:", {moda})


def desvio():
    desvio = st.pstdev(lista_notas)
    print ("O Desvio Padrão das Notas foi de:", {desvio})


if resp == "não":
    print (lista_notas)
    moda()
    media()
    desvio()
