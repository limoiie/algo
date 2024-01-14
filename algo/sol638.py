import math

from algo import *


# noinspection PyPep8Naming,PyMethodMayBeStatic
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def shoppingOffers(
        self, price: List[int], special: List[List[int]], needs: List[int]
    ) -> int:
        n = len(price)

        def compute_discount(offer):
            return offer[-1] - sum(price[i] * offer[i] for i in range(n))

        special.sort(key=compute_discount)

        def backtrace(i, acc, bought):
            nonlocal min_cost
            if acc >= min_cost:
                return

            if bought == needs:
                min_cost = min(min_cost, acc)
                return

            if i == len(special):
                remain_cost = sum(price[i] * (needs[i] - bought[i]) for i in range(n))
                min_cost = min(min_cost, acc + remain_cost)
                return

            def compute_count(offer_x):
                x, offer = offer_x
                if special[i][x] > 0:
                    return (needs[x] - bought[x]) // special[i][x]
                return math.inf

            max_cnt = min(map(compute_count, enumerate(needs)))
            for c in range(max_cnt, -1, -1):
                backtrace(
                    i + 1,
                    acc + c * special[i][-1],
                    [bought[k] + c * special[i][k] for k in range(n)],
                )

        min_cost = math.inf
        backtrace(0, 0, [0] * n)
        return min_cost


# leetcode submit region end(Prohibit modification and deletion)


_cases = [
    TestCase(args=([2, 5], [[3, 0, 5], [1, 2, 10]], [3, 2]), expected=14),
]


@pytest.mark.parametrize("case", _cases)
def test_solution(case):
    sol = Solution()
    output = sol.shoppingOffers(*case.args)
    assert output == case.expected
