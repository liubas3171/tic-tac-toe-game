"""
Module with class BTNode which is used for binary tree
"""


class BTNode:
    """Represents a node for a linked binary tree."""

    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right
