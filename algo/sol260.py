from algo import *


# noinspection PyPep8Naming,PyMethodMayBeStatic
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        acc = 0
        for num in nums:
            acc ^= num
        last_diff_bit = acc & (-acc)

        a, b = 0, 0
        for num in nums:
            if num & last_diff_bit:
                a ^= num
            else:
                b ^= num
        return [a, b]


# leetcode submit region end(Prohibit modification and deletion)


_cases = [
    TestCase(args=(...,), expected=...),
]


@pytest.mark.parametrize("case", _cases)
def test_solution(case):
    sol = Solution()
    output = sol.singleNumber(*case.args)
    assert output == case.expected
