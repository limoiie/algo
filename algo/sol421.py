from algo import *


# noinspection PyPep8Naming,PyMethodMayBeStatic
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        pass


# leetcode submit region end(Prohibit modification and deletion)


_cases = [
    TestCase(args=(...,), expected=...),
]


@pytest.mark.parametrize("case", _cases)
def test_solution(case):
    sol = Solution()
    output = sol.findMaximumXOR(*case.args)
    assert output == case.expected
