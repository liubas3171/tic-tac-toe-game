'''Module with class BinaryTree which was created to play tic tac toe'''

import random
import copy
from btnode import BTNode


class BinaryTree:
    '''Class for representing a binary tree'''

    def __init__(self):
        '''Create a new BinaryTree'''
        self._root = None
        self._size = 0

    def generate_tree(self, start_board):
        '''Board -> None
        Generate a binary tree with possible moves
        '''
        self._root = BTNode(start_board)

        def recursive(node):
            '''func for recursive creating of tree'''
            if node.data.is_full():
                return None

            pos_1 = random.randint(1, 9)
            while node.data.cell_is_busy(pos_1):
                pos_1 = random.randint(1, 9)

            if node.data.num_o() > node.data.num_x():
                data = copy.deepcopy(node.data)

                node.left = BTNode(data)
                node.left.data.add_move('x', pos_1)
                recursive(node.left)

                pos = random.randint(1, 9)
                while node.data.cell_is_busy(pos):
                    pos = random.randint(1, 9)

                data = copy.deepcopy(node.data)

                node.right = BTNode(data)
                node.right.data.add_move('x', pos)
                recursive(node.right)
            else:
                data = copy.deepcopy(node.data)

                node.left = BTNode(data)
                node.left.data.add_move('o', pos_1)
                recursive(node.left)

                pos = random.randint(1, 9)
                while node.data.cell_is_busy(pos):
                    pos = random.randint(1, 9)

                data = copy.deepcopy(node.data)

                node.right = BTNode(data)
                node.right.data.add_move('o', pos)
                recursive(node.right)

        recursive(self._root)

    def choose_win(self):
        '''None -> Board
        Count winning combination on right and left children of root
        and return Board which you should prefer
        '''
        if not self._root.right or not self._root.left:
            return self._root.data

        def recursive(node):
            '''func for recursive counting of win combination in tree'''
            if not node:
                return 0
            if node.data.it_win() == 'x':
                return 1
            if node.data.it_win() == 'o':
                return -1
            if node.data.is_full():
                return 0
            return recursive(node.right) + recursive(node.left)

        left = recursive(self._root.left)
        right = recursive(self._root.right)
        if right > left:
            return self._root.right.data
        return self._root.left.data
