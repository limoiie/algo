from algo import *


# noinspection PyPep8Naming,PyMethodMayBeStatic
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def validUtf8(self, data: List[int]) -> bool:
        pm = [
            0b0000_0000,
            0b1000_0000,
            0b1100_0000,
            0b1110_0000,
            0b1111_0000,
            0b1111_1000,
        ]

        i, n = 0, len(data)
        while i < n:
            b = data[i]
            if b & pm[1] == pm[0]:
                i += 1
            else:
                i += 1
                for m in range(2, 5):
                    if b & pm[m + 1] == pm[m]:
                        for _ in range(m - 1):
                            if i >= n or data[i] & pm[2] != pm[1]:
                                return False
                            i += 1
                        break
                else:
                    return False
        return True


# leetcode submit region end(Prohibit modification and deletion)


_cases = [
    TestCase(args=([255],), expected=False),
    TestCase(args=([197, 130, 1],), expected=True),
    TestCase(args=([235, 140, 4],), expected=False),
]


@pytest.mark.parametrize("case", _cases)
def test_solution(case):
    sol = Solution()
    output = sol.validUtf8(*case.args)
    assert output == case.expected
