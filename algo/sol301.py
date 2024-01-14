from algo import *


# noinspection PyPep8Naming,PyMethodMayBeStatic
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        state = []
        cnt = 0
        for c in s:
            if c == "(":
                cnt += 1
            elif c == ")":
                cnt -= 1
            state.append(cnt)


# leetcode submit region end(Prohibit modification and deletion)


_cases = [
    TestCase(args=(...,), expected=...),
]


@pytest.mark.parametrize("case", _cases)
def test_solution(case):
    sol = Solution()
    output = sol.removeInvalidParentheses(*case.args)
    assert output == case.expected
