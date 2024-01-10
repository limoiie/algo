from . import *


# noinspection PyPep8Naming,PyMethodMayBeStatic
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    mst_list: List[List[int]]

    def findCriticalAndPseudoCriticalEdges(
        self, n: int, edges: List[List[int]]
    ) -> List[List[int]]:
        critical = []
        pseudo_critical = []
        edges = sorted((w, a, b, i) for i, (a, b, w) in enumerate(edges))
        min_mst_sum = self.find_mst_sum(n, edges)
        for i, (w, a, b, idx) in enumerate(edges):
            mst_sum = self.find_mst_sum(n, edges, skip=i)
            if mst_sum != min_mst_sum:
                critical.append(idx)
                continue
            mst_sum = self.find_mst_sum(n, edges, fix_pair=(a, b, w))
            if mst_sum == min_mst_sum:
                pseudo_critical.append(idx)

        return [
            sorted(critical),
            sorted(pseudo_critical),
        ]

    def find_mst_sum(self, n, edges, skip=-1, fix_pair=None):
        ans = 0
        ufind = UnionFind(n)
        if fix_pair:
            a, b, w = fix_pair
            if ufind.union(a, b):
                ans += w
                n -= 1
                if n == 1:
                    return ans
        for i, (w, a, b, idx) in enumerate(edges):
            if i == skip:
                continue
            if ufind.union(a, b):
                ans += w
                n -= 1
                if n == 1:
                    return ans
        return -1


class UnionFind:
    def __init__(self, n):
        self.p = list(range(n))

    def find(self, i):
        if self.p[i] != i:
            self.p[i] = self.find(self.p[i])
        return self.p[i]

    def union(self, i, j):
        pi = self.find(i)
        pj = self.find(j)
        if pi == pj:
            return False
        self.p[pi] = pj
        return True


# leetcode submit region end(Prohibit modification and deletion)


_cases = [
    TestCase(
        args=(
            5,
            [
                [0, 1, 1],
                [1, 2, 1],
                [2, 3, 2],
                [0, 3, 2],
                [0, 4, 3],
                [3, 4, 3],
                [1, 4, 6],
            ],
        ),
        expected=[[0, 1], [2, 3, 4, 5]],
    ),
]


@pytest.mark.parametrize("case", _cases)
def test_solution(case):
    sol = Solution()
    output = sol.findCriticalAndPseudoCriticalEdges(*case.args)
    assert output == case.expected
