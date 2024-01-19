from algo import *


# noinspection PyPep8Naming,PyMethodMayBeStatic
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def fallingSquares(self, positions: List[List[int]]) -> List[int]:
        points = set()
        for left, side_len in positions:
            points.add(left)
            points.add(left + side_len)

        points_dict = {}
        points = sorted(points)
        for i, point in enumerate(points):
            points_dict[point] = i

        squares = []
        for left, side_len in positions:
            left, right = points_dict[left], points_dict[left + side_len]
            squares.append((left, right))
        positions = squares

        ans = []
        max_real_height = -math.inf
        tree = SegmentTree(len(points))
        for left, right in positions:
            real_side_len = points[right] - points[left]
            real_height = tree.query(left, right) + real_side_len
            max_real_height = max(max_real_height, real_height)
            ans.append(max_real_height)
            tree.update(left, right, real_height)
        return ans


class SegmentTree:
    def __init__(self, n):
        self.n = n
        self.tree = [0] * (n << 2)

    def _update(self, i, lo, hi, qlo, qhi, val: int):
        if qlo >= hi or qhi <= lo:
            return
        if lo + 1 == hi:
            self.tree[i] = val
            return

        m = (lo + hi) >> 1
        self._update((i << 1) + 1, lo, m, qlo, qhi, val)
        self._update((i << 1) + 2, m, hi, qlo, qhi, val)
        self.tree[i] = max(self.tree[(i << 1) + 1], self.tree[(i << 1) + 2])

    def _query(self, i, lo, hi, qlo, qhi):
        if qlo >= hi or qhi <= lo:
            return -math.inf
        if qlo <= lo and hi <= qhi:
            return self.tree[i]

        m = (lo + hi) >> 1
        l_max = self._query((i << 1) + 1, lo, m, qlo, qhi)
        r_max = self._query((i << 1) + 2, m, hi, qlo, qhi)
        return max(l_max, r_max)

    def update(self, qlo: int, qhi: int, val: int):
        return self._update(0, 0, self.n, qlo, qhi, val)

    def query(self, qlo: int, qhi: int):
        return self._query(0, 0, self.n, qlo, qhi)


# leetcode submit region end(Prohibit modification and deletion)


_cases = [
    TestCase(args=([[6, 1], [9, 2], [2, 4]],), expected=[1, 2, 4]),
    TestCase(args=([[1, 2], [2, 3], [6, 1]],), expected=[2, 5, 5]),
    TestCase(args=([[100, 100], [200, 100]],), expected=[100, 100]),
]


@pytest.mark.parametrize("case", _cases)
def test_solution(case):
    sol = Solution()
    output = sol.fallingSquares(*case.args)
    assert output == case.expected
