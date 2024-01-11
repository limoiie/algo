from algo import *


# noinspection PyPep8Naming,PyMethodMayBeStatic
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def countBits(self, n: int) -> List[int]:
        return self.compute(n, 0)

    def compute(self, n: int, prefix_ones: int):
        if n == 0:
            return [prefix_ones]
        h = n_leftmost_bit(n)
        mask = (1 << h) - 1
        return [x + prefix_ones for x in dp[h]] + self.compute(
            n & mask, prefix_ones + 1
        )


dp = [[0]] * 20
for i in range(1, len(dp)):
    dp[i] = dp[i - 1] + [x + 1 for x in dp[i - 1]]


def n_leftmost_bit(n: int):
    h = 0
    while n:
        n >>= 1
        h += 1
    return h - 1


# leetcode submit region end(Prohibit modification and deletion)


_cases = [
    TestCase(args=(2,), expected=[0, 1, 1]),
    TestCase(args=(5,), expected=[0, 1, 1, 2, 1, 2]),
]


@pytest.mark.parametrize("case", _cases)
def test_solution(case):
    sol = Solution()
    output = sol.countBits(*case.args)
    assert output == case.expected
