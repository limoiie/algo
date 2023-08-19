# noinspection PyUnresolvedReferences
from typing import *

import pytest

from algo.datatypes import ListNode


# noinspection PyPep8Naming,PyMethodMayBeStatic
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None:
            return False

        slow = head
        fast = head.next
        while slow != fast:
            if fast is None or fast.next is None:
                return False
            slow = slow.next
            fast = fast.next.next
        return True


_cases = [
    ((),),
]


@pytest.mark.parametrize("inputs,expected", _cases)
def test_sol141(inputs, expected):
    sol = Solution()
    output = sol.hasCycle(*inputs)
    assert output == expected
