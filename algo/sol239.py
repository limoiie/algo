import heapq

# noinspection PyUnresolvedReferences
from typing import *

import pytest

# noinspection PyUnresolvedReferences
from algo.datatypes import *


# noinspection PyPep8Naming,PyMethodMayBeStatic
class Solution:
    class Deque:
        def __init__(self, arr):
            self.i = 0
            self.k = len(arr)
            self.arr = arr

        def push(self, num):
            leftest = self.arr[self.i]
            self.arr[self.i] = num
            self.i = (self.i + 1) % self.k
            return leftest

    class Pique:
        def __init__(self, arr: List[int]):
            self.k = len(arr)
            self.arr = arr
            heapq.heapify(self.arr)

        def replace(self, popped: int, pushed: int):
            i = self.arr.index(popped)
            self.arr[i] = pushed
            # noinspection PyUnresolvedReferences,PyProtectedMember
            heapq._siftup(self.arr, i)
            # noinspection PyUnresolvedReferences,PyProtectedMember
            heapq._siftdown(self.arr, 0, i)

        def top(self):
            return self.arr[0]

    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        pq = Solution.Pique([-n for n in nums[:k]])
        dq = Solution.Deque([-n for n in nums[:k]])
        ans = [-pq.top()]
        for num in nums[k:]:
            leftest = dq.push(-num)
            pq.replace(leftest, -num)
            ans.append(-pq.top())
        return ans


_cases = [
    (([1, 3, -1, -3, 5, 3, 6, 7], 3), [3, 3, 5, 5, 6, 7]),
]


@pytest.mark.parametrize("inputs,expected", _cases)
def test_sol239(inputs, expected):
    sol = Solution()
    output = sol.maxSlidingWindow(*inputs)
    assert output == expected
