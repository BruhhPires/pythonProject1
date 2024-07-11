import pygame
from pygame import Surface, Rect

W_WIDTH = 576
H_HEIGHT = 324

# Inicializar o Módulo do Pygame
pygame.init()
print('Setup Start')

# Criação de Janela do Pygame
window: Surface = pygame.display.set_mode(size=(W_WIDTH, H_HEIGHT))

# Carregar Imagem e gerar uma superficie
bg_surf: Surface = pygame.image.load('./assets/bg.png').convert_alpha()
p_surf: Surface = pygame.image.load('./assets/player1.png').convert_alpha()

# Obert o Retangulo da superficie
bg_rect: Rect = bg_surf.get_rect(left=0, top=0)
player1_rect: Rect = p_surf.get_rect(left=100, top=100)

# Desenhar na janela (window)
window.blit(source=bg_surf, dest=bg_rect)
window.blit(source=p_surf, dest=player1_rect)

# Atualizar a janela
pygame.display.flip()

# Colocar um relógio no nosso jogo
clock = pygame.time.Clock()

# Carregar musica e deixar tocando
pygame.mixer.music.load('./assets/music_Theme.wav')
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.2)

print('Setup End')
print('Setup Start') # Printar o FPS
while True:
    clock.tick(140)  # Esse loop está acontecendo 30x por segundo
    print(f'{clock.get_fps() :.0f}')
    window.blit(source=bg_surf, dest=bg_rect)
    window.blit(source=p_surf, dest=player1_rect)
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print('Loop End')
            pygame.quit()
            quit()
    pressed_key = pygame.key.get_pressed()
    if pressed_key[pygame.K_w]:
        player1_rect.centery -= 1
    if pressed_key[pygame.K_s]:
        player1_rect.centery += 1
    if pressed_key[pygame.K_a]:
        player1_rect.centerx -= 1
    if pressed_key[pygame.K_d]:
        player1_rect.centerx += 1

        pass
#
