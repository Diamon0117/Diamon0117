import pygame, sys, random, neat, time, os

def ball_animation():
    global ballSpeed_x, ballSpeed_y, player_01_score, opponent_01_score
    ball.x += ballSpeed_x
    ball.y += ballSpeed_y

    if ball.top <= 0 or ball.bottom >= screen_height:
        ballSpeed_y *= -1
    if ball.left <= 0:
        player_01_score += 1
        ball_restart()
    if ball.right >= screen_width:
        opponent_01_score += 1
        ball_restart()

    if ball.colliderect(player_01) or ball.colliderect(opponent_01):
        ballSpeed_y *= -1
        ballSpeed_x *= -1
        ballSpeed_y += 2.5
        ballSpeed_x += 2.5
def player_animation():
    player_01.y += playerSpeed
    if player_01.top <= 0:
        player_01.top = 0
    if player_01.bottom >= screen_height:
        player_01.bottom = screen_height
def opponent_ai():
    if opponent_01.top < ball.y:
        opponent_01.top += opponent_speed
    if opponent_01.bottom > ball.y:
        opponent_01.bottom -= opponent_speed
    if opponent_01.top <= 0:
        opponent_01.top = 0
    if opponent_01.bottom >= screen_height:
        opponent_01.bottom = screen_height
def player_ai():
    if player_01.top < ball.y:
        player_01.top += opponent_speed
    if player_01.bottom > ball.y:
        player_01.bottom -= opponent_speed
    if player_01.top <= 0:
        player_01.top = 0
    if player_01.bottom >= screen_height:
        player_01.bottom = screen_height
def ball_restart():
    global ballSpeed_x, ballSpeed_y
    ballSpeed_x = 7
    ballSpeed_y = 7
    ball.center = (screen_width/2, screen_height/2)
    ballSpeed_x *= random.choice((1, -1))
    ballSpeed_y *= random.choice((1, -1))

pygame.init()
clock = pygame.time.Clock()

#Main Window
screen_width = 900
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Pong | version 0.0.1")

#Game Objects
ball = pygame.Rect(screen_width/2 - 15, screen_height/2 - 15, 30, 30)
player_01 = pygame.Rect(screen_width - 20, screen_height/2 - 70, 10, 140)
opponent_01 = pygame.Rect(10, screen_height/2 - 70, 10, 140)

a = random.randint(0, 230)
b = random.randint(0, 230)
c = random.randint(0, 230)

#Colors
changing_color_a = 0
changing_color_b = 255
changing_color_c = 155
changing_color = (changing_color_a, changing_color_b, changing_color_c)
rand_color = (a, b, c)
light_grey = (200, 200, 200)
green = (0, 255, 0)
red = (255, 0, 0)
white = (0, 0, 0)

ballSpeed_x = 7
ballSpeed_y = 7
playerSpeed = 0
opponent_speed = 7



#changing color





#Text Variables
player_01_score = 0
opponent_01_score = 0
game_font = pygame.font.Font("freesansbold.ttf", 40)

#Close The Window
while True:
    #Handeling Input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_s:
                playerSpeed += 7
            if event.key == pygame.K_w:
                playerSpeed -= 7
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_s:
                playerSpeed -= 7
            if event.key == pygame.K_w:
                playerSpeed += 7


    ball_animation()
    player_animation()
    opponent_ai()
    #player_ai()


    #Visuals
    screen.fill(white)
    pygame.draw.ellipse(screen, rand_color, ball)
    pygame.draw.rect(screen, green, player_01)
    pygame.draw.rect(screen, red, opponent_01)
    pygame.draw.aaline(screen, light_grey, (screen_width/2, 0), (screen_width/2, screen_height))

    player_01_text = game_font.render(f"{player_01_score}", False, light_grey)
    opponent_01_text = game_font.render(f"{opponent_01_score}", False, light_grey)
    screen.blit(player_01_text, (screen_width / 2 + 30, screen_height - screen_height + 10))
    screen.blit(opponent_01_text, (screen_width / 2 - 50, screen_height - screen_height + 10))

    #Updating Window
    pygame.display.flip()
    clock.tick(60)