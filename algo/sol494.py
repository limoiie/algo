from algo import *


# noinspection PyPep8Naming,PyMethodMayBeStatic
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = {0: 1}
        return backtrace(nums, target, dp, 0, 0)


def backtrace(nums, target, dp, i, acc):
    if i >= len(nums):
        return acc == target
    if (i, acc) not in dp:
        dp[(i, acc)] = backtrace(nums, target, dp, i + 1, acc + nums[i]) + backtrace(
            nums, target, dp, i + 1, acc - nums[i]
        )
    return dp[(i, acc)]


# leetcode submit region end(Prohibit modification and deletion)


_cases = [
    TestCase(args=([1], 2), expected=0),
    TestCase(args=([1, 1, 1, 1, 1], 3), expected=5),
]


@pytest.mark.parametrize("case", _cases)
def test_solution(case):
    sol = Solution()
    output = sol.findTargetSumWays(*case.args)
    assert output == case.expected
