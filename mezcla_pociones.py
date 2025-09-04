
import pygame
import sys

def draw_potion_image(surface, x, y, color, name, font_size=24, name_y_offset=90, width=60, height=80):
    # Dibuja un matraz aforado estilizado
    # Cuerpo (ovalado)
    pygame.draw.ellipse(surface, color, (x, y+20, width, height-20))
    # Cuello (rectángulo)
    pygame.draw.rect(surface, (180, 180, 180), (x+width//2-10, y, 20, 30))
    # Borde del matraz
    pygame.draw.ellipse(surface, (80, 80, 80), (x, y+20, width, height-20), 2)
    pygame.draw.rect(surface, (80, 80, 80), (x+width//2-10, y, 20, 30), 2)
    # Línea de aforo
    pygame.draw.line(surface, (255,0,0), (x+width//2-15, y+height-10), (x+width//2+15, y+height-10), 2)
    # Nombre
    font = pygame.font.SysFont(None, font_size)
    text = font.render(name, True, (255,255,255))
    text_rect = text.get_rect(center=(x+width//2, y+name_y_offset))
    surface.blit(text, text_rect)

# Inicializar Pygame


def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption('Mezcla de Pociones')
    font = pygame.font.SysFont(None, 36)

    # Definición de niveles
    niveles = [
        {
            'ingredientes': [
                ('Agua', (100, 180, 255)),
                ('Hierba', (100, 255, 100)),
                ('Polvo mágico', (200, 100, 255)),
            ],
            'recetas': {
                ('Agua', 'Hierba'): ('Poción de Curación', (255, 80, 120)),
                ('Agua', 'Polvo mágico'): ('Poción de Energía', (255, 255, 80)),
                ('Hierba', 'Polvo mágico'): ('Poción de Velocidad', (255, 100, 255)),
            },
            'tiempo': 30
        },
        {
            'ingredientes': [
                ('Agua', (100, 180, 255)),
                ('Hierba', (100, 255, 100)),
                ('Polvo mágico', (200, 100, 255)),
                ('Raíz', (180, 120, 60)),
            ],
            'recetas': {
                ('Hierba', 'Raíz'): ('Poción de Resistencia', (80, 255, 180)),
                ('Polvo mágico', 'Raíz'): ('Poción de Invisibilidad', (180, 180, 180)),
                ('Agua', 'Raíz'): ('Poción de Fuerza', (150, 75, 0)),
            },
            'tiempo': 40
        },
        {
            'ingredientes': [
                ('Agua', (100, 180, 255)),
                ('Hierba', (100, 255, 100)),
                ('Polvo mágico', (200, 100, 255)),
                ('Raíz', (180, 120, 60)),
                ('Cristal', (255, 255, 255)),
            ],
            'recetas': {
                ('Agua', 'Cristal'): ('Poción de Claridad', (200, 200, 255)),
                ('Hierba', 'Cristal'): ('Poción de Regeneración', (150, 255, 150)),
            },
            'tiempo': 50
        }
    ]

    nivel_actual = 0
    puntos_extra = 0
    descubiertas = set()
    seleccionados = []
    mensaje = ''
    reloj = pygame.time.Clock()
    tiempo_inicio = pygame.time.get_ticks()

    running = True
    while running:
        screen.fill((30, 30, 60))
        nivel = niveles[nivel_actual]
        ingredientes = nivel['ingredientes']
        recetas = nivel['recetas']
        tiempo_limite = nivel['tiempo']
        # Tiempo restante
        tiempo_actual = (pygame.time.get_ticks() - tiempo_inicio) // 1000
        tiempo_restante = max(0, tiempo_limite - tiempo_actual)

        # Guardar las áreas de los ingredientes para detectar clics
        y = 50
        ingredientes_rects = []
        for i, (ing, color) in enumerate(ingredientes):
            x = 50 + i*120
            draw_potion_image(screen, x, y, color, ing, font_size=24, name_y_offset=110, width=60, height=90)
            rect = pygame.Rect(x, y, 60, 90)
            ingredientes_rects.append((rect, ing))
            # Resalta si está seleccionado
            if ing in seleccionados:
                pygame.draw.rect(screen, (255,255,0), (x-5, y-25, 70, 130), 3)
        # Mostrar mensaje
        msg_text = font.render(mensaje, True, (255, 200, 200))
        screen.blit(msg_text, (50, 250))
        # Mostrar pociones descubiertas como imágenes
        y2 = 350
        screen.blit(font.render(f'Nivel {nivel_actual+1} - Pociones descubiertas:', True, (180, 255, 180)), (50, y2))
        x2 = 50
        for pocion in descubiertas:
            for (k1, k2), (nombre, color) in recetas.items():
                if nombre == pocion:
                    draw_potion_image(screen, x2, y2+40, color, nombre, font_size=30, name_y_offset=160, width=80, height=110)
                    x2 += 200
                    break
        # Mostrar tiempo restante y puntos extra
        tiempo_text = font.render(f'Tiempo restante: {tiempo_restante}s', True, (255,255,100))
        screen.blit(tiempo_text, (500, 50))
        puntos_text = font.render(f'Puntos extra: {puntos_extra}', True, (255,255,255))
        screen.blit(puntos_text, (500, 90))
        # Mostrar pistas en el último nivel si hay puntos extra
        if nivel_actual == len(niveles)-1 and puntos_extra > 0:
            pista_text = font.render('¡Usa tus puntos extra para pedir pistas!', True, (255,200,200))
            screen.blit(pista_text, (50, 320))
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                elif event.key == pygame.K_r:
                    descubiertas.clear()
                    seleccionados = []
                    mensaje = 'Nivel reiniciado.'
                    tiempo_inicio = pygame.time.get_ticks()
                elif event.key == pygame.K_p and nivel_actual == len(niveles)-1 and puntos_extra > 0:
                    # Dar pista en el último nivel
                    receta_faltante = [nombre for (k1, k2), (nombre, _) in recetas.items() if nombre not in descubiertas]
                    if receta_faltante:
                        mensaje = f'Pista: Mezcla para obtener {receta_faltante[0]}'
                        puntos_extra -= 1
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                mouse_pos = event.pos
                for rect, ing in ingredientes_rects:
                    if rect.collidepoint(mouse_pos):
                        if len(seleccionados) < 2 and ing not in seleccionados:
                            seleccionados.append(ing)
                        if len(seleccionados) == 2:
                            comb = tuple(sorted(seleccionados))
                            resultado = recetas.get(comb)
                            if resultado:
                                mensaje = f'¡Has creado: {resultado[0]}!'
                                descubiertas.add(resultado[0])
                            else:
                                mensaje = 'La mezcla no produce nada...'
                            seleccionados = []
        # Si se descubren todas las pociones del nivel
        if len(descubiertas) == len(recetas):
            if tiempo_restante > 0:
                puntos_extra += 1
            nivel_actual += 1
            if nivel_actual >= len(niveles):
                mensaje = f'¡Felicidades! Has completado todos los niveles.'
                running = False
            else:
                mensaje = f'¡Nivel completado! Avanzas al nivel {nivel_actual+1}'
                descubiertas = set()
                seleccionados = []
                tiempo_inicio = pygame.time.get_ticks()
        reloj.tick(30)
    pygame.quit()
    sys.exit()

if __name__ == '__main__':
    main()
