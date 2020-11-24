import pygame
import sys

WIDTH = 800
HEIGHT = 600

FPS = 60

COLOR_BLACK = (0, 0, 0)
COLOR_RED = (255, 0, 0)
COLOR_WHITE = (255, 255, 255)
COLOR_GREEN = (0, 255, 0)

class Laser:
    def __init__(self, x, y):
        self.x=x
        self.y=y
    def draw(self, window):
        pygame.draw.rect(window, COLOR_GREEN, (self.x, self.y, 5, 2))
    def move(self, speed):
        self.y+=speed

class Alien:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self, window):
        pygame.draw.rect(window, COLOR_GREEN, (self.x, self.y, 40, 40))

    def movement(self, speed):
        self.y += speed

class Player:
    playerspeed = 4
    cooldown = 30
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.lasers = []

    def draw(self, window):
        pygame.draw.rect(window, COLOR_WHITE, (self.x, self.y, 50, 10))
        for i in self.lasers:
            i.draw(window)

    def move_left(self):
        self.x-= self.playerspeed
        if self.x<=50:
            self.x = 50

    def move_right(self):
        self.x+= self.playerspeed
        if self.x>=700:
            self.x = 700

    def shoot(self):
        if self.cool_down_counter == 0:
            laser = Laser(self.x, self.y)
            self.lasers.append(laser)
            self.cool_down_counter = 1


def main():
    # Initialize imported pygame modules
    pygame.init()

    # Set the window's caption
    pygame.display.set_caption("Space Invaders")

    clock = pygame.time.Clock()

    screen = pygame.display.set_mode((WIDTH, HEIGHT))

    background = pygame.Surface((WIDTH, HEIGHT))
    background = background.convert()
    background.fill(COLOR_BLACK)

    # Blit everything to screen
    screen.blit(background, (0, 0))

    # Update the screen
    pygame.display.flip()


    aliens = []
    for i in range(1, 4):
        for j in range(1, 7):
            alien = Alien(100*j, 75*i)
            aliens.append(alien)
    player = Player(375, 500)


    # Main loop
    while True:
        clock.tick(FPS)

        # Erase everything drawn at last step by filling the background
        # with color black
        background.fill(COLOR_BLACK)

        player.draw(background)
        for i in aliens:
            i.draw(background)

        # Check for Quit event
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Check for key presses and update paddles accordingly
        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[pygame.K_a]:
            # Do something
            player.move_left()
        if keys_pressed[pygame.K_d]:
            # Do something
            player.move_right()
        if keys_pressed[pygame.K_SPACE]:
            player.shoot()

        for alien in aliens:
            alien.movement(0.1)

        # Update game state

        # Render current game state
        pygame.display.flip()
        screen.blit(background, (0, 0))


if __name__ == '__main__':
    main()
