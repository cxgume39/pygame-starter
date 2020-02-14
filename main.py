import pygame # import library
pygame.init()

# Create the window
win = pygame.display.set_mode((800, 600))
img = pygame.image.load("assets/background.png").convert()
img = pygame.transform.scale(img,(800,500))
ship = pygame.image.load("assets/PirateShip.png").convert_alpha()
x = 200
hp=200

# Create the font
font = pygame.font.SysFont("arial", 60)
# Create the text object
text = font.render("The Voyage", True, (5, 60, 94))

run = True
while run:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      run = False
  if x >= x:
    hp -= 1
    print(hp)
# Game code starts here ---------------------
  win.fill((5, 60, 94))

  win.blit(img, (0, 60))
  win.blit(text, (230, 200))
  win.blit(ship, (x,250))
  keys=pygame.key.get_pressed()
  if keys[pygame.K_LEFT]:
    x -= 0.5
  if keys[pygame.K_RIGHT]:
    x += 0.5

  #Update the display
  pygame.display.update()

print("Ending game")
pygame.quit()
