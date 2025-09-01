#ejemplo de programa utilizandolibrerias externas como:pygame
import pygame

#inicio del juego o programa 
pygame.init()
#crear la ventana del juego
ventana=pygame.display.set_mode((400,300))
pygame.display.set_caption("mi primer juego")
#color que tenga esa ventana por ejemplo el RGB
AZUL=(0,0,255)

#CICLO
EJECUTANDO=True
while EJECUTANDO:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            EJECUTANDO=False
    ventana.fill(AZUL)
    #actualizar la pantalla
    pygame.display.flip()
pygame.quit()
