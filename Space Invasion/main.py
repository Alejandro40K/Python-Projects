"""
main.py

Description:
    This script implements a classic arcade-style space shooter game using the Pygame library.
    The player controls a spaceship that can move horizontally and shoot bullets to destroy
    descending enemies. Enemies reappear randomly upon being destroyed. The game features
    background music, sound effects, score tracking, and an end-game condition.

Author: Alejandro Orozco Romo
Created: 2025-07-05
Last Modified: 2025-07-06
Python Version: 3.9

Dependencies:
    - pygame: for graphics, game loop, event handling, and rendering
    - random: for generating random enemy positions
    - math: for calculating the distance between enemies and bullets
    - pygame.mixer: for music and sound effects

License:
    MIT License

Notes:
    - Events: Everything that happens on the Pygame screen (keyboard input, rendering, collisions, etc.).
"""
import io

import pygame
import random
import math
from pygame import mixer

# Initialize py
pygame.init()

# Set screen size
screen = pygame.display.set_mode((800, 600))
is_excecuted = True

# ----------------------------------------
# Title, background and icon
# ----------------------------------------
pygame.display.set_caption("Space Invasion")
icon = pygame.image.load("ovni.png")
pygame.display.set_icon(icon)
background = pygame.image.load("Fondo.jpg")

# Add music
mixer.music.load('MusicaFondo.mp3')  # Load music
mixer.music.set_volume(0.1)
mixer.music.play(-1)  # The music starts, its repeats every time the game stats

# ----------------------------------------
# Player Variables
# ----------------------------------------
# Player image
img_player = pygame.image.load("cohete.png")
# Initial player position
player_x = 368
player_y = 500
player_x_change = 0


# ----------------------------------------
# Enemy Variables
# ----------------------------------------
# Enemy image
img_enemy = []
# Initial random enemy position
enemy_x = []
enemy_y = []
enemy_x_change = []
enemy_y_change = []
enemies_numbers = 20

for enemies in range(enemies_numbers):
    img_enemy.append(pygame.image.load("enemigo.png"))
    enemy_x.append(random.randint(0, 736))
    enemy_y.append(random.randint(50, 200))
    enemy_x_change.append(0.4)   # the enemy change his position
    enemy_y_change.append(40)  # How many pixels are moved per iteration


# ----------------------------------------
# Bullet Variables
# ----------------------------------------
bullets = []

# Enemy image
img_bullet = pygame.image.load("bala.png")

# Initial random enemy position
bullet_x = 0
bullet_y = 500  # height of the ship
bullet_x_change = 0
bullet_y_change = 3
visible_bullet = False


def font_bytes(font):
    with open(font,'rb') as f:
        ttf_bytes =f.read()
        return io.BytesIO(ttf_bytes)


# Score
score = 0
fuente_como_bytes = font_bytes('freesansbold.ttf')
source = pygame.font.Font(fuente_como_bytes , 32)
text_x = 10
text_y = 10

# Final text game
final_source = pygame.font.Font(fuente_como_bytes, 40)


# Final text function
def final_text():
    """
    Displays the 'END GAME' message on the screen at a fixed position.

    :return: None
    """
    my_final_source = final_source.render("END GAME", True, (255, 255, 255))
    screen.blit(my_final_source, (300, 200))


# Score function
def show_score(x, y):
    """
    Renders and displays the current score at the specified (x, y) coordinates on the screen.

    :param x: The x-coordinate where the score will be displayed
    :param y: The y-coordinate where the score will be displayed
    :return: None
    """
    text = source.render(f"Score: {score}", True, (255, 255, 255))  # print in screen
    screen.blit(text, (x, y))


# Player function
def player(x, y):
    """
    Draws the player (spaceship) at the given coordinates on the screen.

    :param x: The x-coordinate of the player's position
    :param y: The y-coordinate of the player's position
    :return: None
    """
    # Render the player image on the screen at (x, y)
    screen.blit(img_player, (x, y))


# Enemy function
def enemies(x, y, enemy):
    """
    Draws the enemies (spaceship) at the given coordinates on the screen.

    :param x: The x-coordinate of the enemies position
    :param y: The y-coordinate of the enemies position
    :param enemy: The index of the enemy to draw (used to access its image)
    :return: None
    """
    # Render the enemy image on the screen at (x, y)
    screen.blit(img_enemy[enemy], (x, y))


# Shoot bullet function
def shoot_bullet(x, y):
    """
    Displays the bullet image on the screen at a position slightly in front of the player.

    :param x: The x-coordinate of the player's position
    :param y: The y-coordinate of the player's position
    :return: None
    """
    # Show and chargue the bullet
    global visible_bullet
    visible_bullet = True
    # The bullet is showsn at  position x = 16 in front of ship and y + 10 in the middle of the ship
    screen.blit(img_bullet, (x + 16, y + 10))


# Detect collisions function
def detect_collisions(x1, y1, x2, y2):
    """
    Checks for a collision between two objects based on their coordinates using Euclidean distance.

    :param x1: The x-coordinate of the first object (e.g., enemy)
    :param y1: The y-coordinate of the first object
    :param x2: The x-coordinate of the second object (e.g., bullet)
    :param y2: The y-coordinate of the second object
    :return: True if the distance between objects is less than 27 pixels, False otherwise
    """
    # the result of the distance will be a number of pixels
    distance = math.sqrt(math.pow(x2 - x1, 2) + math.pow(y2 - y1, 2))
    if distance < 27:
        return True
    else:
        return False


# Reapper enemy function
def reappear_enemy():
    """
    Generates and returns a new random (x, y) position for an enemy within the screen bounds.

    :return: A tuple (en_x, en_y) representing the new enemy coordinates
    """
    en_x = random.randint(0, 736)
    en_y = random.randint(50, 200)
    return en_x, en_y


# ----------------------------------------
# Main Game Loop
# ----------------------------------------
while is_excecuted:

    # Change wallpaper
    screen.blit(background, (0, 0))
    # screen.fill((205,144,228))

    # Iterate events
    for event in pygame.event.get():
        # Close program
        if event.type == pygame.QUIT:
            is_excecuted = False

        # Control player movement keyboard

        # Arrow key press event
        if event.type == pygame.KEYDOWN:
            print("a key was pressed")

            if event.key == pygame.K_LEFT:
                print("left arrow pressed")
                player_x_change = -1  # Modifi these values to increase speed

            if event.key == pygame.K_RIGHT:
                print("right arrow pressed")
                player_x_change = 1

            if event.key == pygame.K_SPACE:
                bullet_sound = mixer.Sound('disparo.mp3')
                bullet_sound.play()
                new_bullet = {
                    "x": player_x,
                    "y": player_y,
                    "speed": -5
                }
                bullets.append(new_bullet)

                if not visible_bullet:
                    bullet_x = player_x  # separate bullet of player
                    shoot_bullet(bullet_x, bullet_y)

        # Arrow key release event
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                print("arrow was relassed ")
                player_x_change = 0

    # Update player position x
    player_x += player_x_change

    # Keep the player on the edges
    if player_x <= 0:  # pixels
        player_x = 0
    elif player_x >= 736:
        player_x = 736

    # Update enemy position x
    for e in range(enemies_numbers):

        # End Game
        if enemy_y[e] > 500:
            for k in range(enemies_numbers):
                enemy_y[k] = 1000  # Sen out to hide
            final_text()
            break

        enemy_x[e] += enemy_x_change[e]

        # Keep the enemy on the edges
        if enemy_x[e] <= 0:  # pixels
            enemy_x_change[e] = 1  # change the movement
            enemy_y[e] += enemy_y_change[e]
        elif enemy_x[e] >= 736:
            enemy_x_change[e] = -1
            enemy_y[e] += enemy_y_change[e]

        # Collision
        for bullet in bullets[:]:  # iterar sobre copia
            collision = detect_collisions(enemy_x[e], enemy_y[e], bullet["x"], bullet["y"])
            if collision:
                collision_sound = mixer.Sound('Golpe.mp3')
                collision_sound.play()
                bullets.remove(bullet)
                score += 1
                print(f"Score: {score}")
                enemy_x[e], enemy_y[e] = reappear_enemy()
                break  # salta a siguiente enemigo para evitar múltiples colisiones simultáneas

        enemies(enemy_x[e], enemy_y[e], e)

    # Bullet movement
    for bullet in bullets[:]:  # ← iterar sobre copia para poder eliminar sin error
        bullet["y"] += bullet["speed"]
        screen.blit(img_bullet, (bullet["x"] + 16, bullet["y"] + 10))

        # Eliminar bala si sale de pantalla
        if bullet["y"] < 0:
            bullets.remove(bullet)

    player(player_x, player_y)

    # Show the score
    show_score(text_x, text_y)

    # Update all events
    pygame.display.update()
