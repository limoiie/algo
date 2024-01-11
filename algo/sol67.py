from algo import *


# noinspection PyPep8Naming,PyMethodMayBeStatic
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        return bin(int(a, 2) + int(b, 2))[2:]


# leetcode submit region end(Prohibit modification and deletion)


_cases = [
    TestCase(
        args=(
            "11",
            "1",
        ),
        expected="100",
    ),
]


@pytest.mark.parametrize("case", _cases)
def test_solution(case):
    sol = Solution()
    output = sol.addBinary(*case.args)
    assert output == case.expected
