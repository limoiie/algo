from algo import *


# noinspection PyPep8Naming,PyMethodMayBeStatic
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def ambiguousCoordinates(self, s: str) -> List[str]:
        ans = []
        for i in range(2, len(s) - 1):
            for prefix in valid(s[1:i]):
                for suffix in valid(s[i:-1]):
                    ans.append(f"({prefix}, {suffix})")
        return ans


def valid(s):
    if s == "0":
        yield s
        return

    if s[0] == "0" and s[-1] != "0":
        yield "0." + s[1:]
        return

    if s[0] != "0":
        yield s

    if s[0] != "0" and s[-1] != "0":
        for i in range(1, len(s)):
            yield s[:i] + "." + s[i:]
        return


# leetcode submit region end(Prohibit modification and deletion)


_cases = [
    TestCase(args=("(123)",), expected=["(1, 2.3)", "(1, 23)", "(1.2, 3)", "(12, 3)"]),
]


@pytest.mark.parametrize("case", _cases)
def test_solution(case):
    sol = Solution()
    output = sol.ambiguousCoordinates(*case.args)
    assert output == case.expected
