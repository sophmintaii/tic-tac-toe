"""
Contains Linked Binary Tree implementation.
"""


class LinkedBinaryTree:
    """
    Linked Binary Tree representation.
    """
    def __init__(self, root):
        """
        Creates a new LinkedBinaryTree onject.
        """
        self.key = root
        self.left_child = None
        self.right_child = None

    def insert_left(self, new_node):
        """
        Inserts left child tree to the self.
        """
        if self.left_child is None:
            self.left_child = LinkedBinaryTree(new_node)
        else:
            temp = LinkedBinaryTree(new_node)
            temp.left_child = self.left_child
            self.left_child = temp

    def insert_right(self, new_node):
        """
        Inserts right child tree to the self.
        """
        if self.right_child is None:
            self.right_child = LinkedBinaryTree(new_node)
        else:
            temp = LinkedBinaryTree(new_node)
            temp.right_child = self.right_child
            self.right_child = temp

    def leaves_list(self):
        """
        Returns leaves of the tree.
        """

        def check_if_leaf(tree, leaves):
            """Recursive helping function."""
            if tree.left_child is None and tree.right_child is None:
                leaves.append(tree.key)
            if tree.left_child is not None:
                check_if_leaf(tree.left_child, leaves)
            if tree.right_child is not None:
                check_if_leaf(tree.right_child, leaves)

        leaves = []
        check_if_leaf(self, leaves)
        return leaves

    def get_right_child(self):
        """
        Returns right child of the tree.
        """
        return self.right_child

    def get_left_child(self):
        """
        Returns left child of the tree.
        """
        return self.left_child
