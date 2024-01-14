from algo import *


# noinspection PyPep8Naming,PyMethodMayBeStatic
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        return list(backtrace(s, 0, [], 0))


def backtrace(s, starting, path, k):
    if starting == len(s) and k == 4:
        yield ".".join(path)
        return

    for i in range(starting, len(s)):
        part = s[starting : i + 1]
        if not is_valid(part):
            break
        path.append(part)
        yield from backtrace(s, i + 1, path, k + 1)
        path.pop()


def is_valid(s):
    if s[0] == "0":
        return len(s) == 1
    return 0 <= int(s) <= 255


# leetcode submit region end(Prohibit modification and deletion)


_cases = [
    TestCase(args=("25525511135",), expected=["255.255.11.135", "255.255.111.35"]),
]


@pytest.mark.parametrize("case", _cases)
def test_solution(case):
    sol = Solution()
    output = sol.restoreIpAddresses(*case.args)
    assert output == case.expected
