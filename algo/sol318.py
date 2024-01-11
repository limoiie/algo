from algo import *


# noinspection PyPep8Naming,PyMethodMayBeStatic
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def maxProduct(self, words: List[str]) -> int:
        sets = []
        for word in words:
            sets.append(set(word))

        ans = 0
        for i in range(len(words)):
            for j in range(i + 1, len(words)):
                if not sets[i].intersection(sets[j]):
                    ans = max(ans, len(words[i]) * len(words[j]))
        return ans


# leetcode submit region end(Prohibit modification and deletion)


_cases = [
    TestCase(args=(["abcw", "baz", "foo", "bar", "xtfn", "abcdef"],), expected=16),
]


@pytest.mark.parametrize("case", _cases)
def test_solution(case):
    sol = Solution()
    output = sol.maxProduct(*case.args)
    assert output == case.expected
