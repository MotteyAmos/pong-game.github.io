import pygame, sys
import random
import math
def key_down(event, player):
    # check when a key is pressed from the keyboard
    if event.key == pygame.K_UP:
        player.move_up = True
    if event.key == pygame.K_DOWN:
        player.move_down = True

def key_up(event, player):
    # check when a key is released from the keyboard
    if event.key == pygame.K_UP:
        player.move_up = False
    if event.key == pygame.K_DOWN:
        player.move_down = False

def run_event(player):
    #check keypresssed and keydown event
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            key_down(event, player)
        
        if event.type == pygame.KEYUP:
            key_up(event, player)

def collusion(ball, rect, Settings):
    # return true if the ball hit and side of the pads
    ball_left = ball.x - ball.radius
    ball_right = ball.x + ball.radius
    ball_top = ball.y - ball.radius
    ball_bottom = ball.y + ball.radius

    rect_right = rect.x + rect.width
    rect_left = rect.x
    rect_top = rect.y
    rect_bottom = rect.y + rect.height

    rect_center_x = rect.x + (rect.width / 2)
    rect_center_y = rect.y + (rect.height / 2)
    rect_mid_width = ((rect.x + rect.width) - rect.x)/ 2
    rect_mid_height = ((rect.y + rect.height) - rect.y) / 2
    if ball.x < Settings.screen_width/2:
        if ball_left >= rect_left and ball_left <= rect_right  and ball.y + ball.radius >= rect.y and  ball.y - ball.radius <= rect.y + rect.height :
            return True
    elif ball.x > Settings.screen_width/2:
        if ball_right >= rect_left and abs(ball.y - rect_center_y) <= ball.radius + (rect.height / 2):
            return True
    #rect
  
    

def pad_play(ball, player, pc_pad, Settings):
    # bounce the ball off when both player strike the ball
    run = [1, -1]
    if ball.x < Settings.screen_width / 2:
        if collusion(ball, player, Settings):
            Settings.ball_move_x *= random.choice(run)
            Settings.ball_move_y *= -1
    if ball.x > Settings.screen_width / 2:
        if collusion(ball, pc_pad, Settings):
            Settings.ball_move_x *= -1
            Settings.ball_move_y *= random.choice(run)

def scores(Settings, screen, player, pc_pad):
    # check and upadate the score of the player when they hit the ball
    #player score
    player_score = pygame.font.SysFont("Sans-serif", 70)
    player_score_text = player_score.render(f"score: {player.score}",True, Settings.white)
    player_score_rect = player_score_text.get_rect()
    player_score_rect.center = (150, 20)

    # pc score
    pc_score = pygame.font.SysFont("Sans-Serif", 70)
    pc_score_text = pc_score.render(f"Score: {pc_pad.score}", True, Settings.white)
    pc_score_rect = pc_score_text.get_rect()
    pc_score_rect.center = (Settings.screen_width -150, 20)

    screen.blit(player_score_text, player_score_rect)
    screen.blit(pc_score_text, pc_score_rect)
        


def main_update(SCREEN, Settings, player, pc_pad, net, ball, clock):
    #check and update all action
    clock.tick(Settings.FLP)
    run_event(player)
    SCREEN.fill(Settings.bg_color)

    net.draw_all_net()
    player.draw_rect()
    
    #check, move and create the ball
    pad_play(ball, player, pc_pad, Settings)
    ball.check_ball()
    ball.move_ball()
    ball.draw_ball()

    pc_pad.update_pc_pad(ball)
    #check if the player pad has been move 
    player.move_pad()


    #check and update both scores
    scores(Settings, SCREEN, player, pc_pad)

    pygame.display.update()
