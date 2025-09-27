import pygame
import sys

import pygame
from src.map.map_generator import MapGenerator
from src.entities.player import Player
from src.graphics.camera import Camera

# Inicializar Pygame
pygame.init()
WIDTH, HEIGHT = 640, 480
CUBE_COUNT = 50
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mapa de Cubos Flotantes")

# Generar nivel
generator = MapGenerator(level_width=WIDTH, level_height=HEIGHT, cube_count=CUBE_COUNT, cube_size=32)
level = generator.generate()

# Colocar jugador en cubo inicial
player = Player(level.start_cube)

# Colores
CUBE_COLOR = (200, 200, 200)
START_COLOR = (0, 255, 0)
END_COLOR = (255, 0, 0)
PLAYER_COLOR = (0, 0, 255)

# Loop principal
running = True
clock = pygame.time.Clock()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fondo
    screen.fill((0, 0, 0))
    
    #Camara
    camera = Camera(x=WIDTH//2, y=HEIGHT//2, zoom=1.0)

    # Dibujar cubos en orden correcto (back-to-front)
    for cube in sorted(level.cubes, key=lambda c: (c.grid_x + c.grid_y, c.grid_z)):
        top, right, left = cube.get_faces()

        pygame.draw.polygon(screen, (220,220,220), top)
        pygame.draw.polygon(screen, (180,180,180), right)
        pygame.draw.polygon(screen, (140,140,140), left)

        for face in [top, right, left]:
            pygame.draw.polygon(screen, (0,0,0), face, 1)

    # Dibujar jugador
    px = player.x + player.current_cube.size // 2
    py = player.y + player.current_cube.size // 2
    pygame.draw.circle(screen, PLAYER_COLOR, (int(px), int(py)), player.current_cube.size // 4)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()