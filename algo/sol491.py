from algo import *


# noinspection PyPep8Naming,PyMethodMayBeStatic
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        subs = {(nums[0],)}
        for num in nums[1:]:
            others = [(num,)]
            for sub in subs:
                if num >= sub[-1]:
                    others.append(tuple(list(sub) + [num]))
            subs.update(others)
        return [s for s in subs if len(s) > 1]


# leetcode submit region end(Prohibit modification and deletion)


_cases = [
    TestCase(args=([4, 6, 7, 7],), expected=...),
]


@pytest.mark.parametrize("case", _cases)
def test_solution(case):
    sol = Solution()
    output = sol.findSubsequences(*case.args)
    assert output == case.expected
