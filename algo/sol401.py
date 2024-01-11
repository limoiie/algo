from algo import *


# noinspection PyPep8Naming,PyMethodMayBeStatic
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        return bt(turnedOn, 0, 10, 0)


def bt(turned: int, k: int, n: int, acc: int):
    if turned == 0:
        return [f"{acc >> 6}:{acc & 63:02}"]

    ans = []
    for i in range(k, n - turned + 1):
        nacc = acc | (1 << (n - i - 1))
        if (nacc & 63) > 59 or (nacc >> 6) > 11:
            continue
        ans += bt(turned - 1, i + 1, n, nacc)
    return reversed(ans)


# leetcode submit region end(Prohibit modification and deletion)


_cases = [
    TestCase(
        args=(2,),
        expected=[
            "0:01",
            "0:02",
            "0:04",
            "0:08",
            "0:16",
            "0:32",
            "1:00",
            "2:00",
            "4:00",
            "8:00",
        ],
    ),
]


@pytest.mark.parametrize("case", _cases)
def test_solution(case):
    sol = Solution()
    output = sol.readBinaryWatch(*case.args)
    assert output == case.expected
