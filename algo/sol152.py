from algo import *


# noinspection PyPep8Naming,PyMethodMayBeStatic
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        product = 1
        skip_first_product = -math.inf
        max_product = nums[-1]
        for num in nums:
            if num == 0:
                product = 1
                skip_first_product = 0
            elif num > 0:
                product *= num
                skip_first_product *= num
                max_product = max(max_product, product, skip_first_product)
            elif num < 0:
                product = product * num
                if not math.isinf(skip_first_product):
                    skip_first_product = skip_first_product * num
                max_product = max(max_product, product, skip_first_product)
                if math.isinf(skip_first_product) or skip_first_product == 0:
                    skip_first_product = 1
        return max_product


# leetcode submit region end(Prohibit modification and deletion)


_cases = [
    TestCase(args=([-2],), expected=-2),
    TestCase(args=([1, 0, -1, 2, 3, -5, -2],), expected=60),
    TestCase(args=([2, 3, -2, 4],), expected=6),
    TestCase(args=([2, 3, -2, 4, -3, 5, -1],), expected=720),
    TestCase(args=([3, -2, 4, -3, 5, -4, 2],), expected=480),
    TestCase(args=([-2, 0, -1],), expected=0),
    TestCase(args=([-2, -1, 3],), expected=6),
]


@pytest.mark.parametrize("case", _cases)
def test_solution(case):
    sol = Solution()
    output = sol.maxProduct(*case.args)
    assert output == case.expected
