from typing import List


class FenwickTree:
    """
    A Fenwick tree or binary indexed tree (BIT) is a data structure
    that can efficiently update values and calculate prefix sums
    in an array of values.
    """

    def __init__(self, n: int):
        self.tree = [0] * (n + 1)

    def query(self, i: int):
        """
        Query the sum of A[0, i), the first i elements.
        """
        acc = 0
        while i > 0:
            acc += self.tree[i]
            i -= i & -i
        return acc

    def update(self, i: int, val: int):
        """
        Update A[i], the i-th element, with the value val.
        """
        i += 1
        while i < len(self.tree):
            self.tree[i] += val
            i += i & -i


def make(nums: List[int]):
    bit = FenwickTree(len(nums))
    for i, num in enumerate(nums):
        bit.update(i, num)
    return bit


class Test:
    def test(self):
        arr = [2, 1, 1, 3, 2, 3, 4, 5, 6, 7, 8, 9]
        bit = FenwickTree(len(arr))
        for i, num in enumerate(arr):
            bit.update(i, num)

        assert bit.query(3) == 4
        assert bit.query(4) == 7
        assert bit.query(6) == 12

        bit.update(3, 6)

        assert bit.query(3) == 4
        assert bit.query(4) == 13
        assert bit.query(6) == 18
