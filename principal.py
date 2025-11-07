#pueden continuar el video en el minuto 36"
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
static_body = space.static_body
#space.gravity = (0, 5000) #Unitless, it can be applied horizontally and vertically. In this case this is not necessary
static_body = space.static_body #Espacio para poder "atach" las bolas de billar a un espacio que de fricción
draw_options = pymunk.pygame_util.DrawOptions(screen)

#clock
clock = pygame.time.Clock()
FPS=120

#game variables
dia = 36 #Diametro de la bola

#colours
BG = (50, 50, 50)

#load images
table_image = pygame.image.load("assets/img/table.png").convert_alpha()#Cargar imagen de la tabla de pool
ball_image = []

#function for creating balls
def create_ball(radius, pos):
  body = pymunk.Body() #no ponemos nada en los parentesis para que la bola se mueva
  body.position = pos
  shape = pymunk.Circle(body, radius)
  shape.mass = 5 #Unitless value
  shape.elasticity = 0.8 #Determina la elasticidad de la bola de billar
  #use pivot joint to add friction #"Buscar para qué sirve PivotJoint" 
  pivot = pymunk.PivotJoint(static_body, body, (0,0), (0,0)) #Las dos tuplas son las coordenadas donde el joint va a ser hecho
  pivot.max_bias = 0 #disable joint correction
  pivot.max_force = 1000 #Valor de la fricción. "Emulate linear friction" 
 
  space.add(body, shape, pivot )
  return shape

#Setup game balls
balls =[]
rows = 5
#potting balls #Acomodar las bolas en el triángulo inicial
for col in range(5):
  for row in range(rows):
    pos = (250 + (col * (dia+1)), 267 + (row * (dia+1))+(col * dia / 2))
    new_ball = create_ball(dia / 2, pos)
    balls.append(new_bal)
  rows -=1
#Cue ball
pos = (888, SCREEN_HEIGHT /2)
cue_ball = create_ball(dia / 2, pos)
balls.append(cue_ball)

#create pool table cushions "Para que la bola colisione con la mesa"
cushions = [[
  [(88, 56), (109, 77), (555, 77), (564, 56)]],
  [(621, 56), (630, 77), (1081, 77), (1102, 56)],
  [(89, 621), (110, 600),(556, 600), (564, 621)],
  [(622, 621), (630, 600), (1081, 600), (1102, 621)],
  [(56, 96), (77, 117), (77, 560), (56, 581)],
  [(1143, 96), (1122, 117), (1122, 560), (1143, 581)]
]

#Function for creating cushions
def create_cushion(poly_dims):
  body = pymunk.Body(body_type = pymunk.Body.STATIC) #objeto estático
  body.position= ((0,0))
  shape = pymunk.Poly(body, poly_dims)
  shape.elasticity = 0.8 #Hace a los bordes de la mesa elásticos
  space.add(body, shape)
for c in cushions:
  create_cushion(c)
  


#game loop
run = True
while run:

  clock.tick(FPS) #Define how frequently the overall game update
  space.step(1 / FPS)

  #fill backfround
  screen.fill(BG)
  #Draw pool table
  screen.blit(table_image,(0,0))
  

  
  #Event handeler
  for event in pygame.event.get():
    if event.type == pygame.MOUSEBUTTONDOWN:
      cue_ball.body.apply_impulse_at_local_point(()) #Aplica impulso en modo de coordenadas x-y.
    if event.type == pygame.QUIT:
      run = False

  space.debug_draw(draw_options)
  pygame.display.update() #We need to update the modifications
      
pygame.quit()

