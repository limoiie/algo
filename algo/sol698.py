from algo import *


# noinspection PyPep8Naming,PyMethodMayBeStatic
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        total = sum(nums)
        if total // k * k != total:
            return False
        sub_sum = total // k

        nums.sort()

        def backtrace(sub_acc, included):
            if dp[included] is not None:
                return dp[included]

            if sub_acc == sub_sum:
                if included == (1 << n) - 1:
                    return True
                dp[included] = backtrace(0, included)
                return dp[included]

            for i in range(n):
                if (included & (1 << i) != 0) or sub_acc + nums[i] > sub_sum:
                    continue
                dp[included] = backtrace(sub_acc + nums[i], included | (1 << i))
                if dp[included]:
                    return True

            return False

        dp = [None] * (1 << n)
        return backtrace(0, 0)


# leetcode submit region end(Prohibit modification and deletion)


_cases = [
    TestCase(args=([4, 3, 2, 3, 5, 2, 1], 4), expected=True),
    TestCase(args=([1, 2, 3, 4], 3), expected=False),
]


@pytest.mark.parametrize("case", _cases)
def test_solution(case):
    sol = Solution()
    output = sol.canPartitionKSubsets(*case.args)
    assert output == case.expected
