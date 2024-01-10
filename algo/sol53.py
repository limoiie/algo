from . import *


# noinspection PyPep8Naming,PyMethodMayBeStatic
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = nums[0]
        acc = 0
        for num in nums:
            acc += num
            max_sum = max(max_sum, acc)
            acc = acc if acc > 0 else 0
        return max_sum


# leetcode submit region end(Prohibit modification and deletion)


_cases = [
    TestCase(args=([-2, 1, -3, 4, -1, 2, 1, -5, 4],), expected=6),
    TestCase(args=([1],), expected=1),
    TestCase(args=([5, 4, -1, 7, 8],), expected=23),
    TestCase(args=([-2, -1],), expected=-1),
    TestCase(args=([-1],), expected=-1),
]


@pytest.mark.parametrize("case", _cases)
def test_solution(case):
    sol = Solution()
    output = sol.maxSubArray(*case.args)
    assert output == case.expected
