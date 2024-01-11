from algo import *


# noinspection PyPep8Naming,PyMethodMayBeStatic
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    # noinspection PyMethodMayBeStatic
    def findDuplicate(self, nums: List[int]) -> int:
        slow, fast = nums[0], nums[0]
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        slow = nums[0]
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        return slow


# leetcode submit region end(Prohibit modification and deletion)


_cases = [
    TestCase(args=([1, 3, 4, 2, 2],), expected=2),
    TestCase(args=([3, 1, 3, 4, 2],), expected=3),
]


@pytest.mark.parametrize("case", _cases)
def test_solution(case):
    sol = Solution()
    output = sol.findDuplicate(*case.args)
    assert output == case.expected
