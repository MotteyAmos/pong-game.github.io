import pygame, sys
from pygame.locals import *
from settings import Settings
import functionality
from player import Player
from pc_pad import PcPad
from net import Net
from ball import Ball

#initialize the functionality of the game
pygame.init()
clock = pygame.time.Clock()

#setting the window screen
SCREEN = pygame.display.set_mode(Settings.screen_size)
pygame.display.set_caption(Settings.game_title)
# player pad
player = Player(SCREEN, 100)
#pc pad
pc_pad = PcPad(SCREEN, 100)
# net
net = Net(SCREEN)
#ball
ball = Ball(SCREEN, player, pc_pad)

# create a fleet of nets
net.create_net()
def __main():
    while True:
        
        functionality.main_update(SCREEN, Settings, player, pc_pad, net, ball, clock)
        
if __name__ == "__main__":
    __main()