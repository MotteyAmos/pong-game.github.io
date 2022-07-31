import random
class Settings:
    black = (0,0,0)
    white = (255, 255, 255)
    silver = (192, 192, 192)
    FLP = 120
    
    #background settings
    screen_size = screen_width, screen_height = 800, 600
    bg_color = black
    game_title = "Pong Game"

    #net settings
    net_width = 6
    net_x = (screen_width / 2) - (net_width / 2)
    net_height = 15
    net_gap = 2 * net_height
    net_y = [y for y in range(0, screen_height, 40)]

    # ball settings
    ball_x = screen_width / 2
    ball_y = screen_height / 2
    ball_radius = 20
    
    ball_move_x = random.choice([2, -2])
    ball_move_y = random.choice([2, -2])
