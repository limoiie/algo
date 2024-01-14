from algo import *


# noinspection PyPep8Naming,PyMethodMayBeStatic
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        return backtrace(nums, 0)


def backtrace(nums, starting):
    if starting == len(nums):
        return [nums[:]]

    ans, visited = [], set()
    for j in range(starting, len(nums)):
        if nums[j] in visited:
            continue
        nums[starting], nums[j] = nums[j], nums[starting]
        ans += backtrace(nums, starting + 1)
        nums[starting], nums[j] = nums[j], nums[starting]
        visited.add(nums[j])
    return ans


# leetcode submit region end(Prohibit modification and deletion)


_cases = [
    TestCase(args=([0, 1, 0, 9],), expected=[]),
    TestCase(args=([1, 1, 2],), expected=[[1, 1, 2], [1, 2, 1], [2, 1, 1]]),
    TestCase(
        args=([3, 3, 0, 3],),
        expected=[[0, 3, 3, 3], [3, 0, 3, 3], [3, 3, 0, 3], [3, 3, 3, 0]],
    ),
]


@pytest.mark.parametrize("case", _cases)
def test_solution(case):
    sol = Solution()
    output = sol.permuteUnique(*case.args)
    assert output == case.expected
