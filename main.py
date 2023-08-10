import pygame
import math
import time
import random
pygame.init()

WIDTH = 800
HEIGHT = 600

WINDOW = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Aim Trainter")

class Target:
    MAX_SIZE = 30
    GROWTH_RATE = 0.2
    COLOR = "blue"
    COLOR2 = "white"

    def __init__(self, posX, posY):
        self.x = posX
        self.y = posY
        self.size = 0
        self.growing = True

    def update(self):
        if self.size + self.GROWTH_RATE >= self.MAX_SIZE:
            self.growing = False

        if self.growing:
            self.size += self.GROWTH_RATE
        else:
            self.size -= self.GROWTH_RATE

    def draw(self, window):
        pygame.draw.circle(window, self.COLOR, (self.x, self.y), self.size)
        pygame.draw.circle(window, self.COLOR2, (self.x, self.y), self.size * 0.8)
        pygame.draw.circle(window, self.COLOR, (self.x, self.y), self.size * 0.6)
        pygame.draw.circle(window, self.COLOR2, (self.x, self.y), self.size * 0.4)


def main():
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                break

    pygame.quit()


if __name__ == "__main__":
    main()


