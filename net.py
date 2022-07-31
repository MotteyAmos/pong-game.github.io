import pygame
from settings import Settings
from player import Player


class Net:
    nets = []
    def __init__(self, screen, y = float()):
        self.screen = screen
        self.y = y

    def draw_net(self):
        pygame.draw.rect(self.screen, Settings.white, pygame.Rect(Settings.net_x, self.y, Settings.net_width, Settings.net_height))
    
    def __repr__(self):
        return f"{self.y}"
    
    def create_net(self):
        for y in Settings.net_y:
            Net.nets.append(Net(self.screen, y))
    
    def draw_all_net(self):
        for net in Net.nets:
            net.draw_net()
            

    