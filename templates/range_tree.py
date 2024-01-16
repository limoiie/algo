import dataclasses
from typing import List, Optional


@dataclasses.dataclass
class Point:
    x: int
    value: object


@dataclasses.dataclass
class Interval:
    low: int
    high: int


@dataclasses.dataclass
class Node:
    value: Point
    left: Optional["Node"] = None
    right: Optional["Node"] = None


class RangeTree:
    """
    Range Tree Implementation.

    What is a Range Tree?
    =====================

    A range tree is a tree data structure to hold points in a k-dimensional space.
    It allows one to efficiently find all points within an axis-aligned rectangle
    defined by two points (lower-left and upper-right corners).

    Complexity
    ==========

    Time complexity:

    - Construction: O(n log n)

    - Insertion: O(log n)

    - Search: O(log n + m)

    - Deletion: O(log n)

    Space complexity: O(n)

    Here, "n" represents the total number of points,
    and "m" represents the number of reported results.

    References

    - https://en.wikipedia.org/wiki/Range_tree
    - https://www.geeksforgeeks.org/range-tree/
    """

    def __init__(self, points: List[Point]):
        assert points, "Points must not be empty."
        self.root = self.build(points)

    def _build(self, points: List[Point], lo: int, hi: int):
        if lo >= hi:
            return None

        mid = (lo + hi) >> 1

        left = self._build(points, lo, mid)
        right = self._build(points, mid, hi)

        return Node(points[mid], left, right)

    def _query(self, node: Node, interval: Interval):
        if not (node and interval.low <= node.value.x <= interval.high):
            return

        yield node.value

        yield from self._query(node.left, interval)
        yield from self._query(node.right, interval)

    def _delete(self, node: Node, point: Point):
        if not node:
            return None

        if point.x < node.value.x:
            node.left = self._delete(node.left, point)
        elif point.x > node.value.x:
            node.right = self._delete(node.right, point)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left

            # Get the smallest value in the right subtree
            temp = node.right
            while temp.left:
                temp = temp.left

            node.value = temp.value
            node.right = self._delete(node.right, temp.value)

        return node

    def build(self, points: List[Point]):
        """
        Build a range tree from a list of points.

        Time complexity: O(n log n)
        """
        points.sort(key=lambda p: p.x)
        return self._build(points, lo=0, hi=len(points))

    def insert(self, point: Point):
        """
        Insert a point into the range tree.

        Time complexity: O(log n)
        """
        node = self.root
        while node:
            if point.x < node.value.x:
                if node.left is None:
                    node.left = Node(point)
                    break
                node = node.left
            else:
                if node.right is None:
                    node.right = Node(point)
                    break
                node = node.right

    def delete(self, point: Point):
        """
        Delete a point from the range tree.

        Time complexity: O(log n)
        """
        self._delete(self.root, point)

    def query(self, interval: Interval):
        """
        Query the range tree for all points within the given range.

        Time complexity: O(log n + m)

        :param interval: The range to query.
        """
        return list(self._query(self.root, interval))
