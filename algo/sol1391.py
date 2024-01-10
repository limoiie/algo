from . import *


# noinspection PyPep8Naming,PyMethodMayBeStatic
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        m, n = len(grid), len(grid[0])
        ufind = UnionFind(m, n)
        for i in range(m):
            for j in range(n):
                if i != 0:
                    if grid[i - 1][j] in [2, 3, 4] and grid[i][j] in [2, 5, 6]:
                        ufind.union((i - 1, j), (i, j))
                if j != 0:
                    if grid[i][j - 1] in [1, 4, 6] and grid[i][j] in [1, 3, 5]:
                        ufind.union((i, j - 1), (i, j))

        return ufind.find((0, 0)) == ufind.find((m - 1, n - 1))


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

    def union(self, i, j):
        pi = self.find(i)
        pj = self.find(j)
        self.p[pi] = pj


# leetcode submit region end(Prohibit modification and deletion)


_cases = [
    TestCase(
        args=([[2, 4, 3], [6, 5, 2]],),
        expected=True,
    ),
    TestCase(
        args=([[1, 2, 1], [1, 2, 1]],),
        expected=False,
    ),
    TestCase(
        args=([[1, 2, 1]],),
        expected=False,
    ),
]


@pytest.mark.parametrize("case", _cases)
def test_solution(case):
    sol = Solution()
    output = sol.hasValidPath(*case.args)
    assert output == case.expected
