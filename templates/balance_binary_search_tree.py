from math import log2
from algo import *


# noinspection PyMethodMayBeStatic
class DayStoutWarrenAlgo:
    """
    The Day–Stout–Warren (DSW) algorithm
    is a method for efficiently balancing binary search trees –
    that is, decreasing their height to O(log n) nodes,
    where n is the total number of nodes.
    Unlike a self-balancing binary search tree,
    it does not do this incrementally during each operation,
    but periodically,
    so that its cost can be amortized over many operations.
    """

    def run(self, tree):
        root = TreeNode(right=tree)
        size = self.tree_to_vine(root)
        self.vine_to_tree(root, size)
        return root.right

    def tree_to_vine(self, root):
        tail = root
        rest = tail.right
        size = 0
        while rest is not None:
            if rest.left is None:
                # enroll forward
                tail = rest
                rest = rest.right
                size += 1
            else:
                # rotate rest.left to tail.right
                temp = rest.left
                rest.left = temp.right
                temp.right = rest
                rest = temp
                tail.right = temp
        return size

    def vine_to_tree(self, root, size):
        leaves = size + 1 - (1 << int(log2(size + 1)))
        self.compress(root, leaves)
        size -= leaves
        while size > 1:
            size //= 2
            self.compress(root, size)
        return root.right

    def compress(self, root, cnt):
        curr = root
        for _ in range(cnt):
            child = curr.right
            curr.right = child.right
            curr = curr.right
            child.right = curr.left
            curr.left = child
