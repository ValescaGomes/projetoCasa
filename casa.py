#Importando o pygame
import pygame
#Iniciando o jogo
pygame.init()
#largura e altura da janela de exibição
window_width=500
window_height=500

#Adicionando os valores da janela de exibição a variável tamanho.
tamanho = (window_width, window_height)
#a variável tela recebe e define o tamanho da janela
tela = pygame.display.set_mode(tamanho)
#Setando o nome que irá aparecer na tela do jogo
pygame.display.set_caption("CASA")
#variavel fexharTela é setada como falso
fecharTela=False
#Definindo as cores
BRANCO=(255,255,255)
VERMELHO=(255,0,0)
VERDE=(0,255,0)
AZUL=(0,0,255)
PRETO=(0,0,0)
MARRON=(165,42,42)

#fundo da janela é branco
tela.fill(BRANCO)
#método que desenha a casa
def desenhoCasa():
    #desenhar retangulo na tela, cor da casa marron e coordenadas.
    pygame.draw.rect(tela, MARRON, [110, 350, 300, 250])
    pygame.draw.polygon(tela, AZUL, [[450, 350], [275, 230], [70, 350]])
    pygame.draw.rect(tela, VERDE, [160, 400, 50, 300])
#comando que fecha a tela se clicar no "X"
while(fecharTela==False):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            fecharTela = True
#chamando o método desenhoCasa
    desenhoCasa()
#esse comando atualiza o conteúdo da tela, TIRA ESSE COMANDO E TESTA SEM ELE
    pygame.display.flip()


