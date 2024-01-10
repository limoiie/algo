from algo import *


# noinspection PyPep8Naming,PyMethodMayBeStatic
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        if n < 2:
            return

        def scatter(x):
            return (1 + (x << 1)) % (n | 1)

        def swap_by_virtual_index(ai, aj):
            vi, vj = scatter(ai), scatter(aj)
            nums[vi], nums[vj] = nums[vj], nums[vi]

        median = quick_select(nums, 0, n - 1, (n + 1) >> 1)

        i, j, k = 0, 0, n - 1
        while j <= k:
            if nums[scatter(j)] > median:
                swap_by_virtual_index(i, j)
                i += 1
                j += 1
            elif nums[scatter(j)] < median:
                swap_by_virtual_index(k, j)
                k -= 1
            else:
                j += 1


def quick_select(nums, l, r, k):
    pivot = nums[r]
    i, j = l, l
    while j < r:
        if nums[j] <= pivot:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
        j += 1
    nums[i], nums[j] = nums[j], nums[i]

    if i - l + 1 == k:
        return nums[i]

    if i - l + 1 > k:
        return quick_select(nums, l, i - 1, k)
    return quick_select(nums, i + 1, r, k - i + l - 1)


# leetcode submit region end(Prohibit modification and deletion)


_cases = [
    TestCase(args=([4, 5, 5, 6],), expected=...),
    # TestCase(args=([1, 4, 3, 4, 1, 2, 1, 3, 1, 3, 2, 3, 3],), expected=...),
    # TestCase(args=([1, 5, 1, 1, 6, 4],), expected=...),
    # TestCase(args=([1, 3, 2, 2, 3, 1],), expected=...),
    # TestCase(args=([1],), expected=...),
]


def is_wiggle(nums):
    print(nums)
    prev = 1000_000_000
    for i, num in enumerate(nums):
        if prev == num:
            return False
        if (prev < num) != (i & 1):
            return False
        prev = num
    return True


@pytest.mark.parametrize("case", _cases)
def test_solution(case):
    sol = Solution()
    sol.wiggleSort(*case.args)
    assert is_wiggle(case.args[0])
