from . import *


# noinspection PyPep8Naming,PyMethodMayBeStatic
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        row_slots, col_slots = [0] * m, [0] * n
        cnt = 0
        for i, row in enumerate(grid):
            for j, c in enumerate(row):
                if c == 1:
                    row_slots[i] += 1
                    col_slots[j] += 1
                    cnt += 1

        for i, row in enumerate(grid):
            for j, c in enumerate(row):
                if c == 1 and row_slots[i] == 1 and col_slots[j] == 1:
                    cnt -= 1
                    continue
        return cnt


# leetcode submit region end(Prohibit modification and deletion)


_cases = [
    TestCase(args=([[1, 0], [0, 1]],), expected=0),
    TestCase(args=([[1, 0], [1, 1]],), expected=3),
]


@pytest.mark.parametrize("case", _cases)
def test_solution(case):
    sol = Solution()
    output = sol.countServers(*case.args)
    assert output == case.expected
