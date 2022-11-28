class SeaMap():

    def __init__(self):
        self.map = []
        for row in range(10):
            r = []
            for col in range(10):
                r.append('-')
            self.map.append(r)
        self.count_hit = []
        # print(*self.map, sep="\n")

    def cell(self):
        return self.map

    def make_star(self, row, col):
        if self.map[row][col - 1] != 'x': self.map[row][col - 1] = '*'
        if self.map[row][col] != 'x': self.map[row][col] = '*'
        if self.map[row][col - 2] != 'x': self.map[row][col - 2] = '*'
        if self.map[row - 1][col] != 'x': self.map[row - 1][col] = '*'
        if self.map[row - 1][col - 2] != 'x': self.map[row - 1][col - 2] = '*'
        if self.map[row - 2][col] != 'x': self.map[row - 2][col] = '*'
        if self.map[row - 2][col - 1] != 'x': self.map[row - 2][col - 1] = '*'
        if self.map[row - 2][col - 2] != 'x': self.map[row - 2][col - 2] = '*'

    def find_miss(self, row, col):
        if self.map[row][col - 1] == '-': return True
        if self.map[row][col] == '-': return True
        if self.map[row][col - 2] == '-': return True
        if self.map[row - 1][col] == '-': return True
        if self.map[row - 1][col - 2] == '-': return True
        if self.map[row - 2][col] == '-': return True
        if self.map[row - 2][col - 1] == '-': return True
        if self.map[row - 2][col - 2] == '-': return True
    # ToDo зацикливается, если больше двух Х доработать обработку счетчика попаданий в функции died
    def died(self, row, col):
        if row - 1 != 0 and row != 10 and col - 1 != 0 and col != 10:
            if self.find_miss(row, col):
                if self.map[row - 2][col - 1] == 'x':
                    self.make_star(row-1, col)
                    self.died(row - 1, col)
                if self.map[row][col - 1] == 'x':
                    self.make_star(row+1, col)
                    self.died(row+1, col)
                if self.map[row - 1][col - 2] == 'x':
                    self.make_star(row, col-1)
                    self.died(row, col - 1)
                if self.map[row - 1][col] == 'x':
                    self.make_star(row, col+1)
                    self.died(row, col+1)
                else:
                    self.make_star(row, col)



            # if self.map[row - 2][col - 1] == '-' or '*':
            #     self.map[row - 2][col] = '*'
            #     self.map[row - 2][col - 2] = '*'
            #     self.map[row - 2][col - 1] = '*'
            #
            # if self.map[row][col - 1] == '-' or '*':
            #     self.map[row][col] = '*'
            #     self.map[row][col - 2] = '*'
            #     self.map[row][col - 1] = '*'
            #
            # if self.map[row - 1][col - 2] == '-' or '*':
            #     self.map[row - 1][col - 2] = '*'
            #     self.map[row][col - 2] = '*'
            #     self.map[row - 2][col - 2] = '*'
            #
            # if self.map[row - 1][col] == '-' or '*':
            #     self.map[row - 1][col] = '*'
            #     self.map[row][col] = '*'
            #     self.map[row - 2][col] = '*'

        else:
            pass

    def shoot(self, row, col, result):
        if result == 'miss':
            self.map[row - 1][col - 1] = '*'
        if result == 'hit':
            self.map[row - 1][col - 1] = 'x'
        if result == 'sink':
            self.map[row - 1][col - 1] = 'x'
            self.died(row, col)


sm = SeaMap()
# sm.shoot(5, 4, 'hit') #4\3
sm.shoot(5, 5, 'hit') #4\4
sm.shoot(5, 6, 'sink') #4\5
# for row in range(10):
#     for col in range(10):
#         print(sm.cell(row, col), end=" ")
#     print()
print(*sm.cell(), sep='\n')