# Introduction to the Sprite class


import pygame
import random

# ----- CONSTANTS
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
SKY_BLUE = (95, 165, 228)
WIDTH = 1920
HEIGHT = 1080
TITLE = "Sprite Example"
NUM_JEWELS = 75
class Jewel(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.image = pygame.Surface((35, 20))
        self.image.fill((100, 255, 100))

        self.rect = self.image.get_rect()
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("./images/link.png")
        self.rect = self.image.get_rect()

    def update(self):
        self.rect.center = pygame.mouse.get_pos()
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

def main():
    pygame.init()

    # ----- SCREEN PROPERTIES
    size = (WIDTH, HEIGHT)
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption(TITLE)

    # ----- LOCAL VARIABLES
    done = False
    clock = pygame.time.Clock()
    score = 0


    all_sprites_group = pygame.sprite.Group()
    jewels_group = pygame.sprite.Group()

    for i in range(NUM_JEWELS):
        jewel = Jewel()
        jewel.rect.x = random.randrange(WIDTH - jewel.rect.width)
        jewel.rect.y = random.randrange(HEIGHT - jewel.rect.height)
        all_sprites_group.add(jewel)

    player = Player()
    all_sprites_group.add(player)
    # ----- MAIN LOOP
    while not done:
        # -- Event Handler
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

        # ----- LOGIC
        all_sprites_group.update()

        jewels_collected = pygame.sprit.spritcollide(player, jewels_group, True)
        for jewel in jewels_collected:
            score += 1
            print(score)
        # ----- DRAW
        screen.fill(BLACK)
        all_sprites_group.draw(screen)
        # ----- UPDATE
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()


if __name__ == "__main__":
    main()
