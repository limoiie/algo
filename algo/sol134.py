from typing import *

import pytest


# noinspection PyPep8Naming,PyMethodMayBeStatic
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        start_idx, total_acc, cand_acc = 0, 0, 0
        for i in range(len(gas)):
            diff = gas[i] - cost[i]
            total_acc += diff
            cand_acc += diff
            if cand_acc < 0:
                cand_acc = 0
                start_idx = i + 1

        return start_idx if total_acc >= 0 else -1


_cases = [
    (([1, 2, 3, 4, 5], [3, 4, 5, 1, 2]), 3),
    (([2, 3, 4], [3, 4, 3]), -1),
]


@pytest.mark.parametrize("inputs,expected", _cases)
def test_sol134(inputs, expected):
    sol = Solution()
    output = sol.canCompleteCircuit(*inputs)
    assert output == expected
