size = 3
sep = '|'
border = '-'*size*3+'\n'

class Tile:
    
    def __init__(self,x,y,player,sep,size):
        self.x = x
        self.y = y
        self.player = player
        self.sep = sep
        self.size = size

    def __eq__(self,other):
        return self.player == other.player
    
    def __hash__(self):
        return self.player
    
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
        board = self.border+board+self.border
        return str(board)

    def h_win(self):
        for row in self.tiles:
            row = set(row)
            if len(row) == 1 and len({' '}+row) > 1:
                return True
            else:
                return False
    
    def v_win(self):
        i = 0
        while i < self.size:
            col = {row[i] for row in self.tiles}
            if len(col) == 1 and len({' '}+col) > 1:
                return True
            else:
                i += 1
        return False
    
    def d_win(self,rev):
        if rev:
            d = {self.tiles[self.size-i][i] for i in range(self.size)}
        else:
            d = {self.tiles[i][i] for i in range(self.size)}
        if len(d) == 1 and len({' '}+d) > 1:
            return True
        else:
            return False

def main(size,sep,border):
    board = Board(size,sep,border)
    print(board)

main(size,sep,border)