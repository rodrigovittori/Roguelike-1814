#pgzero

"""
Version actual: [M7.L1: Actividades Extra]
packs de assets: https://kenney.nl/assets/series:Tiny?sort=update
"""

celda = Actor('border') # Celda de ejemplo (se usa para calcular escalas)

# Paleta de terrenos:

pared =  Actor("border") # 0: Pared de bloques
piso =   Actor("floor")  # 1: Suelo liso
crack =  Actor("crack")  # 2: Suelo resquebrajado/quebradizo
huesos = Actor("bones")  # 3: Suelo con pilita de huesos

size_w = 9 # Ancho del mapa en celdas
size_h = 10 # Altura del mapa en celdas

WIDTH =  celda.width  * size_w
HEIGHT = celda.height * size_h

TITLE = "Mazmorras" # Título de la ventana de juego
FPS = 30 # Número de fotogramas por segundo

# PERSONAJE:

personaje = Actor("stand")
personaje.salud = 100
personaje.ataque = 5

# To-do: Lista de mapas?
# Ampliamos a 9x9 + una fila para mostrar el texto (9x10)

mapa =   [[0, 0, 0, 0, 0, 0, 0, 0, 0], 
          [0, 1, 1, 1, 1, 1, 1, 1, 0], 
          [0, 1, 1, 2, 1, 3, 1, 1, 0], 
          [0, 1, 1, 1, 2, 1, 1, 1, 0], 
          [0, 1, 3, 2, 1, 1, 3, 1, 0], 
          [0, 1, 1, 1, 1, 3, 1, 1, 0], 
          [0, 1, 1, 3, 1, 1, 2, 1, 0], 
          [0, 1, 1, 1, 1, 1, 1, 1, 0], 
          [0, 0, 0, 0, 0, 0, 0, 0, 0],
          [-1, -1, -1, -1, -1, -1, -1, -1, -1]] # Fila extra para mostrar el texto
      
mapa2 = [[0, 0, 0, 0, 0, 0, 0, 0, 0], 
          [0, 1, 1, 1, 1, 1, 1, 1, 0], 
          [0, 1, 1, 3, 1, 3, 1, 1, 0], 
          [0, 1, 1, 3, 1, 3, 1, 1, 0], 
          [0, 1, 1, 1, 1, 1, 1, 1, 0], 
          [0, 3, 1, 1, 1, 1, 1, 3, 0], 
          [0, 1, 3, 1, 1, 1, 3, 1, 0], 
          [0, 1, 1, 3, 3, 3, 1, 1, 0], 
          [0, 0, 0, 0, 0, 0, 0, 0, 0],
          [-1, -1, -1, -1, -1, -1, -1, -1, -1]] # Fila extra para mostrar el texto


def dibujar_mapa(mapa):
    
    for fila in range(len(mapa)):
        for columna in range(len(mapa[0])):
            
            """
            0: pared
            1: piso (sin nada)
            2: piso (roto/resquebrajado)
            3: piso (c/ huesitos)
            """
            
            if (mapa[fila][columna] == 0): # pared
                pared.left = pared.width * fila
                pared.top =  pared.height * columna
                pared.draw()
                
            elif (mapa[fila][columna] == 1): # piso (sin nada)
                piso.left = pared.width * fila
                piso.top =  pared.height * columna
                piso.draw()
                
            elif (mapa[fila][columna] == 2): # piso (roto/resquebrajado)
                # crack
                crack.left = crack.width * fila
                crack.top  = crack.height * columna
                crack.draw()
                
            elif (mapa[fila][columna] == 3): # piso (c/ huesitos)
                # huesos
                huesos.left = huesos.width * fila
                huesos.top  = huesos.height * columna
                huesos.draw()
                
def draw():
  screen.fill("#2f3542") # (47, 53, 66)
  dibujar_mapa(mapa)
  personaje.draw()

  screen.draw.text(("Salud: " + str(personaje.salud)), midleft=(30, (HEIGHT - int(celda.height/2))), color = 'white', fontsize = 24)
  screen.draw.text(("Ataque: " + str(personaje.ataque)), midright=((WIDTH - 30), (HEIGHT - int(celda.height/2))), color = 'white', fontsize = 24)

def on_key_down(key):
  
  if ((keyboard.right or keyboard.d) and (personaje.x < WIDTH - celda.width * 2)):
    # ¿Xq 2?: Una (la que me voy a desplazar) y otra (por la pared, que NO puedo atravesar)
    personaje.x += celda.width
    personaje.image = "stand" # xq stand mira a la dcha
        
  elif ((keyboard.left or keyboard.a) and (personaje.x > celda.width * 2)):
    personaje.x -= celda.width
    personaje.image = "left"
        
  elif ((keyboard.down or keyboard.s) and (personaje.y < HEIGHT - celda.height * 3)): # ¿xq 3?: porque le agrego OTRA fila (en la que mostramos el texto)
    personaje.y += celda.height
    
  elif ((keyboard.up or keyboard.w) and (personaje.y > celda.height * 2)):
        personaje.y -= celda.height