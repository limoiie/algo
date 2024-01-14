from algo import *


# noinspection PyPep8Naming,PyMethodMayBeStatic
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        return backtrace(candidates, 0, [], target)


def backtrace(candidates, starting, path, target):
    if target == 0:
        return [list(path)]

    ans = []
    for i in range(starting, len(candidates)):
        if i != starting and candidates[i] == candidates[i - 1]:
            continue
        cand = candidates[i]
        if cand <= target:
            path.append(cand)
            ans += backtrace(candidates, i + 1, path, target - cand)
            path.pop()
    return ans


# leetcode submit region end(Prohibit modification and deletion)


_cases = [
    TestCase(
        args=([10, 1, 2, 7, 6, 1, 5], 8),
        expected=[[1, 1, 6], [1, 2, 5], [1, 7], [2, 6]],
    ),
]


@pytest.mark.parametrize("case", _cases)
def test_solution(case):
    sol = Solution()
    output = sol.combinationSum2(*case.args)
    assert output == case.expected
