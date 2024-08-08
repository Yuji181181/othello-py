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

square_num = 8
square_size = 800//square_num

player = 1

vec_table = [
    (-1, -1),  
    (0, -1),    
    (1, -1),    
    (-1, 0),   
    (1, 0),  
    (-1, 1),   
    (0, 1),    
    (1, 1)] 

game_over = False
pass_num = 0





def draw_grid():    
    for i in range(square_num):
        pygame.draw.line(screen,BLACK,(0,i*square_size),(800,i*square_size),3)
        pygame.draw.line(screen,BLACK,(i*square_size,0),(i*square_size,800),3)

def draw_board():
    for row_index, row in enumerate(board):
        for col_index, col in enumerate(row):
            if col == 1:
                pygame.draw.circle(screen, BLACK, (col_index * square_size + 50, row_index * square_size + 50), 45)
            elif col == -1:
                pygame.draw.circle(screen, WHITE, (col_index * square_size + 50, row_index * square_size + 50), 45)


run = True
while run:
    
    screen.fill(GREEN)
    draw_grid()
    draw_board()
    
    
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


