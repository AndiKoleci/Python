import pygame
import sys
from random import randint

WIDTH = 800
HEIGHT = 600
FPS = 60
COLOR_BLACK = (0, 0, 0)
COLOR_RED = (255, 0, 0)
COLOR_WHITE = (255, 255, 255)
COLOR_GREEN = (0, 255, 0)


# CONTROLS AND GAMEPLAY
# USE A AND D TO MOVE, USE SPACE TO SHOOT
# GOOD LUCK AND START SHOOTING!

class Block:
    count = 10

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self, window):
        pygame.draw.rect(window, COLOR_GREEN, (self.x, self.y, 90, 40))

    def collision(self):
        self.count -= 1


class Laser:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self, window):
        pygame.draw.rect(window, COLOR_WHITE, (self.x, self.y, 4, 12))

    def move(self, speed):
        self.y -= speed


class Alien:
    lasers = []
    alien_direction = 1

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self, window):
        pygame.draw.rect(window, COLOR_GREEN, (self.x, self.y, 40, 40))

    def movement(self, speed):
        self.y += speed
        self.x += speed * 10 * self.alien_direction

    def shoot(self):
        laser = Laser(self.x + 18, self.y)
        self.lasers.append(laser)


class Player:
    playerspeed = 4
    cooldown = 30
    lasers = []

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.lasers = []

    def draw(self, window):
        pygame.draw.rect(window, COLOR_WHITE, (self.x, self.y, 50, 10))
        for i in self.lasers:
            i.draw(window)

    def move_left(self):
        self.x -= self.playerspeed
        if self.x <= 50:
            self.x = 50

    def move_right(self):
        self.x += self.playerspeed
        if self.x >= 700:
            self.x = 700

    def shoot(self):
        if self.cooldown <= 0:
            self.cooldown = 30
            laser = Laser(self.x + 23, self.y)
            self.lasers.append(laser)


def main():
    # Initialize imported pygame modules
    pygame.init()
    end_cd = 90
    alien_cd = 180

    # Set the window's caption
    pygame.display.set_caption("Space Invaders Lite")

    clock = pygame.time.Clock()

    screen = pygame.display.set_mode((WIDTH, HEIGHT))

    background = pygame.Surface((WIDTH, HEIGHT))
    background = background.convert()
    background.fill(COLOR_BLACK)

    # Blit everything to screen
    screen.blit(background, (0, 0))

    # Update the screen
    pygame.display.flip()

    # This is where i declare all of the objects: player, aliens and blocks. Lasers are added by the shoot functions.

    aliens = []
    for i in range(1, 3):
        for j in range(1, 7):
            alien = Alien(110 * j, 75 * i)
            aliens.append(alien)
    players = []
    player = Player(375, 550)
    players.append(player)
    blocks = []
    block1 = Block(160, 450)
    blocks.append(block1)
    block2 = Block(360, 450)
    blocks.append(block2)
    block3 = Block(560, 450)
    blocks.append(block3)

    # Main loop
    while True:
        clock.tick(FPS)

        # Erase everything drawn at last step by filling the background
        # with color black
        background.fill(COLOR_BLACK)
        player.cooldown -= 1
        alien_cd -= 1

        # This 5 for functions draw all of the objects

        for i in players:
            i.draw(background)
        for i in aliens:
            i.draw(background)
        for i in blocks:
            i.draw(background)
        for i in player.lasers:
            i.draw(background)
        for i in aliens:
            for j in i.lasers:
                j.draw(background)

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

        # This is where I move the aliens and lasers and where I check for collisions.

        for alien in aliens:
            alien.movement(0.05)
            if alien.x <= 0 or alien.x >= 760:
                for j in aliens:
                    j.alien_direction *= -1
            for k in alien.lasers:
                k.move(-0.5)
                for l in blocks:
                    if l.x <= k.x <= l.x + 90 and l.y <= k.y <= l.y + 35:
                        alien.lasers.remove(k)
                        l.count -= 1
                        if l.count == 0:
                            blocks.remove(l)
                if player.x <= k.x <= player.x + 50 and player.y <= k.y <= player.y + 20:
                    for o in players:
                        players.remove(o)
            for block in blocks:
                if alien.x + 40 >= block.x and alien.x <= block.x + 90 and alien.y + 40 >= block.y and alien.y <= block.y + 40:
                    blocks.remove(block)
                    aliens.remove(alien)
            for player in players:
                if alien.x + 40 >= player.x and alien.x <= player.x + 50 and alien.y + 40 >= player.y and alien.y <= player.y + 10:
                    players.remove(player)
                    aliens.remove(alien)

        for i in player.lasers:
            i.move(5)
            for j in blocks:
                if j.x <= i.x <= j.x + 90 and j.y <= i.y <= j.y + 35:
                    player.lasers.remove(i)
                    j.count -= 1
                    if j.count == 0:
                        blocks.remove(j)

            for k in aliens:
                if k.x <= i.x <= k.x + 40 and k.y <= i.y <= k.y + 35:
                    player.lasers.remove(i)
                    aliens.remove(k)

        # These are conditions for the shooting aliens and for the end of the game.

        if len(aliens) == 0 or len(players) == 0:
            end_cd -= 1
            if end_cd == 0:
                sys.exit()
        if alien_cd == 0:
            k = randint(0, len(aliens) - 1)
            shooting_alien = aliens[k]
            shooting_alien.shoot()
            alien_cd = 180
        # Render current game state
        pygame.display.flip()
        screen.blit(background, (0, 0))


if __name__ == '__main__':
    main()
