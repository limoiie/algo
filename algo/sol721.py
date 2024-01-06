# noinspection PyUnresolvedReferences
from typing import *

import pytest


class UnionFind:
    def __init__(self, n):
        self._parents = list(range(n))

    def union(self, i, j):
        self._parents[self.find(i)] = self.find(j)

    def find(self, i):
        return i if self._parents[i] == i else self.find(self._parents[i])


# noinspection PyPep8Naming,PyMethodMayBeStatic
class Solution:
    def accountsMerge(self, accounts: List[List[str]]):
        ufind = UnionFind(len(accounts))
        emails_to_account_idx = dict()
        for i, (name, *emails) in enumerate(accounts):
            for email in emails:
                j = emails_to_account_idx.setdefault(email, i)
                if i != j:
                    ufind.union(i, j)

        unique_accounts = dict()
        for i, (name, *emails) in enumerate(accounts):
            root_i = ufind.find(i)
            root = unique_accounts.setdefault(root_i, [name])
            root.extend(emails)

        return [
            [name] + sorted(set(emails)) for name, *emails in unique_accounts.values()
        ]


_cases = [
    (
        (
            [
                ["John", "johnsmith@mail.com", "john_newyork@mail.com"],
                ["John", "johnsmith@mail.com", "john00@mail.com"],
                ["Mary", "mary@mail.com"],
                ["John", "johnnybravo@mail.com"],
            ],
        ),
        [
            ["John", "john00@mail.com", "john_newyork@mail.com", "johnsmith@mail.com"],
            ["Mary", "mary@mail.com"],
            ["John", "johnnybravo@mail.com"],
        ],
    ),
]


@pytest.mark.parametrize("inputs,expected", _cases)
def test_sol721(inputs, expected):
    sol = Solution()
    output = sol.accountsMerge(*inputs)
    assert output == expected
