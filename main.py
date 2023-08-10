import pygame
import math
import time
import random
pygame.init()

WIDTH = 800
HEIGHT = 600

WINDOW = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Aim Trainter")

TARGET_INCREMENT = 400
TARGET_EVENT = pygame.USEREVENT
TARGET_PADDING = 30

BG_COLOR = (0, 30, 30)

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

    def drawTarget(self, window):
        pygame.draw.circle(window, self.COLOR, (self.x, self.y), self.size)
        pygame.draw.circle(window, self.COLOR2, (self.x, self.y), self.size * 0.8)
        pygame.draw.circle(window, self.COLOR, (self.x, self.y), self.size * 0.6)
        pygame.draw.circle(window, self.COLOR2, (self.x, self.y), self.size * 0.4)

# called every frame
def draw(win, targets):
    win.fill(BG_COLOR)

    for target in targets:
        target.drawTarget(win)
    
    pygame.display.update()



def main():
    running = True

    # a list for storing targets
    targets = []
    clock = pygame.time.Clock()
    
    # every increment redraw targets on the screen
    pygame.time.set_timer(TARGET_EVENT,TARGET_INCREMENT)


    while running:
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                break
            if event.type == TARGET_EVENT:
                x = random.randint(TARGET_PADDING, WIDTH - TARGET_PADDING)
                y = random.randint(TARGET_PADDING, HEIGHT - TARGET_PADDING)
                newTarget = Target(x,y)
                targets.append(newTarget)

        for target in targets:
            target.update()
            if target.size <= 0:
                targets.remove(target)

        draw(WINDOW, targets)

    pygame.quit()


if __name__ == "__main__":
    main()





