from algo import *


# noinspection PyPep8Naming,PyMethodMayBeStatic
# leetcode submit region begin(Prohibit modification and deletion)
class NumArray:
    def __init__(self, nums: List[int]):
        self.bit = FenwickTree(len(nums))
        for i, num in enumerate(nums):
            self.bit.update(i, num)
        self.nums = nums

    def update(self, index: int, val: int) -> None:
        self.bit.update(index, val - self.nums[index])
        self.nums[index] = val

    def sumRange(self, left: int, right: int) -> int:
        return self.bit.query(right + 1) - self.bit.query(left)


class FenwickTree:
    def __init__(self, n: int):
        self.tree = [0] * (n + 1)

    def query(self, i: int):
        acc = 0
        while i > 0:
            acc += self.tree[i]
            i -= i & -i
        return acc

    def update(self, i: int, val: int):
        i += 1
        while i < len(self.tree):
            self.tree[i] += val
            i += i & -i


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)
# leetcode submit region end(Prohibit modification and deletion)


class Test:
    def test_solution1(self):
        ins = NumArray([1, 3, 5])
        assert ins.sumRange(0, 2) == 9
        ins.update(1, 2)
        assert ins.sumRange(0, 2) == 8

    def test_solution2(self):
        ins = NumArray([7, 2, 7, 2, 0])
        ins.update(4, 6)
        ins.update(0, 2)
        ins.update(0, 9)
        assert ins.sumRange(4, 4) == 6
        ins.update(3, 8)
        assert ins.sumRange(0, 4) == 32
        ins.update(4, 1)
        assert ins.sumRange(0, 3) == 26
        assert ins.sumRange(0, 4) == 27
        ins.update(0, 4)
