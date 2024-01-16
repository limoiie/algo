from typing import List


class SegmentTree:
    """
    Segment Tree Implementation.

    What is a Segment Tree?
    =======================

    A segment tree is a tree data structure
    for maintaining accumulative properties over intervals, or segments.
    It is, in principle, a static structure;
    that is, it's a structure that cannot be modified once it's built.
    A similar data structure is the range tree.

    Illustration
    ------------

      12
       ++-+
        6 6------+
        +---+-+ +++
            2 4 2 4--------------+
            | | +------------+   |
            | +----------+   |   |
            +-------+-+ +++ +++ +++
                    1 1 2 2 1 1 3 1     # segment tree that maintains sum

                  [ 1,1,2,2,1,1,3,1 ]   # original array

    Complexity
    ==========

    Time complexity:

    - Construction: O(n)

    - Update: O(log n)

    - Query: O(log n)

    Space complexity: O(n)

    Here, "n" represents the total number of elements.

    References

    - https://en.wikipedia.org/wiki/Segment_tree
    - https://www.geeksforgeeks.org/segment-tree-set-1-sum-of-given-range/
    """

    def __init__(self, arr: List[int]):
        self.n = len(arr)
        self.tree = [0] * (self.n << 2)
        self._build(arr, 0, 0, self.n - 1)

    def _build(self, arr, tree_idx, left, right):
        if left == right:
            self.tree[tree_idx] = arr[left]
            return self.tree[tree_idx]

        mid = (left + right) >> 1
        l_acc = self._build(arr, 2 * tree_idx + 1, left, mid)
        r_acc = self._build(arr, 2 * tree_idx + 2, mid + 1, right)
        self.tree[tree_idx] = l_acc + r_acc
        return self.tree[tree_idx]

    def _update(self, tree_idx, left, right, arr_idx, new_val):
        if left == right:
            self.tree[tree_idx] = new_val
            return

        mid = (left + right) >> 1
        if arr_idx <= mid:
            self._update(2 * tree_idx + 1, left, mid, arr_idx, new_val)
        else:
            self._update(2 * tree_idx + 2, mid + 1, right, arr_idx, new_val)
        self.tree[tree_idx] = self.tree[2 * tree_idx + 1] + self.tree[2 * tree_idx + 2]

    def _query(self, tree_idx, left, right, q_left, q_right):
        if q_left > right or q_right < left:
            return 0

        if q_left <= left and q_right >= right:
            return self.tree[tree_idx]

        mid = (left + right) >> 1
        l_acc = self._query(2 * tree_idx + 1, left, mid, q_left, q_right)
        r_acc = self._query(2 * tree_idx + 2, mid + 1, right, q_left, q_right)
        return l_acc + r_acc

    def update(self, arr_idx, new_val):
        """
        Update the value of an element in the array.

        Time complexity: O(log n)

        :param arr_idx:
        :param new_val:
        """
        self._update(0, 0, self.n - 1, arr_idx, new_val)

    def query(self, q_left, q_right):
        """
        Query the sum of elements in a given range.

        Time complexity: O(log n)

        :param q_left:
        :param q_right:
        :return:
        """
        return self._query(0, 0, self.n - 1, q_left, q_right)
