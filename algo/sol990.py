from . import *


# leetcode submit region begin(Prohibit modification and deletion)
class UnionFind:
    def __init__(self):
        self.parents = dict()
        self.exclusive = dict()

    def union(self, i, j):
        pi = self.find(i)
        pj = self.find(j)

        if pi != pj:
            self.exclusive.setdefault(pi, set())
            self.exclusive.setdefault(pj, set())

            if pj in self.exclusive[pi] or pi in self.exclusive[pj]:
                return False

            self.exclusive[pj].union(self.exclusive[pi])
            self.parents[pi] = pj

        return True

    def exclude(self, i, j):
        pi = self.find(i)
        pj = self.find(j)

        if pi == pj:
            return False

        self.exclusive.setdefault(pi, set()).add(pj)
        self.exclusive.setdefault(pj, set()).add(pi)

        return True

    def find(self, i):
        self.parents.setdefault(i, i)
        if self.parents[i] != i:
            self.parents[i] = self.find(self.parents[i])
        return self.parents[i]


# noinspection PyPep8Naming,PyMethodMayBeStatic
class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        ufind = UnionFind()
        for eq in equations:
            l, s, _, r = eq
            if s == '=':
                if not ufind.union(l, r):
                    return False
            else:
                if not ufind.exclude(l, r):
                    return False
        return True
        
# leetcode submit region end(Prohibit modification and deletion)


_cases = [
    TestCase(args=(...,), expected=...),
]


@pytest.mark.parametrize("case", _cases)
def test_solution(case):
    sol = Solution()
    output = sol.method(*case.args)
    assert output == case.expected
