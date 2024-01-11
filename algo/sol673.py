from algo import *


# noinspection PyPep8Naming,PyMethodMayBeStatic
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        sorted_nums = sorted(set(nums))

        max_len, total = 0, 0
        bit = FenwickTree(len(sorted_nums))
        for num in nums:
            idx = bisect.bisect_left(sorted_nums, num)
            lic, cnt = bit.query(idx)
            cnt = cnt if lic else 1
            lic += 1
            if lic == max_len:
                total += cnt
            elif lic > max_len:
                max_len, total = lic, cnt
            bit.update(idx, val=(lic, cnt))
        return total


class FenwickTree:
    def __init__(self, n):
        self.tree = [(0, 0)] * (n + 1)

    def query(self, i):
        acc = (0, 0)
        while i > 0:
            if acc[0] == self.tree[i][0]:
                acc = (self.tree[i][0], self.tree[i][1] + acc[1])
            elif acc[0] < self.tree[i][0]:
                acc = (self.tree[i][0], self.tree[i][1])
            i -= i & -i
        return acc

    def update(self, i, val):
        i += 1
        while i < len(self.tree):
            if self.tree[i][0] == val[0]:
                self.tree[i] = (val[0], val[1] + self.tree[i][1])
            elif self.tree[i][0] < val[0]:
                self.tree[i] = (val[0], val[1])
            i += i & -i


# leetcode submit region end(Prohibit modification and deletion)


_cases = [
    TestCase(args=([1, 3, 5, 4, 7],), expected=2),
    TestCase(args=([2, 2, 2, 2, 2],), expected=5),
]


@pytest.mark.parametrize("case", _cases)
def test_solution(case):
    sol = Solution()
    output = sol.findNumberOfLIS(*case.args)
    assert output == case.expected
