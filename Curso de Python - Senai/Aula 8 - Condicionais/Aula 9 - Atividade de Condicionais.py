import random 

perguntas = [
'carregue novamente', 
'O que é, o que é: que quanto mais tira, maior fica?',
'O que é, o que é: tem dentes, mas não morde?',
'O que é, o que é: passa diante do sol, e não faz sombra?',
'O que é, o que é: vive no mar, é redondo e vive dizendo "oi"?'
'O que é o que é: anda com os pés na cabeça?']

respostas = [
    ' ',
    '1 - Um buraco',
    '2 - Um pente',
    '3 - O vento',
    '4 - O polvo',
    '5 - O piolho']

per_aleatorio = random.choice(perguntas)

indice = perguntas.index(per_aleatorio)

print (f'''
Pergunta...
{per_aleatorio} ???
''')

resp_user = int(input(f'''

{respostas[1]}
{respostas[2]}
{respostas[3]}
{respostas[4]}
{respostas[5]}
>>> '''))

if indice == resp_user: 
    print ("Acertou em cheio")

else:
    print ("Errou feio")