#lista  Estrutura composta com mais de um dado; Pode ser interável, ou seja, percorrível

lista_vazia = []
print (lista_vazia)

#lista com valores inteiros
lista_cheia = [1,2,3]
#             0, 1, 2 ou -3, -2, -1
print (lista_cheia)

print (lista_cheia[0]) #aqui traz a valor na posição 0

#atribuindo a uma variável: 

n1 = lista_cheia[0]
n2 = lista_cheia[1]
print (n1+n2)


#Funções das Listas: nome_funçã0 (lista) 

# 1 - DIR() = Quais métodos é possivel utilizar com esta estrutura

x = 10
print (dir(x))


# 2 - LEN() = Tamanho (quantidade de valores) da Lista 

print (len(lista_cheia))


# 3 - SUM() = Irá somar os itens da lista numérica 

print (sum(lista_cheia))


#4 - MAX() = qual o maior valor da lista numerica

print (max(lista_cheia))


#5 - MIN() = qual o menor valor da lista numerica

print (min(lista_cheia))


#6 - SORTED - Organiza a lista, pode se numerica ou texto


print(sorted(lista_cheia))


#Métodos 

# 1- Append = adiciona um número no final da lista 

lista_cheia.append(100) #Irá adicionar 100 no final da lista 
print (lista_cheia)

# 2 - Insert - Adiciona um numero na lista 

lista_cheia.insert(0, 250) # Irá adicionao na posição Zero o numero 250
print (lista_cheia)


# 3 - Count - Irá contar a quantidade de determinado dado

print (lista_cheia.count(8))

# 4 - Extend - Adiciona vários dados de uma vez 

lista_cheia.extend ([10,10,2,5,1,1,1,'ola'])
print (lista_cheia)

# Adicionando dados:

lista_cheia[0] = 500
print (lista_vazia)

# Retirando dados 

# 1 - Remove = remove um dado, através do valor 

lista_cheia.remove(500)
print (lista_cheia)

# 2 - Del = deleta de dentro para fora, através da posição 

del lista_cheia[0]
print (lista_cheia)

# 3 - Pop - pode remover com posição ou com valor 

lista_cheia.pop(0) # está removendo a posição 0; Se estiver sem a menção da posição, irá remover a ultima posição
lista_cheia() 
print(lista_cheia)


lista_cheia.sort  #irá ordenar do menor para maior


lista_cheia.sort(reverse= True) #irá ordenar a lista do maior para menor
print (lista_cheia)


#Copy  - cópia da lista 

x = lista_cheia.copy()
print(x)

#Index - verifica a posição do Valor na lista 

indice = lista_cheia.index(410)
print (indice)

#Split = transforma os caracteres em uma lista 

x = "texto"
print (x.split())

#Clear = Limpa os dados da Lista 

lista_cheia.clear()
print(lista_cheia)

# range() com o list()

lista_0_10 = list(range(11))
print(lista_0_10)
lista_1_10 = list(range(1,11))
print(lista_1_10)
lista_1_10_2 = list(range(1,11,3))
print(lista_1_10_2)