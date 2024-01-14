from algo import *


# noinspection PyPep8Naming,PyMethodMayBeStatic
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        def backtrace(prefix, i):
            if i >= len(s):
                ans.append(prefix)
                return

            backtrace(prefix + s[i], i + 1)
            if s[i].isalpha():
                backtrace(prefix + s[i].swapcase(), i + 1)

        ans = []
        backtrace("", 0)
        return ans


# leetcode submit region end(Prohibit modification and deletion)


_cases = [
    TestCase(args=("a1b2",), expected=["a1b2", "a1B2", "A1b2", "A1B2"]),
]


@pytest.mark.parametrize("case", _cases)
def test_solution(case):
    sol = Solution()
    output = sol.letterCasePermutation(*case.args)
    assert output == case.expected
