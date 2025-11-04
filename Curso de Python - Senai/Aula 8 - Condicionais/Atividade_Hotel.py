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
quantidade =  int(input('Quantidade pessoas: '))

dados = {
'nomes':[],
'idades':[]
}


lista_quartos  =  ['', 'simples', 'duplo', 'luxo']
valores_quartos = [0, 100,150,250]


if quantidade == 1:
    nome  =  input('Nome:')
    idade = int(input('Idade: '))
    dados['nomes'].append(nome)
    dados['idades'].append(idade)
    
    

    escolha =  int(input(f'''
                    1 - {lista_quartos[1]} R$ {float(valores_quartos[1])}
                    2 - {lista_quartos[2]} R$ {float(valores_quartos[2])}
                    3 - {lista_quartos[3]} R$ {float(valores_quartos[3])}               
                    '''))
    
    print('O hospede', nome, 'escolheu o quarto: ', lista_quartos[escolha])
    quantidade_dias =  int(input('Dias: '))
    calculo = quantidade_dias * valores_quartos[escolha]
    print(f'R$, {calculo:.2f}')
    print('Quantidade de dias do hospede', nome, '-> ', quantidade_dias)

elif quantidade == 2:
    nome1  =  input('Nome:')
    idade = int(input('Idade: '))

    nome2  =  input('Nome:')
    idade = int(input('Idade: '))

    escolha =  int(input(f'''
                    Escolha de quarto hospede{nome1}     
                    1 - {lista_quartos[1]} R$ {float(valores_quartos[1])}
                    2 - {lista_quartos[2]} R$ {float(valores_quartos[2])}
                    3 - {lista_quartos[3]} R$ {float(valores_quartos[3])}               
                    '''))
    
    print('O hospede', nome1, 'escolheu o quarto: ', lista_quartos[escolha])
    quantidade_dias =  int(input('Dias: '))
    calculo = quantidade_dias * valores_quartos[escolha]
    print(f'R$, {calculo:.2f}')
    print('Quantidade de dias do hospede', nome1, '-> ', quantidade_dias)



    escolha =  int(input(f'''
                    1 - {lista_quartos[1]} R$ {float(valores_quartos[1])}
                    2 - {lista_quartos[2]} R$ {float(valores_quartos[2])}
                    3 - {lista_quartos[3]} R$ {float(valores_quartos[3])}               
                    '''))
    
    print('O hospede', nome2, 'escolheu o quarto: ', lista_quartos[escolha])
    quantidade_dias =  int(input('Dias: '))
    calculo = quantidade_dias * valores_quartos[escolha]
    print(f'R$, {calculo:.2f}')
    print('Quantidade de dias do hospede', nome2, '-> ', quantidade_dias)


elif quantidade == 3:

    nome1  =  input('Nome:')
    idade = int(input('Idade: '))
    escolha =  int(input(f'''
                    1 - {lista_quartos[1]} R$ {float(valores_quartos[1])}
                    2 - {lista_quartos[2]} R$ {float(valores_quartos[2])}
                    3 - {lista_quartos[3]} R$ {float(valores_quartos[3])}               
                    '''))
    
    print('O hospede', nome1, 'escolheu o quarto: ', lista_quartos[escolha])
    quantidade_dias =  int(input('Dias: '))
    calculo = quantidade_dias * valores_quartos[escolha]
    print(f'R$, {calculo:.2f}')
    print('Quantidade de dias do hospede', nome1, '-> ', quantidade_dias)


    nome2  =  input('Nome:')
    idade = int(input('Idade: '))
    escolha =  int(input(f'''
                    1 - {lista_quartos[1]} R$ {float(valores_quartos[1])}
                    2 - {lista_quartos[2]} R$ {float(valores_quartos[2])}
                    3 - {lista_quartos[3]} R$ {float(valores_quartos[3])}               
                    '''))
    
    print('O hospede', nome2, 'escolheu o quarto: ', lista_quartos[escolha])
    quantidade_dias =  int(input('Dias: '))
    calculo = quantidade_dias * valores_quartos[escolha]
    print(f'R$, {calculo:.2f}')
    print('Quantidade de dias do hospede', nome2, '-> ', quantidade_dias)


    nome3  =  input('Nome:')
    idade = int(input('Idade: '))
    escolha =  int(input(f'''
                    1 - {lista_quartos[1]} R$ {float(valores_quartos[1])}
                    2 - {lista_quartos[2]} R$ {float(valores_quartos[2])}
                    3 - {lista_quartos[3]} R$ {float(valores_quartos[3])}               
                    '''))
    
    print('O hospede', nome3, 'escolheu o quarto: ', lista_quartos[escolha])
    quantidade_dias =  int(input('Dias: '))
    calculo = quantidade_dias * valores_quartos[escolha]
    print(f'R$, {calculo:.2f}')
    print('Quantidade de dias do hospede', nome3, '-> ', quantidade_dias)



else:
    print('Para mais hospedes chame o coord.')                




