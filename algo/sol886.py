# noinspection PyUnresolvedReferences
from typing import *

import pytest


class UnionFind:
    def __init__(self, n):
        self.parents = list(range(n))

    def union(self, i, j):
        self.parents[self.find(i)] = self.find(j)

    def find(self, i):
        if self.parents[i] != i:
            self.parents[i] = self.find(self.parents[i])
        return self.parents[i]


# noinspection PyPep8Naming,PyMethodMayBeStatic
class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]):
        ufind = UnionFind(n + 1)
        dislike_map = dict()

        for a, b in dislikes:
            root_a = ufind.find(a)
            root_b = ufind.find(b)

            if root_a == root_b:
                return False

            if root_a in dislike_map and root_b in dislike_map:
                if ufind.find(dislike_map[root_a]) == ufind.find(dislike_map[root_b]):
                    return False

                ufind.union(root_a, dislike_map[root_b])
                ufind.union(root_b, dislike_map[root_a])

            elif root_a in dislike_map:
                ufind.union(b, dislike_map[root_a])

            elif root_b in dislike_map:
                ufind.union(a, dislike_map[root_b])

            else:
                dislike_map[root_a] = root_b
                dislike_map[root_b] = root_a

        return True


_cases = [
    ((4, [[1, 2], [1, 3], [2, 4]]), True),
    ((3, [[1, 2], [1, 3], [2, 3]]), False),
    ((10, [[1, 2], [3, 4], [5, 6], [6, 7], [8, 9], [7, 8]]), True),
    ((4, [[1, 2], [3, 4], [1, 3], [1, 4]]), False),
]


@pytest.mark.parametrize("inputs,expected", _cases)
def test_sol886(inputs, expected):
    sol = Solution()
    output = sol.possibleBipartition(*inputs)
    assert output == expected
