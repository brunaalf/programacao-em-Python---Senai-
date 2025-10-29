### 1 - Crie um programa para efetuar a leitura de um número inteiro e apresentar o resultado do quadrado deste número.

numero1 = int(input("Digite o número para ver o seu quadrado :"))
resultado = numero1 ** 2

print (resultado)

### 2 - Crie duas variáveis para armazenar seu primeiro nome e sobrenome. Em seguida, concatene-as para formar seu nome completo e exiba o resultado.

nome = str(input("Digite seu nome: "))
sobrenome = str(input("Digite seu sobrenome: "))

print (nome, sobrenome)

### 3 - Peça ao usuário para digitar dois números inteiros e armazene-os em variáveis. Realize a concatenação desses números como strings e exiba o resultado.
num1 = int(input("Digite um número"))
num2 = int(input("Digite outro numero"))

var1 = str(num1)
var2 = str(num2)

print (var1 + var2)

print (type(var1))

### 4 - Crie uma variável para armazenar a palavra "Python". Em seguida, adicione um número inteiro ao final da palavra usando a concatenação e exiba o resultado.
variavel1 = "python"

print (variavel1, 1)

### 5 - Declare uma variável contendo uma frase. Em seguida, peça ao usuário para digitar uma palavra e concatene essa palavra no final da frase. Exiba o resultado.

frase = "o céu é azul"

nova_frase = str(input("Digite uma nova frase"))

print (frase, nova_frase)
