from algo import *


# noinspection PyPep8Naming,PyMethodMayBeStatic
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        return list(backtrace(n, 0, [], k))


def backtrace(n, starting, path, k):
    if k == 0:
        yield path[:]

    for i in range(starting, n):
        path.append(i + 1)
        yield from backtrace(n, i + 1, path, k - 1)
        path.pop()


# leetcode submit region end(Prohibit modification and deletion)


_cases = [
    TestCase(args=(4, 2), expected=...),
]


@pytest.mark.parametrize("case", _cases)
def test_solution(case):
    sol = Solution()
    output = sol.combine(*case.args)
    assert output == case.expected
