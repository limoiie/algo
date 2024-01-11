from algo import *


# noinspection PyPep8Naming,PyMethodMayBeStatic
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        acc = 0
        for c in s:
            acc ^= ord(c)
        for c in t:
            acc ^= ord(c)
        return chr(acc)


# leetcode submit region end(Prohibit modification and deletion)


_cases = [
    TestCase(args=("abcd", "abcde"), expected="e"),
]


@pytest.mark.parametrize("case", _cases)
def test_solution(case):
    sol = Solution()
    output = sol.findTheDifference(*case.args)
    assert output == case.expected
