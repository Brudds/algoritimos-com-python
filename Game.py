import pygame
import random

pygame.init()

azul = (50, 100, 213)
laranja = (205, 102, 0)
verde = (0, 255, 0)
amarelo = (255, 255, 102)

dimensoes = (600, 600)

x = 300
y = 300
d = 20
listaCobra = [[x, y]]
dx = 0
dy = 0

xComida = round(random.randrange(0, 600 - d) / 20) * 20
yComida = round(random.randrange(0, 600 - d) / 20) * 20

fonte = pygame.font.SysFont("hack", 35)

tela = pygame.display.set_mode((dimensoes))
pygame.display.set_caption('Snake Project')

tela.fill(azul)
clock = pygame.time.Clock()

def desenhaCobra(listaCobra):
    tela.fill(azul)
    for unidade in listaCobra:
        pygame.draw.rect(tela, laranja, [unidade[0], unidade[1], d, d])

def moverCobra(dx, dy, listaCobra):
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                dx = -d
                dy = 0
            elif event.key == pygame.K_RIGHT:
                dx = d
                dy = 0
            elif event.key == pygame.K_UP:
                dx = 0
                dy = -d
            elif event.key == pygame.K_DOWN:
                dx = 0
                dy = d
    x_novo = listaCobra[-1][0] + dx
    y_novo = listaCobra[-1][1] + dy

    listaCobra.append([x_novo, y_novo])

    del listaCobra[0]

    return dx, dy, listaCobra

def verifica_comida(dx, dy, xComida, yComida, listaCobra):
    head = listaCobra[-1]
    x_novo = head[0] + dx
    y_novo = head[1] + dy
    if head[0] == xComida and head[1] == yComida:
        listaCobra.append([x_novo, y_novo])
        xComida = round(random.randrange(0, 600 - d) / 20) * 20
        yComida = round(random.randrange(0, 600 - d) / 20) * 20
    pygame.draw.rect(tela, verde, [xComida, yComida, d, d])
    return xComida, yComida, listaCobra

def verifica_parede(listaCobra):
    head = listaCobra[-1]
    x = head[0]
    y = head[1]

    if x not in range(600) or y not in range(600):
        raise Exception

def atualizar_pontos(listaCobra):
    pts = str(len(listaCobra))
    score = fonte.render("Pontuação: " + pts, True, amarelo)
    tela.blit(score, [0, 0])

def verifica_corpo(listaCobra):
    head = listaCobra[-1]
    corpo = listaCobra.copy()

    del corpo[-1]
    for x,y in corpo:
        if x==head[0] and y == head[1]:
            raise Exception

while True:
    pygame.display.update()
    desenhaCobra(listaCobra)
    dx, dy, listaCobra = moverCobra(dx, dy, listaCobra)
    xComida, yComida, listaCobra = verifica_comida(dx, dy, xComida, yComida, listaCobra)
    verifica_parede(listaCobra)
    verifica_corpo(listaCobra)
    atualizar_pontos(listaCobra)

    clock.tick(10)
