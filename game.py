'''Module for making gameplay'''

from board import Board
from btree import BinaryTree


def main():
    '''Function for creating gameplay'''
    print('Hello and welcome to crosses-zeros!')
    print('Your symbol is "o".')
    print('During the game you can choose position where to put your symbol.')
    print('Positions are:\n1 2 3\n3 4 5\n6 7 8')
    print('\nAfter you chose, you will see board with my move.')
    print('So, you start!')

    board = Board()
    binary_tree = BinaryTree()
    while True:
        pos = int(input('\nEnter a position:\n>'))
        if board.cell_is_busy(pos):
            print('This cell is busy, try other one')
            continue
        try:
            board.add_move('o', pos)
        except KeyError:
            print('The wrong position')
            continue
        binary_tree.generate_tree(board)
        board = binary_tree.choose_win()
        print(board)
        if board.it_win() == 'o':
            print('Congratulation, you won!')
            break
        if board.it_win() == 'x':
            print("You lost, but don't be upset. Try again)")
            break
        if board.is_full():
            print('Draw!')
            break


if __name__ == '__main__':
    while True:
        main()
        ANS = input('Do you want to restart? (1 - yes, 2 - no):\n>')
        if ANS == '2':
            break
