from algo import *


# noinspection PyPep8Naming,PyMethodMayBeStatic
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        m, n = len(matrix), len(matrix[0])

        left = [0] * n
        right = [n] * n
        height = [0] * n
        max_area = 0

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == "1":
                    height[j] += 1
                else:
                    height[j] = 0

            cur_left = 0
            for j in range(n):
                if matrix[i][j] == "1":
                    left[j] = max(left[j], cur_left)
                else:
                    left[j] = 0
                    cur_left = j + 1

            cur_right = n
            for j in range(0, n)[::-1]:
                if matrix[i][j] == "1":
                    right[j] = min(right[j], cur_right)
                else:
                    right[j] = n
                    cur_right = j

            for j in range(n):
                max_area = max(max_area, height[j] * (right[j] - left[j]))

        return max_area


# leetcode submit region end(Prohibit modification and deletion)


_cases = [
    TestCase(args=([["1"]],), expected=1),
    TestCase(
        args=(
            [
                ["1", "0", "1", "0", "0"],
                ["1", "0", "1", "1", "1"],
                ["1", "1", "1", "1", "1"],
                ["1", "0", "0", "1", "0"],
            ],
        ),
        expected=6,
    ),
]


@pytest.mark.parametrize("case", _cases)
def test_solution(case):
    sol = Solution()
    output = sol.maximalRectangle(*case.args)
    assert output == case.expected
