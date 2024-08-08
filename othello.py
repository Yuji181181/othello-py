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



def draw_grid():    
    for i in range(square_num):
        pygame.draw.line(screen,BLACK,(0,i*square_size),(800,i*square_size),3)
        pygame.draw.line(screen,BLACK,(i*square_size,0),(i*square_size,800),3)




run = True
while run:
    
    screen.fill(GREEN)
    draw_grid()
    
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    
    
    
    
    
    
    
    
    
    
    
    
    pygame.display.update()

pygame.quit()


