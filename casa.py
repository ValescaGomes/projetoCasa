import pygame

pygame.init()

window_width=500
window_height=500

animation_increment=10
clock_tick_rate=20

tamanho = (window_width, window_height)
tela = pygame.display.set_mode(tamanho)

pygame.display.set_caption("CASA")

fecharTela=False

BRANCO=(255,255,255)
VERMELHO=(255,0,0)
VERDE=(0,255,0)
AZUL=(0,0,255)
PRETO=(0,0,0)
MARRON=(165,42,42)

clock = pygame.time.Clock()
tela.fill(BRANCO)

def desenhoArvore():
    pygame.draw.rect(tela, MARRON, [110, 350, 300, 250])
    pygame.draw.polygon(tela, AZUL, [[450, 350], [275, 230], [70, 350]])
    pygame.draw.rect(tela, VERDE, [160, 400, 50, 300])
while(fecharTela==False):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            fecharTela = True
    desenhoArvore()
    pygame.display.flip()
    clock.tick(clock_tick_rate)