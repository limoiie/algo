# noinspection PyUnresolvedReferences
from typing import *

import pytest

from algo.datatypes import TreeNode


# noinspection PyPep8Naming,PyMethodMayBeStatic
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        stack = [root]
        reverse = False
        while len(stack):
            level = []
            next_stack = []
            for elem in stack:
                if elem is not None:
                    level.append(elem.val)
                    next_stack.append(elem.left)
                    next_stack.append(elem.right)
            if len(level) == 0:
                break
            if reverse:
                level.reverse()
            res.append(level)
            stack = next_stack
            reverse = not reverse
        return res


_cases = [
    ((),),
]


@pytest.mark.parametrize("inputs,expected", _cases)
def test_sol103(inputs, expected):
    sol = Solution()
    output = sol.zigzagLevelOrder(*inputs)
    assert output == expected
