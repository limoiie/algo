from . import *


# noinspection PyPep8Naming,PyMethodMayBeStatic
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    MOD = 1000_000_007

    def numOfWays(self, nums: List[int]) -> int:
        return self.num_of_ways(nums) - 1

    def num_of_ways(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return 1

        root, left, right = nums[0], [], []
        for num in nums:
            if num < root:
                left.append(num)
            elif num > root:
                right.append(num)

        return (
            (self.num_of_ways(left) * self.num_of_ways(right) % self.MOD)
            * (self.num_of_mix_ways(len(nums) - 1, len(left)) % self.MOD)
            % self.MOD
        )

    def num_of_mix_ways(self, n, k):
        dp = [[0] * (k + 1) for _ in range(n + 1)]
        for i in range(n + 1):
            dp[i][0] = 1
            for j in range(1, min(i, k) + 1):
                dp[i][j] = (dp[i - 1][j - 1] + dp[i - 1][j]) % self.MOD
        return dp[n][k]


# leetcode submit region end(Prohibit modification and deletion)


_cases = [
    TestCase(args=([3, 4, 5, 1, 2],), expected=5),
]


@pytest.mark.parametrize("case", _cases)
def test_solution(case):
    sol = Solution()
    output = sol.numOfWays(*case.args)
    assert output == case.expected
