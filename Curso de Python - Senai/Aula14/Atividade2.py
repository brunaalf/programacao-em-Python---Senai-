import pygame


pygame.init()


tela  = pygame.display.set_mode((300,200))
pygame.display.set_caption('titulo')
run = True


while run:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            run  = False


    tela.fill('purple')
    pygame.draw.ellipse(tela,'white',(145,95,70,70))
    pygame.draw.rect(tela,'green',(100,75,20,20))
    pygame.draw.circle(tela,'pink',(20,20),10)
    # pygame.draw.rect(tela,'blue',(150,100,250,250))
    
    
    pygame.display.flip()




pygame.quit()  