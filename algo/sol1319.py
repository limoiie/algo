from . import *


# leetcode submit region begin(Prohibit modification and deletion)
class UnionFind:
    def __init__(self, n):
        self.p = list(range(n))
        self.s = n

    def find(self, i):
        if self.p[i] != i:
            self.p[i] = self.find(self.p[i])
        return self.p[i]

    def union(self, i, j):
        pi = self.find(i)
        pj = self.find(j)

        if pi != pj:
            self.p[pi] = pj
            self.s -= 1


# noinspection PyPep8Naming,PyMethodMayBeStatic
class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        if len(connections) < n - 1:
            return -1

        ufind = UnionFind(n)
        for a, b in connections:
            ufind.union(a, b)

        return ufind.s - 1


# leetcode submit region end(Prohibit modification and deletion)


_cases = [
    TestCase(
        args=(
            4,
            [[0, 1], [0, 2], [1, 2]],
        ),
        expected=1,
    ),
    TestCase(
        args=(
            6,
            [[0, 1], [0, 2], [0, 3], [1, 2], [1, 3]],
        ),
        expected=2,
    ),
    TestCase(
        args=(
            6,
            [[0, 1], [0, 2], [0, 3], [1, 2]],
        ),
        expected=-1,
    ),
]


@pytest.mark.parametrize("case", _cases)
def test_solution(case):
    sol = Solution()
    output = sol.makeConnected(*case.args)
    assert output == case.expected
