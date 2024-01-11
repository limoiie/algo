from algo import *


# noinspection PyPep8Naming,PyMethodMayBeStatic
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        prefixes = [0]
        for num in nums:
            prefixes.append(prefixes[-1] + num)

        def sort(l, r):
            if l + 1 >= r:
                return 0

            i = j = m = (l + r) >> 1
            count = sort(l, m) + sort(m, r)
            for prefix in prefixes[l:m]:
                while i < r and prefixes[i] - prefix < lower:
                    i += 1
                while j < r and prefixes[j] - prefix <= upper:
                    j += 1
                count += j - i
            prefixes[l:r] = sorted(prefixes[l:r])
            return count

        return sort(l=0, r=len(prefixes))


# leetcode submit region end(Prohibit modification and deletion)


_cases = [
    TestCase(args=(...,), expected=...),
]


@pytest.mark.parametrize("case", _cases)
def test_solution(case):
    sol = Solution()
    output = sol.countRangeSum(*case.args)
    assert output == case.expected
