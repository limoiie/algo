# noinspection PyUnresolvedReferences
from typing import *

import pytest

from algo.datatypes import ListNode


# noinspection PyPep8Naming,PyMethodMayBeStatic
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head
        while curr is not None:
            next_ = curr.next
            curr.next = prev
            prev = curr
            curr = next_
        return prev


_cases = [
    ((),),
]


@pytest.mark.parametrize("inputs,expected", _cases)
def test_sol206(inputs, expected):
    sol = Solution()
    output = sol.reverseList(*inputs)
    assert output == expected
