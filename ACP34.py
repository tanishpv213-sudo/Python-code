import pygame
import random

pygame.init()

screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption("Two Sprites - Custom Event")

WHITE = (255, 255, 255)


class MySprite(pygame.sprite.Sprite):
    def __init__(self, x, y, color):
        super().__init__()

        self.image = pygame.Surface((80, 80))
        self.image.fill(color)

        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

    def change_color(self):
        new_color = (
            random.randint(0, 255),
            random.randint(0, 255),
            random.randint(0, 255)
        )
        self.image.fill(new_color)


sprite1 = MySprite(150, 150, (255, 0, 0))
sprite2 = MySprite(350, 150, (0, 0, 255))

all_sprites = pygame.sprite.Group()
all_sprites.add(sprite1, sprite2)

CHANGE_COLOR = pygame.USEREVENT + 1

running = True
clock = pygame.time.Clock()

while running:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                pygame.event.post(
                    pygame.event.Event(CHANGE_COLOR)
                )

        if event.type == CHANGE_COLOR:
            for sprite in all_sprites:
                sprite.change_color()

    screen.fill(WHITE)

    all_sprites.draw(screen)

    pygame.display.update()
    clock.tick(60)

pygame.quit()
