'''Module with class Board that represents a board for a game tic tac toe'''


class Board:
    '''Class for representing board in game tic tac toe'''

    def __init__(self):
        '''Create a new board with 9 cells'''
        self._cells = ['-' for i in range(9)]
        self._last_symbol = None
        self._last_position = None

    def num_o(self):
        '''return num of "o" at board'''
        res = 0
        for cell in self._cells:
            if cell == 'o':
                res += 1
        return res

    def num_x(self):
        '''return num of "x" at board'''
        res = 0
        for cell in self._cells:
            if cell == 'x':
                res += 1
        return res

    def it_win(self):
        '''
        :return: str, symbol of that player who won.
        If no one win, return True.
        For example, in that cases:
        x x x         x o o
        o - o         o x -
        o - -         o x x
        function will return "x"
        '''
        win = None
        if self._cells[0] == self._cells[1] == self._cells[2] != '-':
            win = self._cells[0]
        elif self._cells[3] == self._cells[4] == self._cells[5] != '-':
            win = self._cells[3]
        elif self._cells[6] == self._cells[7] == self._cells[8] != '-':
            win = self._cells[6]
        elif self._cells[0] == self._cells[3] == self._cells[6] != '-':
            win = self._cells[0]
        elif self._cells[1] == self._cells[4] == self._cells[7] != '-':
            win = self._cells[1]
        elif self._cells[2] == self._cells[5] == self._cells[8] != '-':
            win = self._cells[2]
        # Diagonals:
        elif self._cells[0] == self._cells[4] == self._cells[8] != '-':
            win = self._cells[0]
        elif self._cells[2] == self._cells[4] == self._cells[6] != '-':
            win = self._cells[2]
        return win

    def cell_is_busy(self, position):
        '''int -> bool
        Accept position, int from 1 to 9 and
        return True if at this position on board is any symbol
        '''
        return self._cells[position - 1] != '-'

    def is_full(self):
        '''Return True if all positions are busy, False otherwise'''
        for cell in self._cells:
            if cell == '-':
                return False
        return True

    def add_move(self, symbol, position):
        '''
        Adds symbol to position
        :param symbol: str, can be "x" or "o"
        :param position: int, position where to put symbol. Can be from 1 to 9.
        positions:
        1 2 3
        4 5 6
        7 8 9
        '''
        if symbol in ('x', 'X'):
            symbol = 'x'
        elif symbol in ('0', 'o', 'O'):
            symbol = 'o'
        else:
            raise Exception('Symbol is not correct')
        if not 1 <= position <= 9:
            raise KeyError('Position is not correct')
        self._cells[position - 1] = symbol
        self._last_position = position
        self._last_symbol = symbol

    def __str__(self):
        '''Return str that represents Board'''
        res = ''
        res += self._cells[0] + ' ' + self._cells[1] + ' ' + self._cells[2] + '\n'
        res += self._cells[3] + ' ' + self._cells[4] + ' ' + self._cells[5] + '\n'
        res += self._cells[6] + ' ' + self._cells[7] + ' ' + self._cells[8]
        return res
