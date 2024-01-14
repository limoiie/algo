import math

from algo import *


# noinspection PyPep8Naming,PyMethodMayBeStatic
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def judgePoint24(self, cards: List[int]) -> bool:
        return any(perm(cards, 0, 0))


def perm(cards, i, k):
    if k == 4:
        for res in calc(cards, 0, 4, 0, None):
            if abs(res - 24) < 1e-6:
                yield True
        return

    for j in range(i, len(cards)):
        cards[i], cards[j] = cards[j], cards[i]
        yield from perm(cards, i + 1, k + 1)
        cards[i], cards[j] = cards[j], cards[i]


def calc(nums, lo, hi, acc, factor):
    if lo == hi:
        yield acc if factor is None else (acc + factor)
        return

    if lo + 1 == hi:
        if factor is None:
            yield acc + nums[lo]
        else:
            yield acc + factor + nums[lo]
            yield acc + factor - nums[lo]
            yield acc + factor * nums[lo]
            yield acc + factor / nums[lo] if nums[lo] else math.inf
        return

    for j in range(lo + 1, hi + (factor is not None)):
        for res in calc(nums, lo, j, 0, None):
            if factor is None:
                yield from calc(nums, j, hi, acc, +res)
            else:
                yield from calc(nums, j, hi, acc + factor, +res)
                yield from calc(nums, j, hi, acc + factor, -res)
                yield from calc(nums, j, hi, acc, factor * res)
                yield from calc(nums, j, hi, acc, factor / res) if res else []


# leetcode submit region end(Prohibit modification and deletion)


_cases = [
    TestCase(args=([4, 1, 8, 7],), expected=True),
]


@pytest.mark.parametrize("case", _cases)
def test_solution(case):
    sol = Solution()
    output = sol.judgePoint24(*case.args)
    assert output == case.expected
