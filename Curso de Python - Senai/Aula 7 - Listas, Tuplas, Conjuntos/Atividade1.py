# Exercício 0:** Escreva um programa que use a função `range()` para gerar os números pares de 2 a 20 e, em seguida, imprima cada número.

lista_teste = list(range(2,21,2))

print (lista_teste)


# Exercício 1:** Crie uma lista chamada numeros que contenha os números inteiros de 1 a 10 e imprima-a na tela.

lista_1_20 = list(range(1,11))
print (lista_1_20)


# Exercício 2:** Acesse e imprima o terceiro elemento da lista `numeros`.

numeros = [10,20,30,5]
print (numeros[2])

# Exercício 3:** Adicione o número 9 à lista `numeros` e imprima a lista atualizada.

numeros.append(9)
print (numeros)

# <!-- **Exercício 4:** Remova o número 5 da lista `numeros` e imprima a lista resultante.

numeros.remove(5)
print (numeros)

# **Exercício 5:** Crie uma lista chamada carros contendo três nomes de carros diferentes. Em seguida, concatene essa lista com a lista `numeros` e imprima o resultado. --> -->

lista_carros = ["Corsa,Celta,Idea"]
print (lista_carros + numeros)

print(numeros, lista_carros)

numeros += (lista_carros)

print(numeros)

