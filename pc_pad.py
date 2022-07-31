import pygame
from player import Player
from settings import Settings

class PcPad(Player, Settings):
    
    x = Settings.screen_width - 50
    
    def __init__(self, screen, y):
        super().__init__(screen, y)
        self.score = 0
    
    def update_pc_pad(self, ball):
        self.y = ball.y - (self.height / 2)
        self.draw_rect()
