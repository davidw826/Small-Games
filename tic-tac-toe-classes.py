class Tile:
    
    def __init__(self,x,y,player):
        self.x = x
        self.y = y
        self.player = player
    
class Board:
    
    def __init__(self,size,tiles):
        tiles = []
        for x in range(size):
            tiles.append([Tile(x,y,' ') for y in range(size)])
        