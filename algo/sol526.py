from algo import *


# noinspection PyPep8Naming,PyMethodMayBeStatic
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def countArrangement(self, n: int) -> int:
        nums = [0] * (n + 1)

        def backtrace(num):
            nonlocal ans
            if num >= n + 1:
                ans += 1
                return

            for j in range(1, n + 1):
                if nums[j] == 0 and ((num % j) == 0 or (j % num) == 0):
                    nums[j] = num
                    backtrace(num + 1)
                    nums[j] = 0

        ans = 0
        backtrace(1)
        return ans


# leetcode submit region end(Prohibit modification and deletion)


_cases = [
    TestCase(args=(2,), expected=2),
    TestCase(args=(4,), expected=8),
    TestCase(args=(6,), expected=36),
    TestCase(args=(10,), expected=...),
    TestCase(args=(15,), expected=...),
]


@pytest.mark.parametrize("case", _cases)
def test_solution(case):
    sol = Solution()
    output = sol.countArrangement(*case.args)
    assert output == case.expected
