from algo import *


# noinspection PyPep8Naming,PyMethodMayBeStatic
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        return backtrace(candidates, 0, [], target)


def backtrace(candidates, starting, path, target):
    if target == 0:
        return [list(path)]

    ans = []
    for i in range(starting, len(candidates)):
        cand = candidates[i]
        cnt = 0
        while cand <= target:
            path.append(cand)
            ans += backtrace(candidates, i + 1, path, target - cand)
            target -= cand
            cnt += 1

        for _ in range(cnt):
            target += cand
            path.pop()
    return ans


# leetcode submit region end(Prohibit modification and deletion)


_cases = [
    TestCase(args=([2, 3, 5], 8), expected=[[2, 3, 3], [2, 2, 2, 2], [3, 5]]),
    TestCase(args=([2, 3, 6, 7], 7), expected=[[2, 2, 3], [7]]),
]


@pytest.mark.parametrize("case", _cases)
def test_solution(case):
    sol = Solution()
    output = sol.combinationSum(*case.args)
    assert output == case.expected
