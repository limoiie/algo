import math

from algo import *


# noinspection PyPep8Naming,PyMethodMayBeStatic
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = math.inf
        max_profile = 0
        for price in prices:
            min_price = min(min_price, price)
            max_profile = max(max_profile, price - min_price)
        return max_profile


# leetcode submit region end(Prohibit modification and deletion)


_cases = [
    TestCase(args=([7, 1, 5, 3, 6, 4],), expected=5),
]


@pytest.mark.parametrize("case", _cases)
def test_solution(case):
    sol = Solution()
    output = sol.maxProfit(*case.args)
    assert output == case.expected
