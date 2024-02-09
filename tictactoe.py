import sys
import pygame as p 
from const import *
import numpy as np
import random
import copy
import time

p.init()

screen = p.display.set_mode((WIDTH,HEIGHT))

p.display.set_caption('Tic Tac Toe')
screen.fill(bg_color)

pause = False

class Board:
    
    def __init__(self):
        self.squares = np.zeros( (rows,columns) )
        self.empty_sqrs = self.squares
        self.marked_sqrs = 0
        
    def final_state(self):
        
        for col in range(columns):
            if self.squares[0][col] == self.squares[1][col] == self.squares[2][col] != 0:           
                return self.squares[1][col]
        
        for row in range(rows):
            if self.squares[row][0] == self.squares[row][1] == self.squares[row][2] != 0:
                return self.squares[row][0] 
        
        if self.squares[0][0] == self.squares[1][1] == self.squares[2][2] != 0:
            return self.squares[1][1]
        
        elif self.squares[2][0] == self.squares[1][1] == self.squares[0][2] != 0:
            return self.squares[1][1]
        
        else:
            return 0
        
    def mark_sqr(self, rows, columns, player):
        self.squares[rows][columns] = player
        self.marked_sqrs += 1
        
    def empty_sqr(self, row, col):
        return self.squares[row][col] == 0
    
    def getempty(self):
        empty_sqrs = []
        for row in range(rows):
            for col in range(columns):
                if self.empty_sqr(row, col):
                    empty_sqrs.append( (row,col) )
                    
        return empty_sqrs
    
    def isfull(self):
        return self.marked_sqrs == 9
    
    def isempty(self):
        return self.marked_sqrs == 0
    
    def isend(self):
        return self.marked_sqrs == 9 or self.final_state() != 0

class AI:
    
    def __init__(self, player=2):
        self.level = 1
        self.player = player

        
    def rnd(self, board):
        empty_sqrs = board.getempty()
        idx = random.randrange(0, len(empty_sqrs))
        
        return empty_sqrs[idx]
    
    def minimax(self, board, max):
        
        t_case = board.final_state()
        
        if t_case == 1: 
            return 1, None
        
        elif t_case == 2:
            return -1, None
        
        elif board.isfull():
            return 0, None
        
        if max:
            max_eval = -100
            best_move = None
            empty_sqrs = board.getempty()

            for (row, col) in empty_sqrs:
                temp_board = copy.deepcopy(board)
                temp_board.mark_sqr(row, col, 1)
                eval = self.minimax(temp_board, False)[0]
                if eval > max_eval:
                    max_eval = eval
                    best_move = (row, col)

            return max_eval, best_move

        elif not max:
            min_eval = 100
            best_move = None
            empty_sqrs = board.getempty()

            for (row, col) in empty_sqrs:
                temp_board = copy.deepcopy(board)
                temp_board.mark_sqr(row, col, 2)
                eval = self.minimax(temp_board, True)[0]
                if eval < min_eval:
                    min_eval = eval
                    best_move = (row, col)

            return min_eval, best_move
                
    def move(self, main_board):
        if self.level == 0:
            eval = 'random'
            move = self.rnd(main_board)
            return move
        else:
            
            if self.player == 1:
                max = True
            else:
                max = False
            
            if not Board().isfull() and Board().final_state()==0:
                eval, move = self.minimax(main_board, max)

                print(f'AI has chosen to mark square in pos {move} with an eval of: {eval}')
                return move
    
class Game:
    
    def __init__(self):
        
        self.player = 1
        self.board = Board()
        self.ai = AI()
        self.show_lines()
        self.board = Board()
        self.gamemode = ''
        
    def makemove(self, row, col):   
        self.board.mark_sqr(row, col, self.player)
        self.draw_fig(row, col, self.player)
        self.next_turn()
        
    def genmakemove(self, row, col, player):
        self.draw_fig(row, col, self.player)
                    
    def show_lines(self):
        p.draw.line(screen,line_color, (sqsize,0),(sqsize,HEIGHT), l_width)
        p.draw.line(screen,line_color, (2*sqsize,0),(2*sqsize,HEIGHT), l_width)
        
        p.draw.line(screen,line_color, (0,sqsize),(HEIGHT,sqsize), l_width)
        p.draw.line(screen,line_color, (0,2*sqsize),(HEIGHT,2*sqsize), l_width)

    def next_turn(self):
        self.player = self.player % 2 + 1 
    
    def draw_fig(self, row, col, player):
        if player == 1:
            p.draw.line(screen, x_color, (col*sqsize+offset, row*sqsize+offset),((col)*sqsize+sqsize-offset,row*sqsize+sqsize-offset), fig_width)
            p.draw.line(screen, x_color, (col*sqsize+offset, row*sqsize+sqsize-offset),(col*sqsize+sqsize-offset,row*sqsize+offset), fig_width)
        
        elif player == 2:
            p.draw.circle(screen, circle_color, (col*sqsize+sqcenter,row*sqsize+sqcenter), 3*sqsize//10, fig_width)
            
    def end_game(self):
        
        if self.board.final_state() != 0:

            for col in range(columns):
                if self.board.squares[0][col] == self.board.squares[1][col] == self.board.squares[2][col] != 0:   
                    
                    if self.board.squares[0][col] == 1:
                        color = circle_color
                        endtxt = font.render('X wins!', True,(42, 47, 54))
                    else:
                        color = x_color
                        endtxt = font.render('O wins!', True,(42, 47, 54))
                        
                    p.draw.line(screen, color, (col*sqsize + sqsize//2, offset//2), (col*sqsize + sqsize//2, WIDTH - offset//2), fig_width)
                            
    
            for row in range(rows):
                if self.board.squares[row][0] == self.board.squares[row][1] == self.board.squares[row][2] != 0:
                    
                    if self.board.squares[row][0] == 1:
                        color = circle_color
                        endtxt = font.render('X wins!', True,(42, 47, 54))
                    else:
                        color = x_color
                        endtxt = font.render('O wins!', True,(42, 47, 54))
                        
                    p.draw.line(screen, color, (offset//2, row*sqsize +sqsize//2), (WIDTH - offset//2, row*sqsize + sqsize//2), fig_width)
                        
            
            if self.board.squares[0][0] == self.board.squares[1][1] == self.board.squares[2][2] != 0:
                
                if self.board.squares[1][1] == 1:
                    color = circle_color
                    endtxt = font.render('X wins!', True,(42, 47, 54))
                else:
                    color = x_color
                    endtxt = font.render('O wins!', True,(42, 47, 54))
                
                p.draw.line(screen, color, (offset//2, offset//2), (WIDTH - offset//2, WIDTH - offset/2), fig_width)
            
            elif self.board.squares[2][0] == self.board.squares[1][1] == self.board.squares[0][2] != 0:
                
                if self.board.squares[1][1] == 1:
                    color = circle_color
                    endtxt = font.render('X wins!', True,(42, 47, 54))
                else:
                    color = x_color
                    endtxt = font.render('O wins!', True,(42, 47, 54))
                
                p.draw.line(screen, color, (WIDTH - offset//2, offset//2), (offset//2, WIDTH - offset/2), fig_width)
                

            p.display.update()
        
            time.sleep(1)
            
            p.draw.rect(screen, game_end_color, p.Rect(100, 250, 400, 100))
            screen.blit(restart_text, (200, 310))
            screen.blit(endtxt , (250,260))
            
            p.display.update()
            
        elif self.board.isfull():
            
            endtxt = font.render('Tie!', True,(42, 47, 54))
            
            p.display.update()
        
            time.sleep(1)
            
            p.draw.rect(screen, game_end_color, p.Rect(100, 250, 400, 100))
            screen.blit(restart_text, (200, 310))
            screen.blit(endtxt , (270,260))

    def genBoard(self):
        screen.fill(bg_color)
        self.show_lines()
        for r in range(rows):
            for c in range(columns):
                player = actual_board[r][c]
                self.draw_fig(r, c, player)
                    
        p.display.update()
        
    def pause(self):
        p.draw.rect(screen, pause_color, p.Rect(100, 150, 400, 300), )
        p.draw.rect(screen, pause_color2, p.Rect(100, 150, 400, 35), )
        
        p.draw.rect(screen, (116, 129, 143), (240, 235, 55, 30), 3)
        p.draw.rect(screen, (116, 129, 143), (312, 235, 55, 30), 3)
    
        screen.blit(mode_text, (220,200))
        screen.blit(gamemode_text, (190,300))
        screen.blit(restart_text,(200,415))
        
        screen.blit(x_text,(260,240))
        screen.blit(circle_text,(330,240))
        
        p.draw.rect(screen, (116, 129, 143), (240, 235, 55, 30), 3)
        p.draw.rect(screen, (116, 129, 143), (312, 235, 55, 30), 3)
        
        screen.blit(PVE_text, (230,350))
        screen.blit(PVP_text, (320,350))
        
        p.draw.rect(screen, (116, 129, 143), (220, 343, 70, 40), 3)
        p.draw.rect(screen, (116, 129, 143), (310, 343, 70, 40), 3)
        
        p.display.update()
                   
def main(gamemode, player):
    
    screen.fill(bg_color)
    
    global pause
    
    game = Game()
    board = game.board
    
    game.gamemode = gamemode
    
    ai = AI(player)
    
    while True:
        
        if pause:
            game.pause()
          
        p.display.update()
        
        for event in p.event.get():
        
            if event.type == p.QUIT:
                p.quit()
                sys.exit()
                break
            
            if event.type == p.MOUSEBUTTONDOWN:
                
                if game.gamemode == 'ai':
                    if game.player != ai.player:
                        
                        if not pause:
                            pos = event.pos
                            p_row = pos[1] // sqsize
                            p_col = pos[0] // sqsize
                            
                            if board.empty_sqr(p_row,p_col):
                                game.makemove(p_row,p_col)
                                p.display.update()
                                print(game.board.squares)
                                
                else: 
                    
                    if not pause:
                            pos = event.pos
                            p_row = pos[1] // sqsize
                            p_col = pos[0] // sqsize
                            
                            if board.empty_sqr(p_row,p_col):
                                game.makemove(p_row,p_col)
                                p.display.update()
                                print(game.board.squares)
                                    
            if event.type == p.KEYDOWN:
                
                if event.key == p.K_ESCAPE:
                    if pause:
                        pause = False
                        game.genBoard()
                    else:
                        pause = True
                
                if event.key == p.K_r:
                    main(gamemode = game.gamemode, player = ai.player)
                    
            if pause:
                if event.type == p.MOUSEBUTTONDOWN:
                    pos = event.pos
                    
                    if 290>=pos[0]>=220 and 383>=pos[1]>=343:
                        main('ai',game.player)
                        game.gamemode = 'ai'
                    
                    if 380>=pos[0]>=310 and 383>=pos[1]>=343:
                        main('pvp',game.player)
                        game.gamemode = 'pvp'
                        
                    if game.gamemode == 'ai':
                        if 295>=pos[0]>=240 and 265>=pos[1]>=235:
                            main('ai', 2)
                        
                        if 367>=pos[0]>=312 and 265>=pos[1]>=235:
                            main('ai', 1)
        
        if not pause: 
            if game.gamemode == 'ai' and game.player == ai.player:
                
                if ai.player == 1:
                    
                    if board.marked_sqrs==0:
                        ai.level = 0
                        row, col = ai.move(board)
                        game.makemove(row, col)
                        time.sleep(1)
                        ai.level = 1
                        p.display.update()
                
                    elif not board.isfull():
                        row, col = ai.move(board)
                        game.makemove(row, col)    
                
                else:
                    
                     if not board.isfull():
                        row, col = ai.move(board)
                        game.makemove(row, col)    
                    
            game.end_game()
            
            p.display.update()
            
        global actual_board
        actual_board = game.board.squares
    
main('ai',2)