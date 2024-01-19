import bisect
from typing import List


class SegmentTree:
    """
    Segment Tree Implementation.

    What is a Segment Tree?
    =======================

    A segment tree is a tree data structure
    used to maintain cumulative properties over intervals or segments.
    It enables efficient querying of various range operations,
    such as finding the minimum, maximum, sum, or any other cumulative operation,
    within a specified range of values in an array.

    It is a static structure,
    meaning it cannot be modified once it is built.

    Illustration
    ------------

      12
       ++-+
        6 6-----+
        +---+-+ +-+
            2 4 2 4-------------+
            | | +-----------+   |
            | +---------+   |   |
            +-------+-+ +-+ +-+ +-+
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


class SortedListBasedSegmentTree:
    """
    Segment Tree Implementation based on Sorted List.

    What is this kind of special segment tree?
    ==========================================

    This segment tree is based on a sorted list.
    It keeps track of the boundaries of intervals in the list,
    allowing for the addition of new intervals through merging,
    partial removal of existing intervals,
    and checking if a given interval is completely covered.

    It only focuses on maintaining interval boundaries and
    does not consider any other properties of the intervals.

    Illustration
    ------------

    For example, given the following intervals:

        [10, 20], [15, 25]

    The segment tree will be represented as:

        [10, 25]

    If we remove the interval [15, 20],
    the segment tree will be transformed into:

        [10, 15, 20, 25]
         +----+  +----+

    Querying for [12, 14] will return True,
    because the interval is completely covered by the segment tree.
    Whereas querying for [12, 16] will return False,
    because the element 16 is not covered by the segment tree.

    Comparison with Interval Tree
    -----------------------------

    TBD.

    Complexity
    ==========

    Time complexity:

    - Add: O(n)

    - Query: O(log n)

    - Remove: O(n)

    Space complexity: O(n)

    Here, "n" represents the total number of elements.
    """

    def __init__(self):
        self.intervals = []

    def add_range(self, left: int, right: int) -> None:
        """
        Add a range to the segment tree.

        Time complexity: O(n)
        """
        bl = bisect.bisect_left(self.intervals, left)
        br = bisect.bisect_right(self.intervals, right)
        lr = self.intervals[:bl] if bl % 2 else (self.intervals[:bl] + [left])
        rr = self.intervals[br:] if br % 2 else ([right] + self.intervals[br:])
        self.intervals = lr + rr

    def query_range(self, left: int, right: int) -> bool:
        """
        Query the segment tree for all points within the given range.

        Time complexity: O(log n)
        """
        bl = bisect.bisect_right(self.intervals, left)
        br = bisect.bisect_left(self.intervals, right)
        return bl == br and bl % 2 == 1

    def remove_range(self, left: int, right: int) -> None:
        """
        Remove a range from the segment tree.

        Time complexity: O(n)
        """
        bl = bisect.bisect_left(self.intervals, left)
        br = bisect.bisect_right(self.intervals, right)
        lr = (self.intervals[:bl] + [left]) if bl % 2 else self.intervals[:bl]
        rr = ([right] + self.intervals[br:]) if br % 2 else self.intervals[br:]
        self.intervals = lr + rr
