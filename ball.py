import pygame
from settings import Settings
import time

class Ball:

    def __init__(self, screen, player, pc_pad):
        self.screen = screen
        self.x = Settings.ball_x
        self.y = Settings.ball_y
        self.radius = Settings.ball_radius
        self.color = Settings.white
        self.player = player
        self.pc_pad = pc_pad


    def draw_ball(self):
        #draw the ball
        pygame.draw.circle(self.screen, Settings.silver, (self.x, self.y), self.radius)
    
    def move_ball(self):
        #move the ball in different directions
        self.x += Settings.ball_move_x
        self.y += Settings.ball_move_y
    
    def check_ball(self):
        #change the direction of the ball when it hit the edges of the screen
     
        if self.y + self.radius >= Settings.screen_height or  self.y - self.radius == 0:
            Settings.ball_move_y *= -1
        elif self.x - self.radius >= Settings.screen_width:
            time.sleep(1)
            self.player.score += 1
            self.x = Settings.ball_x
            self.y = Settings.ball_y
        elif self.x - self.radius == 0:
            time.sleep(1)
            self.pc_pad.score += 1
            self.x = Settings.ball_x
            self.y = Settings.ball_y
          