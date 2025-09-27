class Camera:
    def __init__(self, x=0, y=0, zoom=1.0):
        self.x = x
        self.y = y
        self.zoom = zoom

    def apply(self, points):
        """Aplica offset y zoom a una lista de puntos."""
        transformed = []
        for px, py in points:
            tx = (px - self.x) * self.zoom
            ty = (py - self.y) * self.zoom
            transformed.append((tx, ty))
        return transformed
