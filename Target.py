import pygame
import math

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
