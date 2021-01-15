# rectanglepractive.py
#get practice with OOP and pygame
import pygame
# ----- CONSTANTS
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
SKY_BLUE = (95, 165, 228)
WIDTH = 800
HEIGHT = 600
TITLE = "<You're title here>"
# CREATE A RECTANGLE CLASS
class Rectangle():
    def __init__(self):
        self.width = 10
        self.height = 10
        self.x = 10
        self.y = 10
        self.colour = WHITE
def main():
    pygame.init()
    # ----- SCREEN PROPERTIES
    size = (WIDTH, HEIGHT)
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption(TITLE)
    # ----- LOCAL VARIABLES
    done = False
    clock = pygame.time.Clock()
    # CREATE A RECTANGLE ~OBJECT~
    #   * RED
    #   * 10 px WIDE by 40 px high
    #   * (0,0)
    first_rectangle = Rectangle()
    first_rectangle.colour = (255, 0, 0)
    first_rectangle.width = 10
    first_rectangle.height = 40
    first_rectangle.x , first_rectangle.y = (0, 0)
    # ----- MAIN LOOP
    while not done:
        # -- Event Handler
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
        # ----- LOGIC
        # ----- DRAW
        screen.fill(BLACK)
        # Draw the rectangle object
        pygame.draw.rect(
            screen,
            first_rectangle.colour,
            (
                first_rectangle.x,
                first_rectangle.y,
                first_rectangle.width,
                first_rectangle.height
            )
         )
        # ----- UPDATE
        pygame.display.flip()
        clock.tick(60)
    pygame.quit()
if __name__ == "__main__":
    main()
# rectanglepractive.py
#get practice with OOP and pygame
import pygame
# ----- CONSTANTS
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
SKY_BLUE = (95, 165, 228)
WIDTH = 800
HEIGHT = 600
TITLE = "<You're title here>"
# CREATE A RECTANGLE CLASS
class Rectangle():
    def __init__(self):
        self.width = 10
        self.height = 10
        self.x = 10
        self.y = 10
        self.colour = WHITE
def main():
    pygame.init()
    # ----- SCREEN PROPERTIES
    size = (WIDTH, HEIGHT)
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption(TITLE)
    # ----- LOCAL VARIABLES
    done = False
    clock = pygame.time.Clock()
    # CREATE A RECTANGLE ~OBJECT~
    #   * RED
    #   * 10 px WIDE by 40 px high
    #   * (0,0)
    first_rectangle = Rectangle()
    first_rectangle.colour = (255, 0, 0)
    first_rectangle.width = 10
    first_rectangle.height = 40
    first_rectangle.x , first_rectangle.y = (0, 0)
    # ----- MAIN LOOP
    while not done:
        # -- Event Handler
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
        # ----- LOGIC
        # ----- DRAW
        screen.fill(BLACK)
        # Draw the rectangle object
        pygame.draw.rect(
            screen,
            first_rectangle.colour,
            (
                first_rectangle.x,
                first_rectangle.y,
                first_rectangle.width,
                first_rectangle.height
            )
         )
        # ----- UPDATE
        pygame.display.flip()
        clock.tick(60)
    pygame.quit()
if __name__ == "__main__":
    main()