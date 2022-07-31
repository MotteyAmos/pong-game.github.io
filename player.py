import pygame
from settings import Settings

class Player(Settings):
    width = 20
    height = 100
    color = Settings.white
    x = 50
    pad_speed = 8
    
    def __init__(self, screen, y):
        self.screen = screen
        self.y = y

        self.move_up = False
        self.move_down = False
        self.score = 0
    
    
    def draw_rect(self):
        pygame.draw.rect(self.screen, self.color, pygame.Rect(self.x, self.y, Player.width, Player.height))
    
    def move_pad(self):
        if self.move_up and self.y > 0:
            self.y -= self.pad_speed
        if self.move_down and self.y + self.height < Settings.screen_height:
            self.y += self.pad_speed
        self.draw_rect()


       
    