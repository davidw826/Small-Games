size = 3
sep = '|'
border = '-'+'\n'

class Tile:
    
    def __init__(self,x,y,player,sep,size):
        self.x = x
        self.y = y
        self.player = player
        self.sep = sep
        self.size = size
    
    def __str__(self):
        appear = self.player
        if self.x == 0:
            appear = self.sep+self.player
        else:
            appear = self.player
        if self.x == self.size-1:
            appear += self.sep+'\n'
        return appear
    
class Board:
    
    def __init__(self,size,sep,border):
        self.size = size
        self.sep = sep
        self.border = border
        self.tiles = []
        for y in range(self.size):
            self.tiles.append([Tile(x,y,' ',self.sep,self.size) for x in range(self.size)])
    
    def __str__(self):
        board = []
        for row in self.tiles:
            board.append([str(tile) for tile in row])
        board = [self.sep.join(row) for row in board]
        board = self.border.join(board)
        return str(board)

def main(size):
    board = Board(size,sep,border)
    print(board)

main(size)