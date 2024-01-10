from algo import *


# noinspection PyPep8Naming,PyMethodMayBeStatic
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def smallestTrimmedNumbers(
        self, nums: List[str], queries: List[List[int]]
    ) -> List[int]:
        n_digits = len(nums[0])

        # index queries and numbers
        radix_queries = [[] for _ in range(n_digits)]
        for i, (k, trim) in enumerate(queries):
            radix_queries[trim - 1].append((i, k))
        indexed_nums = list(enumerate(nums))

        ans = [0] * len(queries)
        for trim in range(1, n_digits + 1):
            radix = [[] for _ in range(11)]
            # sort by radix
            for i, num in indexed_nums:
                radix[ord(num[-trim]) - ord("0")].append((i, num))
            indexed_nums = [p for box in radix for p in box]
            # query the k-th smallest under given trim
            for i, k in radix_queries[trim - 1]:
                ans[i] = indexed_nums[k - 1][0]
        return ans


# leetcode submit region end(Prohibit modification and deletion)


_cases = [
    TestCase(
        args=(["102", "473", "251", "814"], [[1, 1], [2, 3], [4, 2], [1, 2]]),
        expected=[2, 2, 1, 0],
    ),
    TestCase(args=(["24", "37", "96", "04"], [[2, 1], [2, 2]]), expected=[3, 0]),
]


@pytest.mark.parametrize("case", _cases)
def test_solution(case):
    sol = Solution()
    output = sol.smallestTrimmedNumbers(*case.args)
    assert output == case.expected
