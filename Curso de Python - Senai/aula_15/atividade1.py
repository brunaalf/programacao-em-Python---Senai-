# MANIPULAÇÃO DOS EVENTOS
# JOGO LABIRINTO

# importação do módulo pygame
import pygame

# Inicializa o Pygame
pygame.init()



# COMENTE O CÓDIGO, EXPLIQUE COM SUAS PALAVRAS O QUE ESTA OCORRENDO EM CADA ESTRUTURA DO 
# CÓDIGO E VERIFIQUE O QUE OCORRE. 
# CONSULTE A BIBLIOTECA -> https://www.pygame.org/docs/


# o que a estrutura(sintaticamente)? para que serve(contexto)? 
# são variáveis que é atribuido a largura e a altura da tela 
largura, altura = 400, 400

# variável, atribuido submódulo oferece função criar o 
# tamanho da tela
tela = pygame.display.set_mode((largura, altura))


# função que cria o título da tela
pygame.display.set_caption("Labirinto")

# variaveis para setar as cores dos objetos
preto = (0, 0, 0)
branco = (255, 255, 255)
vermelho = (255, 0, 0)

# variável  que atribui o tamanho da celula 
tamanho_celula = 40


# lista aninhada criando a estrutura do labirinto 

labirinto = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 1, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 1, 0, 1, 1, 0, 1],
    [1, 0, 1, 0, 1, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 1, 1, 1, 0, 1],
    [1, 1, 1, 1, 0, 0, 1, 0, 0, 1],
    [1, 1, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 1, 1, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]

# 2  variáveis da posição 
x, y = 1 * tamanho_celula, 1 * tamanho_celula

# variável atribuido a ela a velocidade 40
velocidade = 40


# função que cria o labirinto

def desenhar_labirinto():

    # loop atribuindo a variavel linha  
    for linha in range(len(labirinto)):
        # loop que identifica as posições dentro da lista
        # coloindo a superficie de preto se o valor for 1
        for coluna in range(len(labirinto[linha])):
            cor = preto if labirinto[linha][coluna] == 1 else branco
            
            # desenhando os quadrados do labirinto 
            # posiciona, pinta e também add o tamanho
            pygame.draw.rect(tela, cor, (coluna * tamanho_celula, linha * tamanho_celula, tamanho_celula, tamanho_celula))

# variável do loop boleana valor True
executando = True

# loop principal, loop do jogo
while executando:
    # todos os eventos estão sendo capturados pela função get()
    for evento in pygame.event.get():
        # uma condição que verifica se o o evento é do tipo QUIT
        if evento.type == pygame.QUIT:
            # a varivável atribui False
            executando = False



    # lista com as possibilidade de pressionamento do  teclado 
    teclas = pygame.key.get_pressed()
    # condição que identifica a tecla da seta a esquerda 
    if teclas[pygame.K_LEFT]:
        # variável  esta  alterando a posição após pressionar, 
        # velocidade negativa no eixo X(esquerda) a tecla
        novo_x = x - velocidade
           # após precionar a tecla da esqueda haverá uma verificação 
           # se a posição é zero o personagem avança 
        if labirinto[y // tamanho_celula][novo_x // tamanho_celula] == 0:
           
           x = novo_x
    # pressionamento  da seta para a direita        
    if teclas[pygame.K_RIGHT]:
        novo_x = x + velocidade
        if labirinto[y // tamanho_celula][novo_x // tamanho_celula] == 0:
            x = novo_x
    # pressionamento da seta para cima         
    if teclas[pygame.K_UP]:
        novo_y = y - velocidade
        if labirinto[novo_y // tamanho_celula][x // tamanho_celula] == 0:
            y = novo_y
    # pressionamento da seta para baixo        
    if teclas[pygame.K_DOWN]:
        novo_y = y + velocidade
        if labirinto[novo_y // tamanho_celula][x // tamanho_celula] == 0:
            y = novo_y

    # retorna da tela branca com o prenchimento da função fill()
    tela.fill(branco)

    # evocando a função que irá desenha as formas 
    desenhar_labirinto()
    # criando o retangulo vcermelho com a função rect do módulo draw
    pygame.draw.rect(tela,'red',(x, y, tamanho_celula, tamanho_celula))

    
    # atualização da tela com a função flip do submódulo display
    pygame.display.flip()

    # FPS quadros por segundo , 10 quadros 
    pygame.time.Clock().tick(10)

# finaliza o módulo do pygame
pygame.quit()
