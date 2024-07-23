#pgzero

"""
Version actual: [M7.L1: Actividad 2/9]
packs de assets: https://kenney.nl/assets/series:Tiny?sort=update
"""

# Ventana de juego hecha de celdas
celda = Actor('border')
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