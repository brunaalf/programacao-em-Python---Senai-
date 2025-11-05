import random 


print('sistema jogos: 🎮🕹️')

opcao = input(
'''
Escolha o jogo 
1 - Adivinhe o número 🔢❓
2 - Charadas 📜❓
3 - Pedra - Papel -  Tesoura 🧻🪨✂️

''')

if opcao == '1':
    print('DIVINHE O NÚMERO: 🔢❓ ')
    numero = random.randrange(1,10)
    escolha1 =  int(input('ecolha um número de 1 à 2000 --> '))

    if numero == escolha1:
        print('Você ganhou o jogo!🫵 😁 ')
        print('O numero aleatrorio é ', numero)
    else:
        print('Errou feio! ☠️🧐')    
        print('O numero aleatrorio é ', numero)

elif opcao == '2':  
    print('Charadas! 📜❓')

    perguntas =[
    'O que é o que é? Quanto mais se tira, maior fica?',
    'Por que o livro foi ao médico?',
    'O que é o que é que tem dentes, mas não morde?',
    'Por que o computador foi preso?',
    'O que é o que é que cai em pé e corre deitado?',
    'O que é um pontinho vermelho no jardim?',
    'O que o tomate foi fazer no banco?',
    'O que é o que é que tem asa, mas não voa, e canta sem ter boca?',
    'Por que o lápis se deu mal na prova?',
    'O que é o que é que quanto mais quente fica, mais frio deixa o ambiente?'
    ]

    respostas = [
    'Um buraco!',
    'muitas “histórias” pra contar!',
    'O pente!',
    'ele executou um programa!', 
    'A chuva!',
    'Uma formiga com batom!',
    'Tirar extrato!',
    'O ventilador!', 
    'Porque estava sem ponta!',
    'O ar-condicionado!']

    pergunta_escolhida =  random.choice(perguntas)
    print(pergunta_escolhida)
    escolha2  =  int(input(f'''
    0 - {respostas[0]}
    1 - {respostas[1]}
    2 - {respostas[2]}
    3 - {respostas[3]}
    4 - {respostas[4]}
    5 - {respostas[5]}
    6 - {respostas[6]}
    7 - {respostas[7]}
    8 - {respostas[8]}
    9 - {respostas[9]}
    '''))

    indice_pergunta  =  perguntas.index(pergunta_escolhida)


    if indice_pergunta  == escolha2:
        print('Acertou em cheio 😍😘💕👌🙂!!!')
        print('Você ganhou um 🌽🌽🌽🌽🌽')
    else:
        print('ERROU FEIO!🎃🎃😝😵‍💫😒😒😟😤🤡🤡🤡')  
        print('Pague R$ 1000.00 🧐☠️😈')  
elif opcao == '3':

    print('🧻 🪨 ✂️')

    ppt_maquina  =  ['🧻','🪨','✂️']
    ppt_jogador  =  ['🧻','🪨','✂️']

    aleatorio = random.choice(ppt_maquina)

    escolha  =  int(input('''
    0 - 🧻
    1 - 🪨
    2 - ✂️
    '''))

    if aleatorio == ppt_jogador[escolha]:
        print('EMPATE!')
        print('A maquina escolheu', aleatorio)
        print('Você escolheu', ppt_jogador[escolha])

    elif aleatorio == '🧻'  and   ppt_jogador[escolha] == '🪨':
        print('O computador ganhou!')
        print('A maquina escolheu', aleatorio)
        print('Você escolheu', ppt_jogador[escolha])    


    elif aleatorio == '🪨' and  ppt_jogador[escolha] == '✂️':
        print('O computador ganhou!')
        print('A maquina escolheu', aleatorio)
        print('Você escolheu', ppt_jogador[escolha]) 


    elif aleatorio == '✂️'  and   ppt_jogador[escolha] == '🧻':
        print('O computador ganhou!')
        print('A maquina escolheu', aleatorio)
        print('Você escolheu', ppt_jogador[escolha]) 




    elif  ppt_jogador[escolha] == '🧻'  and  aleatorio == '🪨':
        print('Você ganhou!')
        print('A maquina escolheu', aleatorio)
        print('Você escolheu', ppt_jogador[escolha])    

    elif ppt_jogador[escolha] == '🪨'  and   aleatorio == '✂️':
        print('Você ganhou!')
        print('A maquina escolheu', aleatorio)
        print('Você escolheu', ppt_jogador[escolha]) 


    elif ppt_jogador[escolha] == '✂️'  and   aleatorio  == '🧻':
        print('Você ganhou!')
        print('A maquina escolheu', aleatorio)
        print('Você escolheu', ppt_jogador[escolha]) 

else:
    print('Escolha algo válido!!!')
            
