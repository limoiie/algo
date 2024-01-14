from algo import *


# noinspection PyPep8Naming,PyMethodMayBeStatic
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        return list(backtrace(1, [], k, n))


def backtrace(starting, path, k, n):
    if k == 0:
        if n == 0:
            yield path[:]
        return

    for i in range(starting, 10):
        path.append(i)
        yield from backtrace(i + 1, path, k - 1, n - i)
        path.pop()


# leetcode submit region end(Prohibit modification and deletion)


_cases = [
    TestCase(args=(3, 7), expected=[[1, 2, 4]]),
    TestCase(args=(3, 9), expected=[[1, 2, 6], [1, 3, 5], [2, 3, 4]]),
    TestCase(args=(4, 1), expected=[]),
]


@pytest.mark.parametrize("case", _cases)
def test_solution(case):
    sol = Solution()
    output = sol.combinationSum3(*case.args)
    assert output == case.expected
