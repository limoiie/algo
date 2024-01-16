from algo import *


# noinspection PyPep8Naming,PyMethodMayBeStatic
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        row = [1]
        for _ in range(rowIndex):
            next_row = [1]
            for i in range(1, len(row)):
                next_row.append(row[i] + row[i - 1])
            next_row.append(1)
            row = next_row
        return row


# leetcode submit region end(Prohibit modification and deletion)


_cases = [
    TestCase(args=(3,), expected=[1, 3, 3, 1]),
    TestCase(args=(0,), expected=[1]),
    TestCase(args=(1,), expected=[1, 1]),
]


@pytest.mark.parametrize("case", _cases)
def test_solution(case):
    sol = Solution()
    output = sol.getRow(*case.args)
    assert output == case.expected
