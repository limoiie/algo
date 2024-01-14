from algo import *


# noinspection PyPep8Naming,PyMethodMayBeStatic
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        return backtrace(num, 0, (), 0)


def backtrace(num, starting, prev_two, k):
    if starting >= len(num):
        return k > 2

    for j in range(starting + 1, len(num) + 1):
        if num[starting] == "0" and j > starting + 1:
            break

        part_num_int = int(num[starting:j])

        if len(prev_two) == 0:
            new_prev_two = (part_num_int,)

        elif len(prev_two) == 1:
            new_prev_two = (prev_two[-1], part_num_int)

        else:
            if prev_two[-1] + prev_two[-2] > part_num_int:
                continue
            if prev_two[-1] + prev_two[-2] < part_num_int:
                return False

            new_prev_two = (prev_two[-1], prev_two[-1] + prev_two[-2])

        if backtrace(num, j, new_prev_two, k + 1):
            return True

    return False


# leetcode submit region end(Prohibit modification and deletion)


_cases = [
    TestCase(args=("199100199",), expected=True),
    TestCase(args=("112358",), expected=True),
    TestCase(args=("111",), expected=False),
]


@pytest.mark.parametrize("case", _cases)
def test_solution(case):
    sol = Solution()
    output = sol.isAdditiveNumber(*case.args)
    assert output == case.expected
