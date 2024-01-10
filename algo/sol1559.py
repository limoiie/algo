from . import *


# noinspection PyPep8Naming,PyMethodMayBeStatic
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def containsCycle(self, grid: List[List[str]]) -> bool:
        m, n = len(grid), len(grid[0])
        ufind = UnionFind(m, n)
        for i in range(m):
            for j in range(n):
                if (
                    i != 0
                    and j != 0
                    and grid[i - 1][j] == grid[i][j - 1] == grid[i][j]
                    and ufind.find((i - 1, j)) == ufind.find((i, j - 1))
                ):
                    return True
                if i != 0 and grid[i][j] == grid[i - 1][j]:
                    ufind.union((i, j), (i - 1, j))
                if j != 0 and grid[i][j] == grid[i][j - 1]:
                    ufind.union((i, j), (i, j - 1))
        return False


class UnionFind:
    def __init__(self, m, n):
        self.p = list(range(m * n))
        self.m, self.n = m, n

    def _find(self, i):
        if self.p[i] != i:
            self.p[i] = self._find(self.p[i])
        return self.p[i]

    def find(self, x):
        return self._find(x[0] * self.n + x[1])

    def union(self, x, y):
        px = self.find(x)
        py = self.find(y)
        self.p[px] = py


# leetcode submit region end(Prohibit modification and deletion)


_cases = [
    TestCase(args=(...,), expected=...),
]


@pytest.mark.parametrize("case", _cases)
def test_solution(case):
    sol = Solution()
    output = sol.containsCycle(*case.args)
    assert output == case.expected
