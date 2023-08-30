import queue
# noinspection PyUnresolvedReferences
from typing import *

import pytest

# noinspection PyUnresolvedReferences
from algo.datatypes import *


# noinspection PyPep8Naming,PyMethodMayBeStatic
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]):
        q = queue.PriorityQueue(len(lists))
        for l in lists:
            if l:
                q.put((l.val, l))

        head = ListNode(0)
        curr = head
        while not q.empty():
            _, l = q.get()
            curr.next = l
            curr = curr.next
            l = l.next
            if l is not None:
                q.put((l.val, l))
        return head.next


_cases = [
    ((),),
]


@pytest.mark.parametrize("inputs,expected", _cases)
def test_sol23(inputs, expected):
    sol = Solution()
    output = sol.mergeKLists(*inputs)
    assert output == expected
