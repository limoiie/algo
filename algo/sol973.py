from algo import *


# noinspection PyPep8Naming,PyMethodMayBeStatic
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        squares = [(x * x + y * y, i) for i, (x, y) in enumerate(points)]
        quick_select(squares, 0, len(squares) - 1, k)
        return [points[squares[i][1]] for i in range(k)]


def quick_select(nums, l, r, k):
    if l == r or k == 0:
        return

    i, j = l, l
    while j < r:
        if nums[j] <= nums[r]:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
        j += 1
    nums[i], nums[j] = nums[j], nums[i]

    if i - l + 1 == k:
        return

    if i - l + 1 > k:
        return quick_select(nums, l, i - 1, k)
    return quick_select(nums, i + 1, r, k - i + l - 1)


# leetcode submit region end(Prohibit modification and deletion)


_cases = [
    TestCase(
        args=([[6, 10], [-3, 3], [-2, 5], [0, 2]], 3),
        expected=[[0, 2], [-3, 3], [-2, 5]],
    ),
    TestCase(args=([[1, 3], [-2, 2]], 1), expected=[[-2, 2]]),
    TestCase(args=([[3, 3], [5, -1], [-2, 4]], 2), expected=[[3, 3], [-2, 4]]),
]


@pytest.mark.parametrize("case", _cases)
def test_solution(case):
    sol = Solution()
    output = sol.kClosest(*case.args)
    assert output == case.expected
