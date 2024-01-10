from . import *


# noinspection PyPep8Naming,PyMethodMayBeStatic
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def validateBinaryTreeNodes(
        self, n: int, leftChild: List[int], rightChild: List[int]
    ) -> bool:
        ufind = UnionFind(n)
        n_in_edges = [0] * n
        n_edges = 0
        for i in range(n):
            if leftChild[i] != -1:
                if n_in_edges[leftChild[i]] > 0:
                    return False
                n_in_edges[leftChild[i]] = 1
                ufind.union(i, leftChild[i])
                n_edges += 1
            if rightChild[i] != -1:
                if n_in_edges[rightChild[i]] > 0:
                    return False
                n_in_edges[rightChild[i]] = 1
                ufind.union(i, rightChild[i])
                n_edges += 1
        return ufind.s == 1 and n_edges + 1 == n


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


# leetcode submit region end(Prohibit modification and deletion)


_cases = [
    TestCase(args=(4, [1, -1, 3, -1], [2, -1, -1, -1]), expected=True),
    TestCase(args=(4, [1, -1, 3, -1], [2, 3, -1, -1]), expected=False),
    TestCase(args=(3, [1, -1, -1], [-1, -1, 1]), expected=False),
]


@pytest.mark.parametrize("case", _cases)
def test_solution(case):
    sol = Solution()
    output = sol.validateBinaryTreeNodes(*case.args)
    assert output == case.expected
