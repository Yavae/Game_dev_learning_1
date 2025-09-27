class Player:
    def __init__(self, current_cube):
        self.current_cube = current_cube  # Cubo donde está el jugador
        self.x = current_cube.x
        self.y = current_cube.y
        self.hp = 10
        self.inventory = []

    def move_to(self, cube):
        """
        Mueve al jugador a otro cubo si es walkable
        """
        if cube.walkable:
            self.current_cube = cube
            self.x = cube.x
            self.y = cube.y
            return True
        return False