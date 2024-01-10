from . import *


# noinspection PyPep8Naming,PyMethodMayBeStatic
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n1, n2 = len(nums1), len(nums2)
        n = n1 + n2

        infinity = 1000_000_000
        lmax, rmin = 0, 0

        l, r = 0, n1
        while l <= r:
            m1 = (l + r) >> 1
            m2 = ((n + 1) >> 1) - m1

            if m2 > n2:
                l = m1 + 1
                continue
            if m2 < 0:
                r = m1 - 1
                continue

            l1v = nums1[m1 - 1] if m1 != 0 else -infinity
            r1v = nums1[m1] if m1 != n1 else infinity
            l2v = nums2[m2 - 1] if m2 != 0 else -infinity
            r2v = nums2[m2] if m2 != n2 else infinity

            if l1v <= r2v:
                lmax = max(l1v, l2v)
                rmin = min(r1v, r2v)
                l = m1 + 1

            else:
                r = m1 - 1

        return (lmax + rmin) / 2 if n & 1 == 0 else lmax


# leetcode submit region end(Prohibit modification and deletion)


_cases = [
    TestCase(args=([2], []), expected=2.0),
    TestCase(args=([3, 4], []), expected=3.5),
    TestCase(args=([1, 3], [2]), expected=2.0),
    TestCase(args=([1, 2], [3, 4]), expected=2.5),
]


@pytest.mark.parametrize("case", _cases)
def test_solution(case):
    sol = Solution()
    output = sol.findMedianSortedArrays(*case.args)
    assert output == case.expected
