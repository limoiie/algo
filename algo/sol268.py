from algo import *


# noinspection PyPep8Naming,PyMethodMayBeStatic
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        acc = 0
        for num in range(len(nums) + 1):
            acc ^= num
        for num in nums:
            acc ^= num
        return acc


# leetcode submit region end(Prohibit modification and deletion)


_cases = [
    TestCase(args=([3, 0, 1],), expected=2),
    TestCase(args=([0, 1],), expected=2),
]


@pytest.mark.parametrize("case", _cases)
def test_solution(case):
    sol = Solution()
    output = sol.missingNumber(*case.args)
    assert output == case.expected
