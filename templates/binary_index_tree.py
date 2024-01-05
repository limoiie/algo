from typing import List


class BinaryIndexTree:
    def __init__(self, arr: List[int]):
        self.tree = [0] * (len(arr) + 1)
        for i, val in enumerate(arr):
            self.update_bit(i, val)

    def sum(self, i: int):
        s = 0
        i += 1
        while i > 0:
            s += self.tree[i]
            i -= i & -i
        return s

    def update_bit(self, i: int, val: int):
        i += 1
        while i < len(self.tree):
            self.tree[i] += val
            i += i & -i
