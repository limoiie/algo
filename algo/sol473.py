from algo import *


# noinspection PyPep8Naming,PyMethodMayBeStatic
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        n = len(matchsticks)
        circum = sum(matchsticks)
        if circum & 3:
            return False

        def solve(idx, x, included):
            if (x, included) in dp:
                return dp[(x, included)]

            if x == 0:
                if included == ((1 << n) - 1):
                    return True
                return solve(0, edge, included)

            if x < 0 or idx == n:
                return False

            for i in range(idx, n):
                if (1 << i) & included == 0:
                    if solve(i + 1, x - matchsticks[i], included ^ (1 << i)):
                        dp[(x, included)] = True
                        return True

            dp[(x, included)] = False
            return False

        dp = {}
        edge = circum >> 2
        return solve(0, edge, 0)


# leetcode submit region end(Prohibit modification and deletion)


_cases = [
    TestCase(args=([1, 1, 2, 2, 2],), expected=True),
    TestCase(args=([3, 3, 3, 3, 4],), expected=False),
    TestCase(
        args=(
            [
                7215807,
                6967211,
                5551998,
                6632092,
                2802439,
                821366,
                2465584,
                9415257,
                8663937,
                3976802,
                2850841,
                803069,
                2294462,
                8242205,
                9922998,
            ],
        ),
        expected=False,
    ),
    TestCase(
        args=([4, 13, 1, 1, 14, 15, 1, 3, 13, 1, 3, 5, 2, 8, 12],), expected=False
    ),
]


@pytest.mark.parametrize("case", _cases)
def test_solution(case):
    sol = Solution()
    output = sol.makesquare(*case.args)
    assert output == case.expected
