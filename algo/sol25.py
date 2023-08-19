# noinspection PyUnresolvedReferences
from typing import *

import pytest

from algo.datatypes import ListNode


# noinspection PyPep8Naming,PyMethodMayBeStatic
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        fake = ListNode(next_=head)

        prev, curr = fake, head
        while True:
            end = curr
            for i in range(k):
                if end is None:
                    break
                end = end.next
            else:
                next_prev = curr
                old_prev = prev
                prev = end
                while curr is not end:
                    next_ = curr.next
                    curr.next = prev
                    prev = curr
                    curr = next_
                old_prev.next = prev
                prev, curr = next_prev, end
                continue
            break

        return fake.next


_cases = [
    ((ListNode.make(1, 2, 3, 4, 5), 2), ListNode.make(2, 1, 4, 3, 5)),
]


@pytest.mark.parametrize("inputs,expected", _cases)
def test_sol25(inputs, expected):
    sol = Solution()
    output = sol.reverseKGroup(*inputs)
    assert output == expected
