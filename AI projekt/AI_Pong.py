import pygame
from pygame.locals import *
import sys
import math
import random

# Formatera bakgrund m.m.
backgroundColor = (201, 255, 229)
width, height = 500, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Pong demo')
screen.fill(backgroundColor)
clock = pygame.time.Clock()

AIpoints = 0
playerPoints = 0

q = pygame.QUIT
main = True
Color = (0, 0, 0)
radius = 5
game = True

pygame.init()  # Starta pygame

# jokerman/cooperblack(badboll), gigi(fantasy), Chopsic.ttf(space), nes(standard)
font = pygame.font.SysFont("nes", 60)
btnFont = pygame.font.SysFont("nes", 30)
# font = pygame.font.Font('Chopsic.ttf', 60)

winText = font.render("Congratulations!", True, (0, 0, 0))
lossText = font.render("Game over!", True, (0, 0, 0))
drawText = font.render("It's a draw!", True, (0, 0, 0))
btnText = btnFont.render("Try again", True, (255, 255, 255))


class Ball:
    def __init__(self, color, width, height):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.draw.circle(
            screen, (0, 0, 0), (circlePosX, circlePosY), 2*radius)


while main:
    done = False
    paddlePosY, AIpaddlePosY = 250, 250
    direction = 0
    circlePosX = 250
    circlePosY = 250 + random.randint(-100, 100)
    diffX = 0.5
    diffY = 0.5

    while game:
        screen.fill(backgroundColor)
        pygame.draw.line(screen, (0, 0, 0), (0, 505), (500, 505), 5)
        player1 = pygame.draw.rect(screen, Color, (30, paddlePosY, 10, 50))
        # (x kordinat, y kordinat, bredd, längd)
        AI = pygame.draw.rect(screen, Color, (470, AIpaddlePosY, 10, 50))
        pygame.draw.line(screen, (0, 0, 0), (249, 0), (249, 600), 2)
        printPoint = font.render(str(playerPoints), True, (0, 0, 0))
        printPointAI = font.render(str(AIpoints), True, (0, 0, 0))

        screen.blit(printPoint, (200 - printPoint.get_width() //
                                 2, 550 - printPoint.get_height() // 2))
        screen.blit(printPointAI, (300 - printPointAI.get_width() //
                                   2, 550 - printPointAI.get_height() // 2))

        ball = Ball(Color, 5, 5)

        clock.tick(500)  # Timer för att sakta ner spelet

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                main = False

            if event.type == pygame.KEYDOWN:
                if event.key == ord('q'):
                    pygame.quit()
                    sys.exit()
                    main = False

        if AIpaddlePosY < circlePosY:
            if AIpaddlePosY > 440:
                AIpaddlePosY = 440
            elif AIpaddlePosY < 10:
                AIpaddlePosY = 10
            else:
                AIpaddlePosY += 1

        elif AIpaddlePosY > circlePosY:
            if AIpaddlePosY > 440:
                AIpaddlePosY = 440
            elif AIpaddlePosY < 10:
                AIpaddlePosY = 10
            else:
                AIpaddlePosY -= 1

        keys = pygame.key.get_pressed()  # kolla vilka tangenter som trycks ned

        if keys[pygame.K_w] or keys[pygame.K_UP]:  # vad händer om man trycker på pil upp eller w
            #förhindrar att paddeln flyger utanför skärmen
            if paddlePosY > 440:
                paddlePosY = 440
            elif paddlePosY < 10:
                paddlePosY = 10
            else:
                direction = -1

        # vad händer om man trycker på pil ned eller s
        elif keys[pygame.K_s] or keys[pygame.K_DOWN]:
            if paddlePosY > 440:
                paddlePosY = 440
            elif paddlePosY < 10:
                paddlePosY = 10
            else:
                direction = 1

        else:
            direction = 0

        # Om den krockar med vägg i Y-led
        if circlePosY >= 500 or circlePosY <= 0:
            diffY = -diffY

        # Om den krockar med vänster padel
        if circlePosX == 50:
            if circlePosY >= paddlePosY-5 and circlePosY <= paddlePosY+55:
                diffX = -diffX  # olika vinklar här

        # Höger padel
        elif circlePosX == 450:
            if circlePosY >= AIpaddlePosY-5 and circlePosY <= AIpaddlePosY+55:
                diffX = -diffX  # och här

        # Krock med vägg i X-led
        elif circlePosX == 10 or circlePosX == 490:
            if playerPoints < 5 and AIpoints < 5:
                if circlePosX == 10:
                    AIpoints += 1
                elif circlePosX == 490:
                    playerPoints += 1
                game = False
            #skriv ut game over över skärmen och avsluta spelet

        # Addera skillnader till bollens koordinater för förflyttning
        circlePosX += diffX
        circlePosY += diffY
        paddlePosY += direction
        pygame.display.flip()

    # Om någon vunnit skriv ut det till player1
    if AIpoints == 5 or playerPoints == 5:
        if AIpoints == 5:
            screen.blit(lossText, (250 - lossText.get_width() //
                                   2, 250 - lossText.get_height() // 2))

        elif playerPoints == 5:
            screen.blit(winText, (250 - winText.get_width() //
                                  2, 250 - winText.get_height() // 2))

        else:
            screen.blit(drawText, (250 - drawText.get_width() //
                                   2, 250 - drawText.get_height() // 2))

        button = pygame.draw.rect(screen, (0, 0, 0), (180, 280, 140, 30))
        screen.blit(btnText, (250 - btnText.get_width() //
                              2, 295 - btnText.get_height() // 2))
        pygame.display.flip()

        # Try again knapp @click
        while not done:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == ord('q'):
                        pygame.quit()
                        sys.exit()
                        done = True
                        main = False

                elif event.type == pygame.MOUSEBUTTONDOWN:
                    # 1 är vänsterklick, 2 mitten, 3 höger
                    if event.button == 1:
                        # `event.pos` är muspekarens position
                        if button.collidepoint(event.pos):
                            # Gå ut ur "done" loopen och in i "game" loopen
                            done = True
                            game = True

        # Återställning av poäng om nån vunnit
        AIpoints = 0
        playerPoints = 0

    # Om ingen vunnit hela spelet än men vunnit en omgång
    else:
        game = True
