from algo import *


# noinspection PyPep8Naming,PyMethodMayBeStatic
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        return backtrace(digits, 0, []) if digits else []


def backtrace(digits, i, path):
    if i == len(digits):
        return ["".join(path)]

    acc = []
    for c in diction[digits[i]]:
        path.append(c)
        acc += backtrace(digits, i + 1, path)
        path.pop()
    return acc


diction = {
    "2": "abc",
    "3": "def",
    "4": "ghi",
    "5": "jkl",
    "6": "mno",
    "7": "pqrs",
    "8": "tuv",
    "9": "wxyz",
}


# leetcode submit region end(Prohibit modification and deletion)


_cases = [
    TestCase(args=(...,), expected=...),
]


@pytest.mark.parametrize("case", _cases)
def test_solution(case):
    sol = Solution()
    output = sol.letterCombinations(*case.args)
    assert output == case.expected
