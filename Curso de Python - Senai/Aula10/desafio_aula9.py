# - ***Desafio 1:  Condicionais***

# ***Sistema de Reservas de Hotel:***

# ***Você foi contratado(a) para desenvolver uma parte do sistema de um hotel. 
# O objetivo é criar um sistema que gerencie reservas de quartos e o pagamento das diárias***.

# - *Cadastro de Cliente:*

# *O sistema deve permitir que o usuário "cadastre" o nome e a idade de até 3 clientes.*

# - *Reservas de Quartos:*

# ***O sistema deve oferecer 3 tipos de quartos:*** 

# ***"Simples", "Duplo" e "Luxo".***

# ***Cada cliente deve escolher um quarto para sua estadia.
# O preço da diária varia conforme o tipo de quarto:
# Simples: R$ 100,00 por dia.
# Duplo: R$ 150,00 por dia.
# Luxo: R$ 250,00 por dia.***

# - ***Cálculo da Estadia:***

# ***O usuário deve informar quantos dias cada cliente ficará no hotel.
# O sistema deve calcular o valor total da estadia para cada cliente, considerando o tipo de quarto e a quantidade de dias.***

# Exemplo: 

#  ***valor_cliente3 = preco_duplo * cliente3_dias***

# *Pagamento:*

# *O sistema deve exibir o valor total a ser pago por cada cliente.

print ("bem vindo ao nosso site. Faça uma reserva agora!")

cliente1_nome = str(input("Digite seu nome"))
cliente1_idade = int(input("Digite sua idade"))
cliente1 = dict(idade1 = cliente1_idade, nome1 = cliente1_nome)

cliente2_nome = str(input("Digite seu nome"))
cliente2_idade = int(input("Digite sua idade"))
cliente2 = dict(idade2 = cliente2_idade, nome2 = cliente2_nome)

cliente3_nome = str(input("Digite seu nome"))
cliente3_idade = int(input("Digite sua idade"))
cliente3 = dict(idade3 = cliente3_idade, nome3 = cliente3_nome)

print (cliente1)