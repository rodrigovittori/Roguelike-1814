#pgzero

"""
Version actual: [M7.L1: Actividad 4/9]
packs de assets: https://kenney.nl/assets/series:Tiny?sort=update
"""

celda = Actor('border') # Celda de ejemplo (se usa para calcular escalas)

# Paleta de terrenos:

pared =  Actor("border") # 0: Pared de bloques
piso =   Actor("floor")  # 1: Suelo liso
crack =  Actor("crack")  # 2: Suelo resquebrajado/quebradizo
huesos = Actor("bones")  # 3: Suelo con pilita de huesos

size_w = 7 # Ancho del mapa en celdas
size_h = 7 # Altura del mapa en celdas

WIDTH =  celda.width  * size_w
HEIGHT = celda.height * size_h

TITLE = "Mazmorras" # Título de la ventana de juego
FPS = 30 # Número de fotogramas por segundo

mapa = [[0, 0, 0, 0, 0, 0, 0],
        [0, 1, 2, 1, 3, 1, 0],
        [0, 1, 1, 2, 1, 1, 0],
        [0, 3, 2, 1, 1, 3, 0],
        [0, 1, 1, 1, 3, 1, 0],
        [0, 1, 3, 1, 1, 2, 0],
        [0, 0, 0, 0, 0, 0, 0]]
        
mapa2 = [[0, 0, 0, 0, 0, 0, 0],
         [0, 1, 1, 3, 1, 1, 0],
         [0, 1, 3, 1, 3, 1, 0],
         [0, 3, 1, 1, 1, 3, 0],
         [0, 3, 1, 1, 1, 3, 0],
         [0, 1, 3, 3, 3, 1, 0],
         [0, 0, 0, 0, 0, 0, 0]]

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
    dibujar_mapa(mapa)