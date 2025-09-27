class Level:
    def __init__(self, width, height):
        self.width = width            # ancho en tiles o unidades
        self.height = height          # alto en tiles o unidades
        self.cubes = []               # lista de Cube
        self.start_cube = None        # cubo de entrada
        self.end_cube = None          # cubo de salida

    def add_cube(self, cube):
        self.cubes.append(cube)

    def get_walkable_cubes(self):
        return [c for c in self.cubes if c.walkable]

    def get_cube_at(self, x, y):
        for c in self.cubes:
            if c.x == x and c.y == y:
                return c
        return None