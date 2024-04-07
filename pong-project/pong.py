import pygame
import sys
import os

pygame.init()
pygame.font.init()

WIDTH, HEIGHT = 500, 700
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Pong')

PLAYER_ONE_SCORE, PLAYER_TWO_SCORE = 0, 0

font = pygame.font.Font('Richu Mast Regular.ttf', 12)

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

PADDLE_WIDTH, PADDLE_HEIGHT = 20, 120
PADDLE_SPEED = 15

BALL_SIZE = 20
BALL_SPEED_X, BALL_SPEED_Y = 6, 6

L_PADDLE = pygame.Rect(20, HEIGHT // 2 - PADDLE_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT)

R_PADDLE = pygame.Rect(WIDTH - 40, HEIGHT // 2 - PADDLE_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT)

ball = pygame.Rect(WIDTH // 2 - BALL_SIZE // 2, HEIGHT // 2 - BALL_SIZE // 2, BALL_SIZE, BALL_SIZE)

def move_paddles():
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and L_PADDLE.top > 0:
        L_PADDLE.y -= PADDLE_SPEED
    if keys[pygame.K_s] and L_PADDLE.bottom < HEIGHT:
        L_PADDLE.y += PADDLE_SPEED
    if keys[pygame.K_UP] and R_PADDLE.top > 0:
        R_PADDLE.y -= PADDLE_SPEED
    if keys[pygame.K_DOWN] and R_PADDLE.bottom < HEIGHT:
        R_PADDLE.y += PADDLE_SPEED

def move_ball():
    global BALL_SPEED_X, BALL_SPEED_Y
    ball.x += BALL_SPEED_X
    ball.y += BALL_SPEED_Y

    global PLAYER_ONE_SCORE, PLAYER_TWO_SCORE

    def reset_ball():
        ball.x = WIDTH // 2 - BALL_SIZE // 2
        ball.y = HEIGHT // 2 - BALL_SIZE // 2

    if ball.top <= 0 or ball.bottom >= HEIGHT:
        BALL_SPEED_Y *= -1
    if ball.left <= 0:
        reset_ball()
        PLAYER_TWO_SCORE = PLAYER_TWO_SCORE + 1
    if ball.right >= WIDTH:
        reset_ball()
        PLAYER_ONE_SCORE = PLAYER_ONE_SCORE + 1
    if ball.colliderect(L_PADDLE) or ball.colliderect(R_PADDLE):
        BALL_SPEED_X *= -1

running = True
while running:
    screen.fill(BLACK)

    pygame.draw.rect(screen, WHITE, L_PADDLE)
    pygame.draw.rect(screen, WHITE, R_PADDLE)
    pygame.draw.ellipse(screen, WHITE, ball)
    pygame.draw.aaline(screen, WHITE, (WIDTH // 2, 0), (WIDTH // 2, HEIGHT))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    move_paddles()
    move_ball()

    score_text_one = font.render(f'Player One: {PLAYER_ONE_SCORE}', True, (255, 255, 255))
    score_text_two = font.render(f'Player Two: {PLAYER_TWO_SCORE}', True, (255, 255, 255))
    screen.blit(score_text_one, (10, 10))
    screen.blit(score_text_two, (10, 25))

    pygame.display.flip()
    pygame.time.Clock().tick(60)

pygame.quit()
sys.exit()