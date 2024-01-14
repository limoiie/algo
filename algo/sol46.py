from algo import *


# noinspection PyPep8Naming,PyMethodMayBeStatic
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        return backtrace(nums, 0)


def backtrace(nums, starting):
    if starting == len(nums):
        return [list(nums)]

    ans = []
    for j in range(starting, len(nums)):
        nums[starting], nums[j] = nums[j], nums[starting]
        ans += backtrace(nums, starting + 1)
        nums[starting], nums[j] = nums[j], nums[starting]
    return ans


# leetcode submit region end(Prohibit modification and deletion)


_cases = [
    TestCase(
        args=([1, 2, 3],),
        expected=[
            [1, 2, 3],
            [1, 3, 2],
            [2, 1, 3],
            [2, 3, 1],
            [3, 2, 1],
            [3, 1, 2],
        ],
    ),
]


@pytest.mark.parametrize("case", _cases)
def test_solution(case):
    sol = Solution()
    output = sol.permute(*case.args)
    assert output == case.expected
