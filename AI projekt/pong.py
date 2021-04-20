import pygame
from pygame.locals import *
import sys
import math
import random 

backgroundColor = (201,255,229)
width, height = 500, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Pong demo')
screen.fill(backgroundColor)
clock = pygame.time.Clock()

q = pygame.QUIT
main = True
Color = (0, 0, 0)
direction = 0
paddlePosY, y2Pos = 250, 250
circlePosX = 250
circlePosY = 250
diffX = 0.5
diffY = 0.5
radie = 5
game = True

pygame.init()

# jokerman/cooperblack(badboll), gigi(fantasy), Chopsic.ttf(space), nes(standard)
font = pygame.font.SysFont("nes", 60)
# font = pygame.font.Font('Chopsic.ttf', 60)

text = font.render("Game over!", True, (0, 0, 0))

# class AI:
#     def __init__(self):
#         pygame.sprite.Sprite.__init__(self)
#         self.move = 0

#     def control(self, movement):
#         self.move += movement
    
#     def update(self):
#         self.rect.move = self.move


class Ball:
    def __init__(self, color, width, height):

        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.draw.circle(screen, (0, 0, 0), (circlePosX, circlePosY), 2*radie)


class invisibleBall:
    def __init__(self, vector):
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = load_png('ball.png')
        # screen = pygame.display.get_surface()
        self.area = screen.get_rect()
        self.vector = vector

    def update(self):
        newpos = self.calcnewpos(self.rect, self.vector)
        self.rect = newpos

    def calcnewpos(self, rect, vector):
        (angle, z) = vector
        (dx, dy) = (z*math.cos(angle), z*math.sin(angle))
        return rect.move(dx, dy)

while main:
    done = False
    while game:
        screen.fill(backgroundColor)
        pygame.draw.line(screen, (0, 0, 0), (0, 505), (500, 505), 5)
        player1 = pygame.draw.rect(screen, Color, (30, paddlePosY, 10, 50))
        player2 = pygame.draw.rect(screen, Color, (470, y2Pos, 10, 50)) # (x kordinat, y kordinat, bredd, längd)
        ball = Ball(Color, 5, 5)

        clock.tick(500)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit(); sys.exit()
                main = False

            if event.type == pygame.KEYDOWN:
                if event.key == ord('q'):
                    pygame.quit()
                    sys.exit()
                    main = False

        keys = pygame.key.get_pressed() #kolla vilka tangenter som trycks ned

        if keys[pygame.K_w] or keys[pygame.K_UP]: #vad händer om man trycker på pil upp eller w
            #förhindrar att paddeln flyger utanför skärmen
            if paddlePosY > 440: 
                paddlePosY = 440
            elif paddlePosY < 10:
                paddlePosY = 10
            else:
                direction = -1

        elif keys[pygame.K_s] or keys[pygame.K_DOWN]: #vad händer om man trycker på pil ned eller s
            if paddlePosY > 440:
                paddlePosY = 440
            elif paddlePosY < 10:
                paddlePosY = 10
            else:
                direction = 1
        
        else:
            direction = 0

        if circlePosX >= 500-2*radie:
            if circlePosY >= 500-2*radie:
                diffY = -diffY
            elif circlePosY <= 0+2*radie:
                diffY = -diffY
            diffX = -diffX

        elif circlePosX <= 0+2*radie:
            if circlePosY >= 500-2*radie:
                diffY = -diffY
            elif circlePosY <= 0+2*radie:
                diffY = -diffY
            diffX = -diffX
        
        elif circlePosY >= 500-2*radie:
            if circlePosX >= 500-2*radie:
                diffX = -diffX
            elif circlePosX <= 0+2*radie:
                diffX = -diffX
            diffY = -diffY
        
        elif circlePosY <= 0+2*radie: 
            if circlePosX >= 500-2*radie:
                diffX = -diffX
            elif circlePosX <= 0+2*radie:
                diffX = -diffX
            diffY = -diffY

        if circlePosX == 50:
            if circlePosY >= paddlePosY and circlePosY <= paddlePosY+50:
                diffX = -diffX

        elif circlePosX == 10:
            game = False
            #skriv ut game over över skärmen och avsluta spelet

        circlePosX += diffX
        circlePosY += diffY
        paddlePosY += direction
        pygame.display.flip()
    
    screen.blit(text,(250 - text.get_width() // 2, 250 - text.get_height() // 2))
    button = pygame.draw.rect(screen, (0, 0, 0), (225, 270, 50, 30))
    pygame.display.flip()
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == ord('q'):
                    pygame.quit()
                    sys.exit()
                    done = True
                    main = False

            elif event.type == pygame.MOUSEBUTTONDOWN:
                # 1 is the left mouse button, 2 is middle, 3 is right.
                if event.button == 1:
                    # `event.pos` is the mouse position.
                    if button.collidepoint(event.pos):
                        done = True

# en osynlig boll som går snabbare än den synliga så AI:n vet var den riktiga ska och kan åka dit snabbare
