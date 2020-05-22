"""
Contains Linked Binary Tree Node implementation.
However, it is not used in the game.
"""


class LinkedBinaryTreeNode:
    """
    Linked Binary Tree Node representation.
    """
    def __init__(self, value):
        """
        Create a new LinkedBinaryTreeNode object.
        """
        self.key = value
        self.left_child = None
        self.right_child = None

    def add_left(self, left):
        """
        Adds left node.
        """
        self.left_child = left

    def add_right(self, right):
        """
        Adds right node.
        """
        self.right_child = right
