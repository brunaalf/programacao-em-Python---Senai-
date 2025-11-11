def mercado_(lista_prod,lista_valores):
    carrinho = []
    meus_valores = []
    per = input('Deseja pedir? ')
    while per  == 'sim':
        produto = int(input(f'''
                  1{lista_prod [1]} - R${lista_valores[1]}
                  2{lista_prod [2]} - R${lista_valores[2]}
                  3{lista_prod [3]} - R${lista_valores[3]}
                  4{lista_prod [4]} - R${lista_valores[4]}
                  5{lista_prod [5]}- R${lista_valores[5]}
                 '''))
        carrinho.append(lista_prod[produto])
        meus_valores.append(lista_valores[produto])
        print(carrinho)
        soma  =  sum(meus_valores)
        print('Total R$', soma)
        
        per = input('Deseja continuar? ')
        
                       
    else:
        print('Obrigada volte sempre! ')
        print('Se a compra foi efetuada vá até pagamentos! ')
        
def pagamentos(forma_pag):
    print(forma_pag) 
    escolha =  int(input('Escolha a forma de pagamento'))
    print('Sua forma de pagamento é ', forma_pag[escolha])
    


def despedir(nome):
    return f'obrigada volte sempre {nome}'


                         


    
