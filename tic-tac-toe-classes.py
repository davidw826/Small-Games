size = 3
sep = '|'
border = '-'

class Tile:
    
    def __init__(self,x,y,player):
        self.x = x
        self.y = y
        self.player = player
    
    def __repr__(self):
        return self.player
    
class Board:
    
    def __init__(self,size,sep,border):
        self.sep = sep
        self.border = border
        self.tiles = []
        for x in range(size):
            self.tiles.append([Tile(x,y,' ') for y in range(size)])
    
    def __str__(self):
        board = [self.sep.join(row) for row in self.tiles]
        board = self.border.join(board)
        return board

def main(size):
    board = Board(size,sep,border)
    print(board)

main(size)