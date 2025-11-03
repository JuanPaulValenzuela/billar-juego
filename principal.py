#"Hola, simplemente fui a ver y estuve copiando el código, pueden continuar el video en el minuto 15:54"
import pygame
import pymunk #"It is useful to create pymunk space. How objects behave are described by this module"
import pymunk.pygame_util #"Use both features" "Draw pymunk objects on the screen"
pygame.init()

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 678

#game window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Pool")

#pymunk space
space = pymunk.Space()
#space.gravity = (0, 5000) #Unitless, it can be applied horizontally and vertically. In this case this is not necessary
static_body = space.static_body #Espacio para poder "atach" las bolas de billar a un espacio que de fricción
draw_options = pymunk.pygame_util.DrawOptions(screen)

#clock

clos = pygame.time.Clock()
FPS=120

#colours
BG = (50, 50 50)

#load images
table_image = pygame.image.load("assets/img/table.png")#Cargar imagen de la tabla de pool


#function for creating balls
def create_ball(radius, pos):
  body = pymunk.Body()
  body.position = pos
  shape = pymunk.Circle(body, radius)
  shape.mass = 5 #Unitless value
  #use pivot joint to add friction #"Buscar para qué sirve PivotJoint" 
  pivot = pymunk.PivotJoint(static_body, body, (0,0), (0,0)) #Las dos tuplas son las coordenadas donde el joint va a ser hecho
  pivot.max_bias = 0 #disable joint correction
  pivot.max_force = 1000 #Valor de la fricción. "Emulate linear friction" 
 
  
  space.add(body, shape, pivot )
  return shape

new_ball = create_ball(25, (300,300))

cue_ball = create_ball(23, (600, 300))

#game loop
run = True
while run:

  clock.tick(FPS) #Define how frequently the overall game update
  space.step(1 / FPS)

  #fill backfround
  screen.fill(BG)
  
  #Event handeler
  for event in pygame.event.get():
    if event.type == pygame.MOUSEBUTTONDOWN:
      cue_ball.body.apply_impulse_at_local_point(()) #Aplica impulso en modo de coordenadas x-y.
    if event.type == pygame.QUIT:
      run = False

  space.debug_draw(draw_options)
  pygame.display.update() #We need to update the modifications
      
pygame.quit()
