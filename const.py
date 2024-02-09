import pygame as p
import numpy as np

p.init()

WIDTH = 600
HEIGHT = 600 
l_width = 15

rows = 3
columns = 3

sqsize = WIDTH // columns
offset = WIDTH//12
sqcenter = WIDTH//6
sqcorner = WIDTH//42

bg_color = (14, 33, 54)

line_color = (16, 45, 82)

game_end_color = (172, 181, 191)
pause_color = (115, 169, 222)
pause_color2 = (48, 57, 66)

x_color = (176, 190, 207)
circle_color = (84, 90, 97)

fig_width = 10

font = p.font.Font('freesansbold.ttf', 25)
restart_text = font.render('Press r to restart', True,(42, 47, 54))
mode_text = font.render('Player Select:', True,(42, 47, 54))
gamemode_text = font.render('Select Gamemode:', True,(42, 47, 54))
x_text = font.render('X', True,(42, 47, 54))
circle_text = font.render('O', True,(42, 47, 54))
PVE_text = font.render('PVE', True,(42, 47, 54))
PVP_text = font.render('PVP', True,(42, 47, 54))

