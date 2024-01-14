from algo import *


# noinspection PyPep8Naming,PyMethodMayBeStatic
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        return list(backtrace(s, 0, []))


def backtrace(s, starting, path):
    if starting == len(s):
        yield path[:]
        return

    for i in range(starting + 1, len(s) + 1):
        if is_palindrome(s, starting, i):
            path.append(s[starting:i])
            yield from backtrace(s, i, path)
            path.pop()


def is_palindrome(s, lo, hi):
    i, j = lo, hi - 1
    while i < j:
        if s[i] != s[j]:
            return False
        i += 1
        j -= 1
    return True


# leetcode submit region end(Prohibit modification and deletion)


_cases = [
    TestCase(args=("a",), expected=[["a"]]),
    TestCase(args=("aab",), expected=[["a", "a", "b"], ["aa", "b"]]),
]


@pytest.mark.parametrize("case", _cases)
def test_solution(case):
    sol = Solution()
    output = sol.partition(*case.args)
    assert output == case.expected
