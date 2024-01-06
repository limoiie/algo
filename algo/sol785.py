# noinspection PyUnresolvedReferences
from typing import *

import pytest


# noinspection PyPep8Naming,PyMethodMayBeStatic
class Solution:
    n: int
    graph: List[List[int]]

    def isBipartite(self, graph: List[List[int]]):
        self.graph = graph
        self.n = len(graph)
        color = [None] * self.n

        while True:
            edge = self.first_edge()
            if not edge:
                break

            stack = [edge]
            self.remove_edge(edge)

            while stack:
                l, r = stack.pop()
                l_root, r_root = color[l], color[r]
                if l_root is not None and l_root == r_root:
                    return False

                color[l] = True
                color[r] = False

                for i in range(self.n):
                    if i in graph[l]:
                        stack.append((l, i))
                        self.remove_edge((l, i))

                    if i in graph[r]:
                        stack.append((i, r))
                        self.remove_edge((r, i))

        return True

    def first_edge(self):
        for i, nodes in enumerate(self.graph):
            if nodes:
                return i, nodes[0]

    def remove_edge(self, edge):
        l, r = edge
        self.graph[l].remove(r)
        self.graph[r].remove(l)


_cases = [
    (([[1, 2, 3], [0, 2], [0, 1, 3], [0, 2]],), False),
    (([[1, 3], [0, 2], [1, 3], [0, 2]],), True),
]


@pytest.mark.parametrize("inputs,expected", _cases)
def test_sol785(inputs, expected):
    sol = Solution()
    output = sol.isBipartite(*inputs)
    assert output == expected
