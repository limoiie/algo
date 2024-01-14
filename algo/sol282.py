from algo import *


# noinspection PyPep8Naming,PyMethodMayBeStatic
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        ans = []
        for i in range(len(num)):
            if num[0] == "0" and i > 0:
                continue
            part = num[: i + 1]
            ans += list(backtrace(num, i + 1, [part], 0, int(part), target))
        return ans


def backtrace(num, starting, path, acc, factor, target):
    if starting == len(num):
        if acc + factor == target:
            yield "".join(path[:])
        return

    for i in range(starting + 1, len(num) + 1):
        if num[starting] == "0" and i > starting + 1:
            break

        part = num[starting:i]

        path.append("+" + part)
        yield from backtrace(num, i, path, acc + factor, int(part), target)
        path.pop()

        path.append("-" + part)
        yield from backtrace(num, i, path, acc + factor, -int(part), target)
        path.pop()

        path.append("*" + part)
        yield from backtrace(num, i, path, acc, factor * int(part), target)
        path.pop()


# leetcode submit region end(Prohibit modification and deletion)


_cases = [
    TestCase(args=("123", 6), expected=["1*2*3", "1+2+3"]),
]


@pytest.mark.parametrize("case", _cases)
def test_solution(case):
    sol = Solution()
    output = sol.addOperators(*case.args)
    assert output == case.expected
