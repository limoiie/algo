from algo import *


# noinspection PyPep8Naming,PyMethodMayBeStatic
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
# leetcode submit region end(Prohibit modification and deletion)


_cases = [
    TestCase(args=(...,), expected=...),
]


@pytest.mark.parametrize("case", _cases)
def test_solution(case):
    sol = Solution()
    output = sol.uniquePaths(*case.args)
    assert output == case.expected
