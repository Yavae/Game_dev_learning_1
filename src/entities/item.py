class Item:
    def __init__(self, x, y, name='Item'):
        self.x = x
        self.y = y
        self.name = name
        self.picked = False
        
    def pick_up(self, player):
        if player.x == self.x and player.y == self.y:
            self.picked = True
            player.inventory.append(self)
            return True
        return False
        