import random
from src.map.level import Level
from src.map.cube import Cube

class MapGenerator:
    def __init__(self, level_width, level_height, cube_count, cube_size=32):
        self.level_width = level_width
        self.level_height = level_height
        self.cube_count = cube_count
        self.cube_size = cube_size

    def generate(self):
        level = Level(self.level_width, self.level_height)

        directions = [
            (1, 0, 0),
            (-1, 0, 0),
            (0, 1, 0),
            (0, -1, 0),
            (0, 0, 1),
            (0, 0, -1),
        ]

        # Calcular offset para centrar (0,0,0)
        offset_x = self.level_width // 2
        offset_y = self.level_height // 2

        positions = [(0, 0, 0)]
        occupied = set(positions)

        # Primer cubo
        first_cube = Cube(0, 0, 0, size=self.cube_size, offset_x=offset_x, offset_y=offset_y)
        level.add_cube(first_cube)

        attempts = 0
        while len(level.cubes) < self.cube_count and attempts < self.cube_count * 10:
            gx, gy, gz = random.choice(positions)
            dx, dy, dz = random.choice(directions)
            nx, ny, nz = gx + dx, gy + dy, max(0, gz + dz)

            if (nx, ny, nz) in occupied:
                attempts += 1
                continue

            new_cube = Cube(nx, ny, nz, size=self.cube_size, offset_x=offset_x, offset_y=offset_y)
            level.add_cube(new_cube)
            positions.append((nx, ny, nz))
            occupied.add((nx, ny, nz))
            attempts = 0

        # Marcar inicio y fin
        if level.cubes:
            level.start_cube = level.cubes[0]
            level.end_cube = level.cubes[-1]

        return level
