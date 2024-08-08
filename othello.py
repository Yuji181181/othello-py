import pygame
pygame.init()
screen = pygame.display.set_mode((800,800))
pygame.display.set_caption("othello.py")

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 128, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

square_num = 8
square_size = 800//square_num

player = 1

game_over = False
pass_num = 0

font = pygame.font.SysFont(None,100,bold=False,italic=False)
black_win_surface = font.render("Black Win!",False,BLACK,RED)
white_win_surface = font.render("White Win!",False,WHITE,RED)
draw_surface = font.render("Draw...", False,BLUE,RED)
reset_surface = font.render("Click to reset!",False,BLACK,RED)

board = [
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, -1, 1, 0, 0, 0],
    [0, 0, 0, 1, -1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0]]
# 黒：1、白：-1

vec_table = [
    (-1, -1),  
    (0, -1),    
    (1, -1),    
    (-1, 0),   
    (1, 0),  
    (-1, 1),   
    (0, 1),    
    (1, 1)] 


def draw_grid():    
    for i in range(square_num):
        pygame.draw.line(screen,BLACK,(0,i*square_size),(800,i*square_size),3)
        pygame.draw.line(screen,BLACK,(i*square_size,0),(i*square_size,800),3)

def draw_board():
    for row_index, row in enumerate(board):
        for col_index, col in enumerate(row):
            if col == 1:
                pygame.draw.circle(screen,BLACK,(col_index*square_size+50,row_index*square_size+50),45)
            elif col == -1:
                pygame.draw.circle(screen,WHITE,(col_index*square_size+50,row_index*square_size+50),45)

def get_valid_positions():
    valid_position_list = []
    for row in range(square_num):
        for col in range(square_num):
            if board[row][col] == 0:
                for vx, vy in vec_table:
                    x = vx + col
                    y = vy + row
                    if 0 <= x < square_num and 0 <= y < square_num and board[y][x] == -player:
                        while True:
                            x += vx
                            y += vy
                            if 0 <= x < square_num and 0 <= y < square_num and board[y][x] == -player:
                                continue
                            elif 0 <= x < square_num and 0 <= y < square_num and board[y][x] == player:
                                valid_position_list.append((col,row))
                                break
                            else:
                                break
    return valid_position_list

def flip_pieces(col, row):
    for vx, vy in vec_table:
        flip_list = []
        x = vx + col
        y = vy + row
        while 0 <= x < square_num and 0 <= y < square_num and board[y][x] == -player:
            flip_list.append((x,y))
            x += vx
            y += vy
            if 0 <= x < square_num and 0 <= y < square_num and board[y][x] == player:
                for flip_x, flip_y in flip_list:
                    board[flip_y][flip_x] = player


run = True
while run:
    
    screen.fill(GREEN)
    draw_grid()
    draw_board()
    
    valid_position_list = get_valid_positions()
    
    for x, y in valid_position_list:
        pygame.draw.circle(screen,YELLOW,(x*square_size+50, y*square_size+50),45,3)
    
    if len(valid_position_list) < 1:
        player *= -1
        pass_num += 1
    
    if pass_num > 1:
        pass_num = 2
        game_over = True
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if game_over == False:
                mx, my = pygame.mouse.get_pos()
                x = mx // square_size
                y = my // square_size
                if board[y][x] == 0 and (x, y) in valid_position_list:
    
    
    
    
    
    
    
    
    
    
    
    
    pygame.display.update()

pygame.quit()


