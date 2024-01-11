from algo import *


# noinspection PyPep8Naming,PyMethodMayBeStatic
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        return self.backtrace(nums, 0, [])

    def backtrace(self, nums, i, prefix):
        ans = [list(prefix)]
        for j in range(i, len(nums)):
            if j > i and nums[j] == nums[j - 1]:
                continue
            prefix.append(nums[j])
            ans.extend(self.backtrace(nums, j + 1, prefix))
            prefix.pop()
        return ans


# leetcode submit region end(Prohibit modification and deletion)


_cases = [
    TestCase(args=([1, 2, 2],), expected=...),
]


@pytest.mark.parametrize("case", _cases)
def test_solution(case):
    sol = Solution()
    output = sol.subsetsWithDup(*case.args)
    assert output == case.expected
