class Cube:
    def __init__(self, grid_x, grid_y, grid_z=0, size=32, offset_x=0, offset_y=0):
        self.grid_x = grid_x
        self.grid_y = grid_y
        self.grid_z = grid_z
        self.size = size

        # Proyección isométrica con desplazamiento
        self.x = (grid_x - grid_y) * size + offset_x
        self.y = (grid_x + grid_y) * (size // 2) - grid_z * size + offset_y

    def get_faces(self):
        s = self.size
        x, y = self.x, self.y

        top = [
            (x, y),
            (x + s, y - s // 2),
            (x + 2 * s, y),
            (x + s, y + s // 2)
        ]
        right = [
            (x + s, y + s // 2),
            (x + 2 * s, y),
            (x + 2 * s, y + s),
            (x + s, y + s + s // 2)
        ]
        left = [
            (x, y),
            (x + s, y + s // 2),
            (x + s, y + s + s // 2),
            (x, y + s)
        ]
        return top, right, left
