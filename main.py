import pygame
print("Pygame installed!")
import pygame
import random

pygame.init()

# =========================
# SCREEN
# =========================
WIDTH = 400
HEIGHT = 700

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mobile Car Racing")

clock = pygame.time.Clock()

# =========================
# COLORS
# =========================
GREEN = (40, 150, 40)
ROAD = (55, 55, 55)
WHITE = (255, 255, 255)
BLUE = (30, 100, 220)
RED = (220, 40, 40)
YELLOW = (240, 200, 20)
BLACK = (0, 0, 0)
GRAY = (120, 120, 120)

# =========================
# FONT
# =========================
font = pygame.font.Font(None, 40)
big_font = pygame.font.Font(None, 65)

# =========================
# CAR SETTINGS
# =========================
CAR_WIDTH = 50
CAR_HEIGHT = 90

player_x = 175
player_y = 550

player_speed = 7

# =========================
# ENEMY SETTINGS
# =========================
enemy_x = random.randint(80, 270)
enemy_y = -120

enemy_speed = 6

score = 0

# =========================
# TOUCH BUTTONS
# =========================
left_button = pygame.Rect(30, 590, 140, 80)
right_button = pygame.Rect(230, 590, 140, 80)

# =========================
# GAME VARIABLES
# =========================
running = True
game_over = False

move_left = False
move_right = False


# =========================
# RESET GAME
# =========================
def reset_game():
    global player_x
    global enemy_x
    global enemy_y
    global enemy_speed
    global score
    global game_over

    player_x = 175

    enemy_x = random.randint(80, 270)
    enemy_y = -120

    enemy_speed = 6
    score = 0

    game_over = False


# =========================
# MAIN GAME LOOP
# =========================
while running:

    clock.tick(60)

    # =====================
    # EVENTS
    # =====================
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        # Touch / mouse
        if event.type == pygame.MOUSEBUTTONDOWN:

            x, y = event.pos

            if not game_over:

                if left_button.collidepoint(x, y):
                    move_left = True

                if right_button.collidepoint(x, y):
                    move_right = True

            else:

                # Tap screen to restart
                reset_game()

        if event.type == pygame.MOUSEBUTTONUP:

            move_left = False
            move_right = False

    # =====================
    # GAME
    # =====================
    if not game_over:

        # Move player
        if move_left:
            player_x -= player_speed

        if move_right:
            player_x += player_speed

        # Keep player on road
        if player_x < 65:
            player_x = 65

        if player_x > 285:
            player_x = 285

        # =================
        # ENEMY MOVEMENT
        # =================
        enemy_y += enemy_speed

        # Enemy passed
        if enemy_y > HEIGHT:

            enemy_y = -120
            enemy_x = random.randint(70, 280)

            score += 1

            # Increase difficulty
            if score % 5 == 0:
                enemy_speed += 1

        # =================
        # COLLISION
        # =================
        player_rect = pygame.Rect(
            player_x,
            player_y,
            CAR_WIDTH,
            CAR_HEIGHT
        )

        enemy_rect = pygame.Rect(
            enemy_x,
            enemy_y,
            CAR_WIDTH,
            CAR_HEIGHT
        )

        if player_rect.colliderect(enemy_rect):

            game_over = True

    # =====================
    # DRAW BACKGROUND
    # =====================

    screen.fill(GREEN)

    # Road
    pygame.draw.rect(
        screen,
        ROAD,
        (50, 0, 300, HEIGHT)
    )

    # Road borders
    pygame.draw.rect(
        screen,
        WHITE,
        (50, 0, 8, HEIGHT)
    )

    pygame.draw.rect(
        screen,
        WHITE,
        (342, 0, 8, HEIGHT)
    )

    # =====================
    # ROAD LINES
    # =====================

    for y in range(-100, HEIGHT, 100):

        pygame.draw.rect(
            screen,
            WHITE,
            (195, y, 10, 50)
        )

    # =====================
    # PLAYER CAR
    # =====================

    pygame.draw.rect(
        screen,
        BLUE,
        (
            player_x,
            player_y,
            CAR_WIDTH,
            CAR_HEIGHT
        )
    )

    # Player windows
    pygame.draw.rect(
        screen,
        (120, 200, 240),
        (
            player_x + 8,
            player_y + 10,
            34,
            25
        )
    )

    # Player wheels
    pygame.draw.rect(
        screen,
        BLACK,
        (
            player_x - 5,
            player_y + 15,
            7,
            25
        )
    )

    pygame.draw.rect(
        screen,
        BLACK,
        (
            player_x + 48,
            player_y + 15,
            7,
            25
        )
    )

    pygame.draw.rect(
        screen,
        BLACK,
        (
            player_x - 5,
            player_y + 55,
            7,
            25
        )
    )

    pygame.draw.rect(
        screen,
        BLACK,
        (
            player_x + 48,
            player_y + 55,
            7,
            25
        )
    )

    # =====================
    # ENEMY CAR
    # =====================

    pygame.draw.rect(
        screen,
        RED,
        (
            enemy_x,
            enemy_y,
            CAR_WIDTH,
            CAR_HEIGHT
        )
    )

    # Enemy window
    pygame.draw.rect(
        screen,
        (250, 180, 180),
        (
            enemy_x + 8,
            enemy_y + 10,
            34,
            25
        )
    )

    # =====================
    # SCORE
    # =====================

    score_text = font.render(
        "Score: " + str(score),
        True,
        WHITE
    )

    screen.blit(
        score_text,
        (10, 10)
    )

    # =====================
    # TOUCH BUTTONS
    # =====================

    pygame.draw.rect(
        screen,
        GRAY,
        left_button
    )

    pygame.draw.rect(
        screen,
        GRAY,
        right_button
    )

    # LEFT text
    left_text = font.render(
        "LEFT",
        True,
        WHITE
    )

    screen.blit(
        left_text,
        (
            left_button.x + 35,
            left_button.y + 20
        )
    )

    # RIGHT text
    right_text = font.render(
        "RIGHT",
        True,
        WHITE
    )

    screen.blit(
        right_text,
        (
            right_button.x + 25,
            right_button.y + 20
        )
    )

    # =====================
    # GAME OVER
    # =====================

    if game_over:

        overlay = pygame.Surface(
            (WIDTH, HEIGHT)
        )

        overlay.set_alpha(170)
        overlay.fill(BLACK)

        screen.blit(
            overlay,
            (0, 0)
        )

        game_over_text = big_font.render(
            "GAME OVER",
            True,
            RED
        )

        screen.blit(
            game_over_text,
            (
                70,
                250
            )
        )

        final_score = font.render(
            "Score: " + str(score),
            True,
            WHITE
        )

        screen.blit(
            final_score,
            (
                145,
                330
            )
        )

        restart_text = font.render(
            "Tap to Restart",
            True,
            YELLOW
        )

        screen.blit(
            restart_text,
            (
                105,
                400
            )
        )

    pygame.display.update()


pygame.quit()