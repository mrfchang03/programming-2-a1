# Donkey Shmup
# Matthew Chang
# reference code from Pygame
# Import modules
import pygame
import random
import math

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
BLACK_SCREEN= (0, 0, 0)
WHITE = (246, 246, 246)

# Constants and game options
FPS = 60
BGCOLOUR = BLACK_SCREEN
AMOUNT_OF_LIVES = 5
ENEMY_SPEED_MULTIPLIER = 1
BULLET_SPEED_MULTIPLIER = 1
MUSH_SPAWN_RATE = 5

MAX_BULLETS = 50
MAX_ENEMIES = 40
SCREEN_WIDTH = 1024
SCREEN_HEIGHT = 768


# --- Classes


class Enemy(pygame.sprite.Sprite):
    """ enemy class"""

    def __init__(self):
        """ enemy creation """
        super().__init__()

        self.image = pygame.image.load("./63b0dbdcdc45a0b.png")
        # scale sprite
        self.image = pygame.transform.scale(self.image, (80, 80))
        # set key to black
        self.image.set_colorkey(BLACK)

        self.rect = self.image.get_rect()

        # set initial velocity
        x = ENEMY_SPEED_MULTIPLIER
        self.vel_x = random.choice([-3 * x, -2 * x, 2 * x, 3 * x])
        self.vel_y = random.choice([-3 * x, -2 * x, 2 * x, 3 * x])

    def update(self):
        """ move the enemy """
        self.rect.x += self.vel_x
        self.rect.y += self.vel_y

        # keep enemy inside the screen
        if self.rect.top < 0 or self.rect.bottom > SCREEN_HEIGHT:
            self.vel_y = -self.vel_y
        if self.rect.left < 0 or self.rect.right > SCREEN_WIDTH:
            self.vel_x = -self.vel_x


class Player(pygame.sprite.Sprite):
    """ player class """

    def __init__(self):
        """ player set up """
        # Call the parent class constructor
        super().__init__()

        self.image = pygame.image.load("./593b62a3e02268b.png").convert()
        # scale sprite
        self.image = pygame.transform.scale(self.image, (60, 60))

        # set colour to white
        self.image.set_colorkey(WHITE)

        self.rect = self.image.get_rect()

        # max velocity
        self.vel_magnitude = 3

        self.vel_x = 0
        self.vel_y = 0

    def update(self):
        """ movement with wasd """
        # go in direction when key is pressed
        # go up
        if pygame.key.get_pressed()[pygame.K_w]:
            if self.rect.top < 0:
                self.vel_y = 0
            # prevent player from going out of boundaries
            else:
                self.vel_y = -self.vel_magnitude
        # go down
        elif pygame.key.get_pressed()[pygame.K_s]:
            if self.rect.bottom > SCREEN_HEIGHT:
                self.vel_y = 0
            # prevent player from going out of boundaries
            else:
                self.vel_y = self.vel_magnitude
        # stay still when no key is pressed
        else:
            self.vel_y = 0

        # go left
        if pygame.key.get_pressed()[pygame.K_a]:
            if self.rect.left < 0:
                self.vel_x = 0
            # prevent player from going out of boundaries
            else:
                self.vel_x = -self.vel_magnitude
        elif pygame.key.get_pressed()[pygame.K_d]:
            if self.rect.right > SCREEN_WIDTH:
                self.vel_x = 0
            else:
                self.vel_x = self.vel_magnitude
        # stay still when no key is pressed
        else:
            self.vel_x = 0
        # move 
        self.rect.y += self.vel_y
        self.rect.x += self.vel_x


class Bullet(pygame.sprite.Sprite):
    """ bullet class """

    def __init__(self, start_x, start_y, dest_x, dest_y):

        super().__init__()

        # Bullet
        self.image = pygame.image.load("./bullet.png")
        # scale sprite
        self.image = pygame.transform.scale(self.image, (20, 20))

        self.image.set_colorkey(BLACK)

        self.rect = self.image.get_rect()

        # Move the bullet to our starting location
        self.rect.x = start_x
        self.rect.y = start_y

        # Make aiming more accurate
        self.floating_point_x = start_x
        self.floating_point_y = start_y

        # Calculate what angle the bullet will travel at
        x_diff = dest_x - start_x
        y_diff = dest_y - start_y
        angle = math.atan2(y_diff, x_diff);

        # calculate the change in both x and y with the given angle found earlier
        velocity = 7 * BULLET_SPEED_MULTIPLIER
        self.change_x = math.cos(angle) * velocity
        self.change_y = math.sin(angle) * velocity

    def update(self):
        """ Move the bullet. """

        # floating x and y is more accurate
        self.floating_point_y += self.change_y
        self.floating_point_x += self.change_x

        # convert the rect x and y to integers
        self.rect.y = int(self.floating_point_y)
        self.rect.x = int(self.floating_point_x)

        # kill bullet when out of screen
        if self.rect.x < 0 or self.rect.x > SCREEN_WIDTH or self.rect.y < 0 or self.rect.y > SCREEN_HEIGHT:
            self.kill()


class Health(pygame.sprite.Sprite):
    """ Health Class"""

    def __init__(self):

        super().__init__()

        # Health
        self.image = pygame.image.load("./mush.png")
        # scale sprite
        self.image = pygame.transform.scale(self.image, (30, 30))

        self.image.set_colorkey(WHITE)

        self.rect = self.image.get_rect()


# --- Create the window

# Initialize Pygame
pygame.init()

# Variables
score = 0
lives = AMOUNT_OF_LIVES
level = 1

# Font setup
pygame.font.init()
font = pygame.font.SysFont('Times New Roman', 25)

# Set the height and width of the screen

screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])

# --- Sprite lists

# List of every single sprite
all_sprites_list = pygame.sprite.Group()

# List of each enemy in the game
enemy_list = pygame.sprite.Group()

# List of each bullet
bullet_list = pygame.sprite.Group()

health_list = pygame.sprite.Group()

# --- Create the sprites
for i in range(1):
    # This represents a enemy
    enemy = Enemy()

    # Random enemy spawn on screen
    enemy.rect.x = random.randrange(SCREEN_WIDTH - 50)
    enemy.rect.y = random.randrange(SCREEN_HEIGHT - 50)

    # Add the enemy to the list of objects
    enemy_list.add(enemy)
    all_sprites_list.add(enemy)

# Create the player
player = Player()
all_sprites_list.add(player)

# player spawns in centre of screen
player.rect.x = SCREEN_WIDTH / 2
player.rect.y = SCREEN_HEIGHT / 2

# Loop until game ends or closes by user
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# -------- Main Program Loop -----------
while not done:
    # --- Game logic

    # update all the sprites
    all_sprites_list.update()


    for bullet in bullet_list:

        # See if it hit a enemy
        enemy_hit_list = pygame.sprite.spritecollide(bullet, enemy_list, True)

        # Kill the bullet and add a score for each
        for enemy in enemy_hit_list:
            bullet_list.remove(bullet)
            all_sprites_list.remove(bullet)
            score += 1

        # kill bullet when off screen
        if bullet.rect.y < -10:
            bullet_list.remove(bullet)
            all_sprites_list.remove(bullet)

    # kill enemy when hit
    enemy_hit_list = pygame.sprite.spritecollide(
        player,
        enemy_list,
        True
    )


    for health in health_list:

        # collision with sprite
        health_hit_list = pygame.sprite.spritecollide(player, health_list, True)

        # for each collision, max the health
        for health in health_hit_list:
            health_list.remove(health)
            all_sprites_list.remove(health)
            lives = 5

    # for each enemy killed, add another
    for hit in enemy_hit_list:
        lives -= 1

        enemy = Enemy()
        # determine initial location
        enemy.rect.x, enemy.rect.y = [
            random.randrange(50, SCREEN_WIDTH - 50),
            random.randrange(50, SCREEN_HEIGHT - 50)
        ]

        # add enemies to lists
        enemy_list.add(enemy)
        all_sprites_list.add(enemy)

    # once old wave is dead, spawn in the next one
    if not enemy_list:
        level += 1
        enemy_amount = pow(2, level)

        # cap the amount of enemies spawned
        if enemy_amount >= MAX_ENEMIES:
            enemy_amount = MAX_ENEMIES

        # spawn enemies
        for i in range(enemy_amount):
            # This represents an enemy
            enemy = Enemy()

            # random location of enemy
            enemy.rect.x = random.randrange(SCREEN_WIDTH - 100)
            enemy.rect.y = random.randrange(SCREEN_HEIGHT - 100)

            # Add enemy to list
            enemy_list.add(enemy)
            all_sprites_list.add(enemy)

        # spawn health potion
        if level % MUSH_SPAWN_RATE == 0:

            health = Health()

            # random location for the health
            health.rect.x = random.randrange(SCREEN_WIDTH - 100)
            health.rect.y = random.randrange(SCREEN_HEIGHT - 100)

            # Add the enemy to the list
            health_list.add(health)
            all_sprites_list.add(health)

    # --- Event Processing
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

        # only fire bullet if it's under the max amount of bullets
        if len(bullet_list) <= MAX_BULLETS:
            if event.type == pygame.MOUSEBUTTONDOWN:
                # Fire a bullet if the user clicks the mouse button


                pos = pygame.mouse.get_pos()
                mouse_x = pos[0]
                mouse_y = pos[1]

                # Different gun modes
                if level <= 3:

                    bullet = Bullet(player.rect.x, player.rect.y, mouse_x, mouse_y)

                    # Add the bullet to the lists
                    all_sprites_list.add(bullet)
                    bullet_list.add(bullet)

                elif level > 3 and level <= 9:
                    # Call the class to create the projectiles
                    bullet_0 = Bullet(player.rect.x, player.rect.y, mouse_x, mouse_y)
                    bullet_1 = Bullet(player.rect.x, player.rect.y, mouse_x - 10, mouse_y - 10)



                    all_sprites_list.add(bullet_0, bullet_1)
                    bullet_list.add(bullet_0, bullet_1)

                elif level > 9 and level <= 15:
                    # Call the class to create the projectiles
                    bullet_0 = Bullet(player.rect.x, player.rect.y, mouse_x, mouse_y)
                    bullet_1 = Bullet(player.rect.x, player.rect.y, mouse_x - 20, mouse_y - 20)
                    bullet_2 = Bullet(player.rect.x, player.rect.y, mouse_x + 20, mouse_y + 20)
                    bullet_3 = Bullet(player.rect.x, player.rect.y, mouse_x + 90, mouse_y + 90)
                    bullet_4 = Bullet(player.rect.x, player.rect.y, mouse_x - 90, mouse_y - 90)

                    # Add the bullet to the lists
                    all_sprites_list.add(bullet_0, bullet_1, bullet_2, bullet_3)
                    bullet_list.add(bullet_0, bullet_1, bullet_2, bullet_3)

                elif level > 15:
                    # Call the class to create the projectiles
                    bullet_0 = Bullet(player.rect.x, player.rect.y, mouse_x, mouse_y)
                    bullet_1 = Bullet(player.rect.x, player.rect.y, mouse_x - 10, mouse_y - 10)
                    bullet_2 = Bullet(player.rect.x, player.rect.y, mouse_x + 10, mouse_y + 10)
                    bullet_3 = Bullet(player.rect.x, player.rect.y, mouse_x + 180, mouse_y + 180)
                    bullet_4 = Bullet(player.rect.x, player.rect.y, mouse_x + 90, mouse_y + 90)
                    bullet_5 = Bullet(player.rect.x, player.rect.y, mouse_x - 90, mouse_y - 90)
                    bullet_6 = Bullet(player.rect.x, player.rect.y, mouse_x + 45, mouse_y + 45)
                    bullet_7 = Bullet(player.rect.x, player.rect.y, mouse_x - 45, mouse_y - 45)

                    # Add the bullet to the lists
                    all_sprites_list.add(bullet_0, bullet_1, bullet_2, bullet_3, bullet_4, bullet_5, bullet_6, bullet_7)
                    bullet_list.add(bullet_0, bullet_1, bullet_2, bullet_3, bullet_4, bullet_5, bullet_6, bullet_7)

    # Endgame
    if lives < 0:
        print(f"""
        Nice try, you finished on level {level} with a score of {score}.
        Play again?
                """)
        done = True

    # --- Draw a frame

    # Clear the screen
    screen.fill(BGCOLOUR)

    # Draw all the sprites
    all_sprites_list.draw(screen)

    # draw the score and lives

    score_surface = font.render(f"Score: {score}", False, WHITE)
    lives_surface = font.render(f"Lives: {lives}", False, WHITE)
    level_surface = font.render(f"Level: {level}", False, WHITE)

    # blit(surface, coordinates)
    screen.blit(score_surface, [10, 10])
    screen.blit(lives_surface, [10, 30])
    screen.blit(level_surface, [10, 50])

    # Update screen
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(FPS)

pygame.quit()
