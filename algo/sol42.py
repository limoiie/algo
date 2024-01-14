from algo import *


# noinspection PyPep8Naming,PyMethodMayBeStatic
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def trap(self, height: List[int]) -> int:
        acc = 0
        left_stack = []
        for i, h in enumerate(height):
            horizon = 0
            while left_stack and left_stack[-1][1] <= h:
                pi, ph = left_stack.pop()
                acc += (ph - horizon) * (i - pi - 1)
                horizon = ph
            if left_stack:
                pi, _ = left_stack[-1]
                acc += (h - horizon) * (i - pi - 1)
            left_stack.append((i, h))
        return acc


# leetcode submit region end(Prohibit modification and deletion)


_cases = [
    TestCase(args=([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1],), expected=6),
    TestCase(args=([4, 2, 0, 3, 2, 5],), expected=9),
]


@pytest.mark.parametrize("case", _cases)
def test_solution(case):
    sol = Solution()
    output = sol.trap(*case.args)
    assert output == case.expected
