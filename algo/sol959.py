from algo import *


# leetcode submit region begin(Prohibit modification and deletion)
class UnionFind:
    def __init__(self, n):
        self.parents = [
            [[(i, j, k) for k in range(4)] for j in range(n)] for i in range(n)
        ]

    def union(self, i, j):
        pi = self.find(i)
        pj = self.find(j)

        if pi != pj:
            self.parents[pi[0]][pi[1]][pi[2]] = pj

    def find(self, i):
        pi = self.parents[i[0]][i[1]][i[2]]
        if pi != i:
            self.parents[i[0]][i[1]][i[2]] = self.find(pi)
        return self.parents[i[0]][i[1]][i[2]]


# noinspection PyPep8Naming,PyMethodMayBeStatic
class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        n = len(grid)
        ufind = UnionFind(n)

        def neighbors(x, y):
            for mk, nk, (dx, dy) in zip(
                [3, 0], [1, 2], [(0, -1), (-1, 0)]
            ):
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < n:
                    yield (x, y, mk), (nx, ny, nk)

        for i, row in enumerate(grid):
            for j, c in enumerate(row):
                if c == " ":
                    ufind.union((i, j, 0), (i, j, 1))
                    ufind.union((i, j, 0), (i, j, 2))
                    ufind.union((i, j, 0), (i, j, 3))

                elif c == "/":
                    ufind.union((i, j, 0), (i, j, 3))
                    ufind.union((i, j, 1), (i, j, 2))

                elif c == "\\":
                    ufind.union((i, j, 0), (i, j, 1))
                    ufind.union((i, j, 2), (i, j, 3))

                for mp, np in neighbors(i, j):
                    ufind.union(mp, np)

        roots = set()
        for i in range(n):
            for j in range(n):
                for k in range(4):
                    roots.add(ufind.find((i, j, k)))
        return len(roots)


# leetcode submit region end(Prohibit modification and deletion)


_cases = [
    TestCase(args=([" /", "  "],), expected=1),
    TestCase(args=([" /", "/ "],), expected=2),
]


@pytest.mark.parametrize("case", _cases)
def test_solution(case):
    sol = Solution()
    output = sol.regionsBySlashes(*case.args)
    assert output == case.expected
