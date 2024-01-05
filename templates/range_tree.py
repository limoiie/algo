from typing import List


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class RangeTree:
    def __init__(self, points: List[List[int]]):
        self.root = self.build_tree(points)

    def build_tree(self, points: List[List[int]]):
        if not points:
            return None

        points = sorted(points, key=lambda p: p[0])  # Sort points by x-coordinate

        mid = len(points) // 2
        node = Node(points[mid])  # Choose the median point as the root of the subtree

        node.left = self.build_tree(points[:mid])
        node.right = self.build_tree(points[mid + 1 :])

        return node

    def query_range(self, x1, x2, node=None):
        if node is None:
            node = self.root

        if node is None or x2 < node.value[0] or x1 > node.value[0]:
            return []

        if x1 <= node.value[0] <= x2:
            result = [node.value]
        else:
            result = []

        result.extend(self.query_range(x1, x2, node.left))
        result.extend(self.query_range(x1, x2, node.right))

        return result
