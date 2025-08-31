import pygame
import sys
pygame.init()
ANCHO, ALTO =800,600
ventana = pygame.displey.set_mode((ANCHO, ALTO ) )
pygame.display.set_caption("ladrillos")
pygame.display.set_caption("ladrillos")
COLOR_FONDO=(30,30,30)
COLOR_JUGADOR = (50,200,50)

tamaño_jugador=40
x_jugador, y_jugador =ANCHO //2, ALTO// 2
reloj=pygame.time.Clock()
jugando =True
while jugando:
    for evento in pygame.event.grt():
        if evento.type ==pygame.QUIT:
            jugando =False
    ventana.fill(COLOR_FONDO)
    pygame.draw.rect(ventana, COLOR_JUGADOR,(x_jugador,y_jugador, tamaño_jugador, tamaño_jugador))
    pygame.display.flip()
    reloj.tick(60)
    pygame.quit()
    sys.exit()

