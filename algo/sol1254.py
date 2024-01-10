from . import *


# leetcode submit region begin(Prohibit modification and deletion)
class UnionFind:
    def __init__(self, m, n):
        self.p = list(range(m * n))
        self.s = m * n
        self.m, self.n = m, n

    def _find(self, i):
        if self.p[i] != i:
            self.p[i] = self._find(self.p[i])
        return self.p[i]

    def find(self, point):
        return self._find(point[0] * self.n + point[1])

    def union(self, x, y):
        px = self.find(x)
        py = self.find(y)

        if px != py:
            self.p[px] = py
            self.s -= 1


# noinspection PyPep8Naming,PyMethodMayBeStatic
class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        ufind = UnionFind(m + 2, n + 2)

        for i in range(m + 2):
            ufind.union((i, 0), (0, 0))
        for j in range(n + 2):
            ufind.union((0, j), (0, 0))

        for i in range(1, m + 2):
            for j in range(1, n + 2):
                if 0 < i <= m and 0 < j <= n and grid[i - 1][j - 1] == 1:
                    ufind.union((i, j), (0, 0))
                    continue

                if i == 1 or j == n + 1 or grid[i - 2][j - 1] == 0:
                    ufind.union((i, j), (i - 1, j))
                if j == 1 or i == m + 1 or grid[i - 1][j - 2] == 0:
                    ufind.union((i, j), (i, j - 1))
        return ufind.s - 1


# leetcode submit region end(Prohibit modification and deletion)


_cases = [
    TestCase(
        args=(
            [
                [1, 1, 1, 1, 1, 1, 1, 0],
                [1, 0, 0, 0, 0, 1, 1, 0],
                [1, 0, 1, 0, 1, 1, 1, 0],
                [1, 0, 0, 0, 0, 1, 0, 1],
                [1, 1, 1, 1, 1, 1, 1, 0],
            ],
        ),
        expected=2,
    ),
    TestCase(args=([[0, 0, 1, 0, 0], [0, 1, 0, 1, 0], [0, 1, 1, 1, 0]],), expected=1),
]


@pytest.mark.parametrize("case", _cases)
def test_solution(case):
    sol = Solution()
    output = sol.closedIsland(*case.args)
    assert output == case.expected
