class TicTacToeBoard:
    def __init__(self):
        self.bool_player = True
        self.player = 'X'
        self.field = [['-', '-', '-'],['-', '-', '-'],['-', '-', '-']]

    def new_game(self):
        self.field = [['-', '-', '-'],['-', '-', '-'],['-', '-', '-']]

    def get_field(self):
        return self.field

    def check_field(self):
        if ((self.field[0][0] and self.field[1][0] and self.field[2][0])
                or (self.field[0][1] and self.field[1][1] and self.field[2][1])
                or (self.field[0][2] and self.field[1][2] and self.field[2][2])
                or (self.field[0][0] and self.field[1][1] and self.field[2][2])
                or (self.field[0][2] and self.field[1][1] and self.field[2][0])) == self.player:
            print(f'Winner {self.player}')
            print(*self.get_field(), sep="\n")
            self.new_game()
        elif '-' not in (self.field[0] and self.field[1] and self.field[2]):
            print('Ничья')
            print(*self.get_field(), sep="\n")
            self.new_game()

    def make_move(self, row, col):
        if self.bool_player:
            self.field[row-1][col-1] = self.player
            self.player = 'O'
            self.bool_player = False
        else:
            self.field[row-1][col-1] = self.player
            self.player = 'X'
            self.bool_player = True
        self.check_field()


board = TicTacToeBoard()
print(*board.get_field(), sep="\n")
board.make_move(1, 1)
print(*board.get_field(), sep="\n")
board.make_move(1, 1)
board.make_move(1, 2)
print(*board.get_field(), sep="\n")
board.make_move(2, 1)
board.make_move(2, 2)
board.make_move(3, 1)
board.make_move(2, 2)
print(*board.get_field(), sep="\n")