from algo import *


# noinspection PyPep8Naming,PyMethodMayBeStatic
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def kthLargestValue(self, matrix: List[List[int]], k: int) -> int:
        m, n = len(matrix), len(matrix[0])
        for i in range(1, m):
            matrix[i][0] ^= matrix[i - 1][0]
        for j in range(1, n):
            matrix[0][j] ^= matrix[0][j - 1]

        for i in range(1, m):
            for j in range(1, n):
                matrix[i][j] ^= (
                    matrix[i - 1][j] ^ matrix[i][j - 1] ^ matrix[i - 1][j - 1]
                )

        q = []
        for row in matrix:
            for elem in row:
                heapq.heappush(q, elem)
                if len(q) > k:
                    heapq.heappop(q)
        return heapq.heappop(q)


# leetcode submit region end(Prohibit modification and deletion)


_cases = [
    TestCase(args=([[5, 2], [1, 6]], 1), expected=7),
    TestCase(args=([[5, 2], [1, 6]], 2), expected=5),
    TestCase(args=([[5, 2], [1, 6]], 3), expected=4),
]


@pytest.mark.parametrize("case", _cases)
def test_solution(case):
    sol = Solution()
    output = sol.kthLargestValue(*case.args)
    assert output == case.expected
