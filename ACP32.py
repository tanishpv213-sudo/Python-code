import pygame

pygame.init()

screen = pygame.display.set_mode((640, 480))

pygame.display.set_caption("My first game screen")

WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)

font = pygame.font.Font(None, 36)
text = font.render("Welcome to my first game!", True, BLACK)

rectangle = pygame.Rect(270, 190, 100, 100)

running = True

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(WHITE)

    pygame.draw.rect(screen, BLUE, rectangle)

    screen.blit(text, (150, 100))

    pygame.display.update()

pygame.quit()
