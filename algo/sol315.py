from algo import *


# noinspection PyPep8Naming,PyMethodMayBeStatic
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        ranks = self.remap(nums)
        bi = BinaryIndexTree(len(nums))
        ans = [0] * len(nums)
        for i, num in enumerate(reversed(nums)):
            bi.update_bit(ranks[num], 1)
            ans[-i - 1] = bi.sum(ranks[num] - 1)
        return ans

    def remap(self, nums: List[int]):
        ranks = collections.Counter()
        for rank, num in enumerate(sorted(set(nums))):
            ranks[num] = rank
        return ranks


class BinaryIndexTree:
    def __init__(self, n):
        self.tree = [0] * (n + 1)

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


# leetcode submit region end(Prohibit modification and deletion)


_cases = [
    TestCase(args=([-1],), expected=[0]),
    TestCase(args=([-1, -1],), expected=[0, 0]),
    TestCase(args=([5, 2, 6, 1],), expected=[2, 1, 1, 0]),
]


@pytest.mark.parametrize("case", _cases)
def test_solution(case):
    sol = Solution()
    output = sol.countSmaller(*case.args)
    assert output == case.expected
