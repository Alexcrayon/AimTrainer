import pygame
import math
import time
import random
pygame.init()

WIDTH = 800
HEIGHT = 600

WINDOW = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Aim Trainer")

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

    # update the size the target by growth rate
    # it is either growing or shrinking
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
    
     
    # Check collision with mouse clicks
    def collide(self, posX, posY):
        distance = math.sqrt((self.x - posX)**2 + (self.y - posY)**2)
        return distance <= self.size



# called every frame
# draw and update everything in the main window
def drawMain(win, targets):
    win.fill(BG_COLOR)

    for target in targets:
        target.drawTarget(win)
    
    pygame.display.update()



def main():
    running = True

    # a list for storing targets
    targets = []
    clock = pygame.time.Clock()
    
    targetClicked = 0
    clicks = 0
    misses = 0
    startTime = time.time()

    # every increment redraw targets on the screen
    pygame.time.set_timer(TARGET_EVENT,TARGET_INCREMENT)

    # main game loop
    while running:
        clock.tick(60)
        mouseClicked = False
        mousePos = pygame.mouse.get_pos()
        # event listener
        for event in pygame.event.get():
            # quit game event
            if event.type == pygame.QUIT:
                running = False
                break
            # target generation event
            if event.type == TARGET_EVENT:
                x = random.randint(TARGET_PADDING, WIDTH - TARGET_PADDING)
                y = random.randint(TARGET_PADDING, HEIGHT - TARGET_PADDING)
                newTarget = Target(x,y)
                targets.append(newTarget)
            # click event
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouseClicked = True
                clicks += 1

        # update the target list by 
        # whether a target has been clicked or shrinks to zero size
        for target in targets:
            target.update()
            if target.size <= 0:
                targets.remove(target)
                misses += 1

            if mouseClicked and target.collide(*mousePos):
                targets.remove(target)
                targetClicked += 1

        # redraw everything
        drawMain(WINDOW, targets)

    pygame.quit()


if __name__ == "__main__":
    main()





