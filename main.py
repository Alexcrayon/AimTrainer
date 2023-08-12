import pygame
import math
import time
import random
import Target

pygame.init()

WIDTH = 800
HEIGHT = 600
TOPBAR_HEIGHT = 50

WINDOW = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Aim Trainer")

TARGET_INCREMENT = 400
TARGET_EVENT = pygame.USEREVENT
TARGET_PADDING = 30

BG_COLOR = (0, 30, 30)
LIVES = 3

FONT = pygame.font.SysFont("comicsans", 24)


# called every frame
# draw and update everything in the main window
def drawMain(win, targets):
    win.fill(BG_COLOR)

    for target in targets:
        target.drawTarget(win)
    
   

def drawTopbar(win, elapsedTime, targetClicked, misses):
    pygame.draw.rect(win, "grey", (0,0, WIDTH, TOPBAR_HEIGHT ))
    timeLabel = FONT.render(formatTime(elapsedTime), 1, "black")

    speed = round(targetClicked / elapsedTime, 1)
    speedLabel = FONT.render(f"Speed: {speed} hit/s", 1, "black")

    hitLabel = FONT.render(f"Hits: {targetClicked}", 1, "black")

    win.blit(timeLabel, (5, 5))
    win.blit(speedLabel, (200,5))
    win.blit(hitLabel, (470,5))


def formatTime(inputTime):
    miliseconds = math.floor(int(inputTime * 1000 % 1000 / 10))
    seconds = int(round(inputTime % 60, 1))
    minutes = int(inputTime//60)

    return f"{minutes:02d}:{seconds:02d}.{miliseconds}"

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
        elapsedTime = time.time() - startTime
        # print(elapsedTime)

        # event listener
        for event in pygame.event.get():
            # quit game event
            if event.type == pygame.QUIT:
                running = False
                break
            # target generation event
            if event.type == TARGET_EVENT:
                x = random.randint(TARGET_PADDING, WIDTH - TARGET_PADDING)
                y = random.randint(TARGET_PADDING + TOPBAR_HEIGHT, HEIGHT - TARGET_PADDING)
                newTarget = Target.Target(x,y)
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

        if misses >= LIVES:
            pass
        # redraw everything
        drawMain(WINDOW, targets)
        drawTopbar(WINDOW, elapsedTime, targetClicked, misses)
        pygame.display.update()
    pygame.quit()


if __name__ == "__main__":
    main()





