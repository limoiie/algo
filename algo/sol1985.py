from algo import *


# noinspection PyPep8Naming,PyMethodMayBeStatic
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        q = []
        for num in nums:
            heapq.heappush(q, BigVal(num))
            if len(q) > k:
                heapq.heappop(q)
        return heapq.heappop(q).num


class BigVal:
    def __init__(self, num):
        self.num = num

    def __lt__(self, other):
        if len(self.num) != len(other.num):
            return len(self.num) < len(other.num)
        return self.num < other.num


# leetcode submit region end(Prohibit modification and deletion)


_cases = [
    TestCase(args=(["3", "6", "7", "10"], 4), expected="3"),
    TestCase(args=(["2", "21", "12", "1"], 3), expected="2"),
    TestCase(args=(["0", "0"], 2), expected="0"),
]


@pytest.mark.parametrize("case", _cases)
def test_solution(case):
    sol = Solution()
    output = sol.kthLargestNumber(*case.args)
    assert output == case.expected
