from algo import *


# noinspection PyPep8Naming,PyMethodMayBeStatic
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        rep = 0
        bag = {"A": 0, "C": 1, "G": 2, "T": 3}

        ans = []
        mem = dict()
        for i, c in enumerate(s):
            rep = ((rep << 2) | bag[c]) & 0b111_111_1111_111_111_1111
            if i >= 9:
                if mem.setdefault(rep, 0) == 1:
                    ans.append(s[i - 9 : i + 1])
                mem[rep] += 1
        return ans


# leetcode submit region end(Prohibit modification and deletion)


_cases = [
    TestCase(
        args=("AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT",),
        expected=["AAAAACCCCC", "CCCCCAAAAA"],
    ),
]


@pytest.mark.parametrize("case", _cases)
def test_solution(case):
    sol = Solution()
    output = sol.findRepeatedDnaSequences(*case.args)
    assert output == case.expected
