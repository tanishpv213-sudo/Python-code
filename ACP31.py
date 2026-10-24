import pygame

pygame.init()

screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption("My first game screen")

background = (58, 58, 58)
image = pygame.image.load(r"C:\Users\Admin\Downloads\cHJpdmF0ZS9sci9pbWFnZXMvd2Vic2l0ZS8yMDIzLTEwL3Jhd3BpeGVsX29mZmljZV8zNV9iaXRtYXBzX2VmZmVjdF9waXhlbF84a19pc29sYXRlZF9vbl9ibGFja19iYV8zYTQwNDAwMi02ZmJlLTQyNjctODgzMC1mODkyNzNmMjQ4YzcucG5n.jpg")
image = pygame.transform.scale(image, (300, 300))

image_rect = image.get_rect(center=(250, 250))

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(background)
    screen.blit(image, image_rect)
    pygame.display.update()

pygame.quit()
