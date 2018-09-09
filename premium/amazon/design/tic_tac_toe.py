class TicTacToe:
    def __init__(self, n):
        """
        Initialize your data structure here.
        :type n: int
        """
        self.rows = [0] * n
        self.cols = [0] * n
        self.diagonal = 0
        self.antidiagonal = 0

    def move(self, row, col, player):
        """
        Player {player} makes a move at ({row}, {col}).
        @param row The row of the board.
        @param col The column of the board.
        @param player The player, can be either 1 or 2.
        @return The current winning condition, can be either:
                0: No one wins.
                1: Player 1 wins.
                2: Player 2 wins.
        :type row: int
        :type col: int
        :type player: int
        :rtype: int
        """
        n = len(self.rows)
        to_add = 1 if player == 1 else -1
        self.rows[row] += to_add
        self.cols[col] += to_add
        if row == col:
            self.diagonal += to_add
        if row == n - col - 1:
            self.antidiagonal += to_add
        if abs(self.rows[row]) == n or abs(self.cols[col]) == n or abs(self.diagonal) == n or abs(self.antidiagonal) == n:
               return player

        return 0

class TicTacToeInefficient:

    def __init__(self, n):
        """
        Initialize your data structure here.
        :type n: int
        """
        self.grid = [[None for _ in range(n)] for _ in range(n)]



    def move(self, row, col, player):
        """
        Player {player} makes a move at ({row}, {col}).
        @param row The row of the board.
        @param col The column of the board.
        @param player The player, can be either 1 or 2.
        @return The current winning condition, can be either:
                0: No one wins.
                1: Player 1 wins.
                2: Player 2 wins.
        :type row: int
        :type col: int
        :type player: int
        :rtype: int
        """
        if self.grid[row][col] != None:
            return 0

        self.grid[row][col] = player
        if self.__check_win(player):
            return player
        return 0

    def __check_win(self, player):
        n = len(self.grid)
        for j in range(n):
            i = 0
            while i < n:
                if self.grid[i][j] != player:
                    break
                i += 1
                if i == n:
                    return True

        for i in range(n):
            j = 0
            while j < n:
                if self.grid[i][j] != player:
                    break
                j += 1
                if j == n:
                    return True
        i = 0
        while i < n:
            if self.grid[i][i] != player:
                break
            i += 1
            if i == n:
                return True

        i, j = n - 1, 0
        while i >= 0 and j < n:
            if self.grid[i][j] != player:
                break
            if i == 0 and j == n -1:
                return True
            i -= 1
            j += 1

        return False

# Your TicTacToe object will be instantiated and called as such:
toe = TicTacToe(3)
print('Expect 0: {}'.format(toe.move(0,0,1)))
print('Expect 0: {}'.format(toe.move(0,2,2)))
print('Expect 0: {}'.format(toe.move(2,2,1)))
print('expect 0: {}'.format(toe.move(1,1,2)))
print('Expect 0: {}'.format(toe.move(2,0,1)))
print('Expect 0: {}'.format(toe.move(1,0,2)))
print('Expect 1: {}'.format(toe.move(2,1,1)))
