from algo import *


# noinspection PyPep8Naming,PyMethodMayBeStatic
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        n = len(nums)

        def merge_sort(lo, hi):
            if hi - lo < 2:
                return 0

            m = (lo + hi) >> 1
            count = merge_sort(lo, m) + merge_sort(m, hi)

            t = lo
            for j in range(m, hi):
                t = bisect.bisect_right(nums, 2 * nums[j], lo=t, hi=m)
                count += m - t

            nums[lo:hi] = sorted(nums[lo:hi])
            return count

        return merge_sort(lo=0, hi=n)


# leetcode submit region end(Prohibit modification and deletion)


_cases = [
    TestCase(args=([1, 3, 2, 3, 1],), expected=2),
    TestCase(args=([2, 4, 3, 5, 1],), expected=3),
]


@pytest.mark.parametrize("case", _cases)
def test_solution(case):
    sol = Solution()
    output = sol.reversePairs(*case.args)
    assert output == case.expected
