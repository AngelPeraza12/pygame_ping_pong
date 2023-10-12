import pygame

pygame.init()

screen_size = (800, 600)
screen = pygame.display.set_mode(screen_size)
clock = pygame.time.Clock()
green = "#008f39"
white = "#E0D8B0"

score1 = 0
score2 = 0
line = "-"

font = pygame.font.Font(None, 40)

player_width = 15
player_height = 90

# cord_&_velocity_player 1
player_x_coord = 50
player_y_coord = 300 - 45
player_y_speed = 0

# cord_&_velocity_player 2
player2_x_coord = 750 - player_width
player2_y_coord = 300 - 45
player2_y_speed = 0

# ball
ball_x = 400
ball_y = 300
ball_x_speed = 3
ball_y_speed = 3

game_over = False

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        if event.type == pygame.KEYDOWN:
            # player 1
            if event.key == pygame.K_w:
                player_y_speed = -3
            if event.key == pygame.K_s:
                player_y_speed = 3
            # player 2
            if event.key == pygame.K_UP:
                player2_y_speed = -3
            if event.key == pygame.K_DOWN:
                player2_y_speed = 3
        if event.type == pygame.KEYUP:
            # player 1
            if event.key == pygame.K_w:
                player_y_speed = 0
            if event.key == pygame.K_s:
                player_y_speed = 0
            # player 2
            if event.key == pygame.K_UP:
                player2_y_speed = 0
            if event.key == pygame.K_DOWN:
                player2_y_speed = 0

    # bound
    if ball_y > 590 or ball_y < 10:
        ball_y_speed *= -1

    if ball_x > 800:
        score1 += 1
        print(score1)
        ball_x = 400
        ball_y = 300
        # go out to right screen invert direction
        ball_x_speed *= -1
        ball_y_speed *= -1

    # bound
    if ball_x < 0:
        score2 += 1
        print(score2)
        ball_x = 400
        ball_y = 300
        # go out to left screen invert direction
        ball_x_speed *= -1
        ball_y_speed *= -1

    # modify cord - movement player
    player_y_coord += player_y_speed
    player2_y_coord += player2_y_speed
    # movement ball
    ball_x += ball_x_speed
    ball_y += ball_y_speed

    screen.fill(green)
    pygame.draw.rect(screen, white, (0, 300, 800, 300), 2)
    # Draw zone

    player1 = pygame.draw.rect(screen, white, (player_x_coord, player_y_coord, player_width, player_height))
    player2 = pygame.draw.rect(screen, white, (player2_x_coord, player2_y_coord, player_width, player_height))
    ball = pygame.draw.circle(screen, white, (ball_x, ball_y), 10)

    # collision ball
    if ball.colliderect(player1) or ball.colliderect(player2):
        ball_x_speed *= -1

    if score1 > 2:
        print("Game over, player1 Wins")
        game_over = True
    if score2 > 2:
        print("Game over, player2 Wins")
        game_over = True

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
