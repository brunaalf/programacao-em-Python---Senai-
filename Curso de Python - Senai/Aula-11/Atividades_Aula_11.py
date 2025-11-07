# Exercício 1:
# Peça ao usuário para inserir um número e manipule a exceção caso ele insira algo que não seja um número inteiro.

# try:
#     num = int(input("digite um numero"))
#     print (num)
# except TypeError as erro:
#     print ("Tipo de ativo diferente",erro)
# except ValueError as erro:
#     print ("Valor não declarado",erro)
# except SyntaxError as erro:
#     print ("erro de syntax",erro)
  



# Exercício 2:
# Peça ao usuário para inserir dois números e realize uma operação de divisão. Manipule a exceção caso ocorra um erro na operação  -  ZeroDivisionError.

# try:

#     num1 = int(input("Digite um numero"))
#     num2 = int(input("Digite outro número"))

#     result = num1/num2 
#     print (result)

# except TypeError as erro:
#     print ("Tipo de valor errado ao solicitado", erro)

# except ValueError as erro:
#     print ("Valor incorreto")

# except SyntaxError as erro:
#     print ("Erro na digitação")

# except ZeroDivisionError as erro:
#     print ("não tente dividir por zero")

# else: 
#     print ("Deu erro e não sei porque")
# finally: 
#     print ("fim de carregamento")


# Exercício 3:
# Crie uma lista e um índice como entrada e retorne o índice. Manipule a exceção caso o índice seja inválido(caso imprima um indice que não exista na lista).
try:
    def lista():
     indice = [1,2,3,4,5]

except TypeError as erro:
    print ("errooooooo")

