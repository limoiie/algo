# noinspection PyUnresolvedReferences
from typing import *

import pytest


class UnionFind:
    def __init__(self, n):
        self.parents = list(range(n))
        self.counts = [1] * n

    def find(self, x):
        if self.parents[x] != x:
            self.parents[x] = self.find(self.parents[x])
        return self.parents[x]

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x != root_y:
            if root_x > root_y:
                root_x, root_y = root_y, root_x
            self.parents[root_x] = root_y
            self.counts[root_y] += self.counts[root_x]


# noinspection PyPep8Naming,PyMethodMayBeStatic
class Solution:
    def minMalwareSpread(self, graph: List[List[int]], initial: List[int]):
        n = len(graph)
        ufind = UnionFind(n)

        # union all connected non-initial nodes
        for i in range(n):
            if i not in initial:
                for j in range(i + 1, n):
                    if j not in initial and graph[i][j]:
                        ufind.union(i, j)

        # collect all initial nodes for those infected root nodes
        inf = [set() for _ in range(n)]  # map infected root to initial nodes doing that
        for i in initial:
            for j in range(n):
                if j not in initial and graph[i][j]:
                    j_root = ufind.find(j)
                    inf[j_root].add(i)

        # count nodes infected by each single initial node, respectively
        score = [0] * n
        for i in range(n):
            if len(inf[i]) == 1:
                (j,) = inf[i]
                score[j] += ufind.counts[i]

        ans = min(initial)
        max_score = 0
        for i in initial:
            if score[i] > max_score:
                max_score = score[i]
                ans = i
            elif score[i] == max_score and i < ans:
                ans = i

        return ans


_cases = [
    (([[1, 1, 0], [1, 1, 0], [0, 0, 1]], [0, 1]), 0),
    (([[1, 1, 0], [1, 1, 1], [0, 1, 1]], [0, 1]), 1),
    (([[1, 1, 0, 0], [1, 1, 1, 0], [0, 1, 1, 1], [0, 0, 1, 1]], [0, 1]), 1),
    (
        (
            [
                [1, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 1, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 1, 0, 1, 0, 1, 0, 0],
                [0, 0, 0, 1, 0, 0, 0, 0, 0],
                [0, 0, 1, 0, 1, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 1, 0, 0, 0],
                [0, 0, 1, 0, 0, 0, 1, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 1, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 1],
            ],
            [6, 0, 4],
        ),
        0,
    ),
]


@pytest.mark.parametrize("inputs,expected", _cases)
def test_sol928(inputs, expected):
    sol = Solution()
    output = sol.minMalwareSpread(*inputs)
    assert output == expected
