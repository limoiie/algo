# noinspection PyUnresolvedReferences
from typing import *

import pytest

# noinspection PyUnresolvedReferences
from algo.datatypes import *


# noinspection PyPep8Naming,PyMethodMayBeStatic
class Solution:
    def findRedundantDirectedConnection(self, edges: List[List[int]]) -> List[int]:
        gc, gp, n = dict(), dict(), len(edges)
        for s, e in edges:
            gc.setdefault(s, []).append(e)
            gp.setdefault(e, []).append(s)

        def collect(x):
            if not gc.get(x, None):  # without children
                if len(ps := gp.get(x, [])) == 2:  # with two parents
                    for p, c in reversed(edges):
                        if c == x and p in ps:
                            return [p, c]
                free.append(x)

        free = []
        for i in range(1, n + 1):
            if edge := collect(i):
                return edge

        while free:
            i = free.pop()
            for ip in gp.pop(i, []):
                gc[ip].remove(i)
                if not gc[ip]:
                    del gc[ip]

                if edge := collect(ip):
                    return edge

        for i in gc.keys():
            if not gp.get(i, None):
                while True:
                    (c,) = gc.get(i, [])
                    cps = gp.get(c, [])
                    if len(cps) == 2:
                        p1, p2 = cps
                        return [p1, c] if i == p2 else [p2, c]
                    i = c

        for s, e in reversed(edges):
            if e in gc.get(s, []):
                return [s, e]


_cases = [
    (([[1, 2], [1, 3], [2, 3]],), [2, 3]),
    (([[1, 2], [2, 3], [3, 4], [4, 1], [1, 5]],), [4, 1]),
    (([[2, 1], [3, 1], [4, 2], [1, 4]],), [2, 1]),
    (([[1, 4], [5, 2], [1, 3], [4, 5], [1, 5]],), [1, 5]),
    (([[1, 2], [2, 1], [2, 3], [3, 4]],), [2, 1])
]


@pytest.mark.parametrize("inputs,expected", _cases)
def test_sol685(inputs, expected):
    sol = Solution()
    output = sol.findRedundantDirectedConnection(*inputs)
    assert output == expected
