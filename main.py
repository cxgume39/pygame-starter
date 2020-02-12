import pygame # import library
pygame.init()

# Create the window
win = pygame.display.set_mode((800, 600))
img = pygame.image.load("assets/background.png").convert()

run = True
while run:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      run = False

# Game code starts here ---------------------
  win.fill((5, 60, 94))

  # Draw a rectangle
  # pygame.draw.rect(win, (219, 34, 42), (50, 50, 100, 200))
  win.blit(img, (150, 00))
  
  #Update the display
  pygame.display.update()

print("Ending game")
pygame.quit()
