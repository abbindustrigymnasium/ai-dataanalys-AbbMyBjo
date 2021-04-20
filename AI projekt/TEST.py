import pygame


pygame.init()
backgroundColor = (201, 255, 229)
screen = pygame.display.set_mode((500, 500))
screen.fill(backgroundColor)
button = pygame.draw.rect(screen, (0, 0, 0), (225, 270, 250, 250))
done = False
while True:
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
                # This block is executed once for each MOUSEBUTTONDOWN event.
            elif event.type == pygame.MOUSEBUTTONDOWN:
                    # 1 is the left mouse button, 2 is middle, 3 is right.
                if event.button == 1:
                        # `event.pos` is the mouse position.
                    if button.collidepoint(event.pos):
                            # Increment the number.
                        pygame.QUIT()
        pygame.display.flip()
