import pygame


pygame.init()


tela  = pygame.display.set_mode((300,200))
pygame.display.set_caption('titulo')
run = True


while run:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            run  = False


    tela.fill('red')
    pygame.display.flip()



pygame.quit()    






