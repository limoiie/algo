from . import *


# leetcode submit region begin(Prohibit modification and deletion)
class UnionFind:
    def __init__(self, m, n):
        self.p = list(range(m * n))
        self.s = [1] * (m * n)
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
        if px == py:
            return
        if px == 0:
            px, py = py, px
        self.p[px] = py
        self.s[py] += self.s[px]


# noinspection PyPep8Naming,PyMethodMayBeStatic
class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        ufind = UnionFind(m + 2, n + 2)
        for i in range(m + 2):
            ufind.union((i, 0), (0, 0))
            ufind.union((i, n + 1), (0, 0))
        for j in range(n + 2):
            ufind.union((0, j), (0, 0))
            ufind.union((m + 1, j), (0, 0))
        for i in range(1, m + 2):
            for j in range(1, n + 2):
                if (0 < i <= m) and (0 < j <= n) and grid[i - 1][j - 1] == 0:
                    ufind.union((i, j), (0, 0))
                    continue
                if i == 1 or (j != n + 1 and grid[i - 2][j - 1] == 1):
                    ufind.union((i, j), (i - 1, j))
                if j == 1 or (i != m + 1 and grid[i - 1][j - 2] == 1):
                    ufind.union((i, j), (i, j - 1))
        ans = 0
        for i, p in enumerate(ufind.p):
            if p == i and i != 0:
                ans += ufind.s[i]
        return ans


# leetcode submit region end(Prohibit modification and deletion)


_cases = [
    TestCase(
        args=([[0, 0, 0, 0], [1, 0, 1, 0], [0, 1, 1, 0], [0, 0, 0, 0]],), expected=3
    ),
    TestCase(
        args=(
            [
                # 1 2  3  4  5  6  7  8  9 10 11 12 13 14 15
                [0, 0, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 0, 0],  # 1
                [1, 1, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 1],  # 2
                [1, 1, 1, 0, 0, 1, 0, 1, 1, 1, 0, 0, 0, 1, 1],  # 3
                [1, 1, 0, 1, 0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 0],  # 4
                [1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1],  # 5
                [1, 0, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0],  # 6
                [0, 1, 0, 0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 0, 0],  # 7
                [0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0],  # 8
                [1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1],  # 9
                [1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 0, 1, 0],  # 10
            ],
        ),
        expected=27,
    ),
]


@pytest.mark.parametrize("case", _cases)
def test_solution(case):
    sol = Solution()
    output = sol.numEnclaves(*case.args)
    assert output == case.expected
