import pygame
import math
from queue import PriorityQueue

WIDTH=800
WIN=pygame.display.set_mode((WIDTH , WIDTH))
pygame.display.set_caption("A* Pathfinding")

RED=(255 , 0 , 0)
GREEN=(0 , 255 , 0)
BLUE=(0 , 255 , 0)
YELLOW=(255 , 255 , 0)
WHITE=(255 , 255 , 255)
BLACK=(0 , 0 , 0)
PURPLE=(128 , 0 , 128)
ORANGE=(255 , 165 , 0)
GREY=(128 , 128 , 128)
TURQUOISE=(64 , 224 , 208)

class Window:
    def __init__(self , row , col , width , total_rows ):
        self.row=row
        self.col=col
        self.width=width
        self.x = row * width
        self.y = row * width
        self.color=WHITE
        self.neighboor=[]
        self.total_rows=total_rows

    def self_pos(self):
        return self.row , self.col
    
    def is_closed(self):
        return self.color == RED
    
    def is_open(self):
        return self.color == GREEN
    
    def is_barrier(self):
        return self.color == BLACK
    
    def is_start(self):
        return self.color == ORANGE
    
    def is_end(self):
        return self.color == TURQUOISE
    
    def reset(self):
        return self.color == WHITE
    
    def make_closed(self):
        self.color = RED
    
    def make_open(self):
        self.color = GREEN

    def make_barrier(self):
        self.color == BLACK
    
    def make_end(self):
        self.color = TURQUOISE
    
    def make_path(self):
        self.color = PURPLE
    
    def draw(self , window):
        pygame.draw.rect(window , self.color , (self.x , self.y , self.width , self.width))

    def update_neighbors( self , grid ):
        pass

    #It will define what happen if we compare two Window(spot)
    def __lt__(self , other):
        return False

    


