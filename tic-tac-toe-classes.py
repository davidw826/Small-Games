size = 3

class Tile:
    
    def __init__(self,x,y,player):
        self.x = x
        self.y = y
        self.player = player
    
    def __str__(self):
        return self.player
    
class Board:
    
    def __init__(self,size):
        self.tiles = []
        for x in range(size):
            self.tiles.append([Tile(x,y,' ') for y in range(size)])
    
    def __str__(self):
        return str(self.tiles)

def main(size):
    board = Board(size)
    print(board)

main(size)