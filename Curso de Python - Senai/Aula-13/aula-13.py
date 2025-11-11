import meu_modulo as md


def mercado():
    nome =  input('nome: ')
    lista_produtos = ['','a','b','c','d','e']
    valores = [0,55.0,60.8,12.88,9.52,5.44]
    md.mercado_(lista_produtos,valores)
    lista_pag = ['', '1 - PIX', '2 - CC', '3 - CD']
    md.pagamentos(lista_pag)
    print(md.despedir(nome))


mercado()  