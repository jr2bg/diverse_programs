# https://riptutorial.com/pygame/example/18049/state-checking

import pygame
import numpy as np

def neigh(pos,n_rows, n_columns):
    Moore_n = np.array([[-1,-1],[-1,0],[-1,1],
                [0,-1],[0,0],[0,1],
                [1,-1],[1,0],[1,1]])
    pos_neig = (np.array(pos) + Moore_n) % np.array([n_rows, n_columns ])
    return pos_neig ## np array con las posiciones de la vecidad para una posición

def rules(config):

    n_config = np.zeros((len(config), len(config[0])))
    for i_r in range(len(config)):
        for j_c in range(len(config[0])):
            l_c = 0
            pos_neig = neigh([i_r, j_c], len(config), len(config[0]) )
            for cell in pos_neig:
                #print(cell)
                l_c += config[cell[0], cell[1]]
            l_c -= config[i_r, j_c]
            if l_c == 3 or (l_c == 2 and config[cell[0], cell[1]] == 1):
                print(i_r, j_c, l_c)
                n_config[i_r, j_c] = 1
    return n_config


def life_Rules(cell, cell_neighbourhood):
    # determines if the cell is 0/1, death/alive based on its neighbours
    # cell_neighbourhood -> list with 0/1 for death/alive neighbour
    # num_al -> number of alive neighbours
    # minus cell to obtain the surrounding value
    num_al = np.sum(cell_neighbourhood) - cell
    # death
    if  num_al < 2 or num_al > 3:
        return 0
    # survival
    elif cell == 1:
        return 1
    # birth
    elif cell == 0 and num_al == 3:
        return 1
    # return the current cell state when 2 alive cells surround it
    else:
        return cell

def rearrange(lattice, filas, cols):
    # rearranges the lattice in order to have an appropiate one
    # columnas
    lattice[:,0] = lattice[:,cols]
    lattice[:,cols+1] = lattice[:,1]
    # filas
    lattice[0,: ] = lattice[filas,:]
    lattice[filas + 1,:] = lattice[1,:]
    # vertices
    lattice[0,0] = lattice[filas,cols]
    lattice[filas+1, cols + 1] = lattice[1,1]
    lattice[0,cols + 1] = lattice[filas,1]
    lattice[filas + 1, 0] = lattice[1, cols]
    return lattice

def iteration(lattice, filas, cols):
    # defines the way it iterates over the lattice covered by cells
    # lattice is an array
    n_lattice = np.copy(lattice)
    for i in range(1,len(lattice) - 1):
        for j in range(1,len(lattice[0]) - 1):
            cell = lattice[i,j]
            cell_neighbourhood = lattice[i-1:i+2, j-1:j+2]
            n_lattice[i,j] = life_Rules(cell, cell_neighbourhood)
    n_lattice = rearrange(n_lattice, filas, cols)
    return n_lattice


white = (255, 255, 255)
black = ( 0, 0, 0)
gray = (165, 165, 165)
tamCuadro = 20
height = 30#num_cuadros altura
width = 30 #num_cuadros ancho

config = np.zeros((height + 2, width + 2))

dic_states = {0: white, 1: black}


## VISUALIZACIÓN
pygame.init()
pygame.event.pump()
mouse_pos = pygame.mouse.get_pos()
mouse_buttons = pygame.mouse.get_pressed()
size = ((tamCuadro + 1) * width, (tamCuadro + 1) * height)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Grid on PYGAME")
clock = pygame.time.Clock()
FPS = 10    #frames per secont
clock.tick(FPS)
gameOver = False
setup = True

while setup:
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            print("a mouse BUTTON PRESSED!!!  :3")
            print(event.pos, event.pos[0] // (tamCuadro + 1))
            config[event.pos[1] // (tamCuadro + 1) + 1 , event.pos[0] // (tamCuadro + 1) + 1] = 1

        elif event.type == pygame.QUIT:
            setup = False
    screen.fill(gray)
    config = rearrange(config, height, width)
    wh = 1
    for i in range(1, size[0], tamCuadro + 1):   # width
        ht = 1
        for j in range(1, size[1], tamCuadro + 1): # height
            pygame.draw.rect(screen, dic_states[config[ht,wh]], [i, j, tamCuadro, tamCuadro], 0)
            ht += 1
        wh += 1
    pygame.display.flip()
    clock.tick(1)

while not gameOver:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameOver = True
    screen.fill(gray)
    config = iteration(config, height, width)
    wh = 1
    for i in range(1, size[0], tamCuadro + 1):   # width
        ht = 1
        for j in range(1, size[1], tamCuadro + 1): # height
            pygame.draw.rect(screen, dic_states[config[ht,wh]], [i, j, tamCuadro, tamCuadro], 0)
            ht += 1
        wh += 1
    pygame.display.flip()
    clock.tick(1)
pygame.quit()
