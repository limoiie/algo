import itertools

# noinspection PyUnresolvedReferences
from typing import *

import pytest

# noinspection PyUnresolvedReferences
from algo.datatypes import *


class UnionFind:
    def __init__(self, variables: list[str]):
        self._vars = variables
        self._prev = list(range(len(variables)))
        self._weight = [1.0] * len(variables)

    def find(self, x: int) -> int:
        if self._prev[x] != x:
            self._prev[x], w = self.find(self._prev[x])
            self._weight[x] *= w
        return self._prev[x], self._weight[x]

    def union(self, x: int, y: int, w: float) -> None:
        px, wx = self.find(x)
        py, wy = self.find(y)
        if px != py:
            self._prev[px] = py
            self._weight[px] = w * wy / wx

    def index(self, x: str) -> int:
        return self._vars.index(x)

    def valid(self, x: str):
        return x in self._vars


# noinspection PyPep8Naming,PyMethodMayBeStatic
class Solution:
    def calcEquation(
        self, equations: List[List[str]], values: List[float], queries: List[List[str]]
    ) -> List[float]:
        u_find = UnionFind(list(set(itertools.chain(*equations))))
        for (u, v), w in zip(equations, values):
            u_find.union(u_find.index(u), u_find.index(v), w)

        ans = []
        for u, v in queries:
            try:
                u = u_find.index(u)
                v = u_find.index(v)
            except ValueError:
                ans.append(-1)
                continue
            pu, wu = u_find.find(u)
            pv, wv = u_find.find(v)
            if pv != pu:
                ans.append(-1)
                continue
            ans.append(wu / wv)
        return ans


_cases = [
    (
        (
            [["a", "b"], ["b", "c"]],
            [2.0, 3.0],
            [["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"]],
        ),
        [6.0, 0.5, -1.0, 1.0, -1.0],
    ),
]


@pytest.mark.parametrize("inputs,expected", _cases)
def test_sol399(inputs, expected):
    sol = Solution()
    output = sol.calcEquation(*inputs)
    assert output == expected
