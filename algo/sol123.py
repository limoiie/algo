from algo import *


# noinspection PyPep8Naming,PyMethodMayBeStatic
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy1st = math.inf
        buy2nd = math.inf
        profit1st = 0
        profit2nd = 0
        for p in prices:
            buy1st = min(buy1st, p)
            profit1st = max(profit1st, p - buy1st)
            buy2nd = min(buy2nd, p - profit1st)
            profit2nd = max(profit2nd, p - buy2nd)
        return profit2nd


# leetcode submit region end(Prohibit modification and deletion)


_cases = [
    TestCase(args=([2, 10, 2, 12, 10, 16],), expected=22),
    TestCase(args=([3, 3, 5, 0, 0, 3, 1, 4],), expected=6),
    TestCase(args=([1, 2, 3, 4, 5],), expected=4),
    TestCase(args=([7, 6, 4, 3, 1],), expected=0),
]


@pytest.mark.parametrize("case", _cases)
def test_solution(case):
    sol = Solution()
    output = sol.maxProfit(*case.args)
    assert output == case.expected
