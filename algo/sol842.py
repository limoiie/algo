from algo import *


# noinspection PyPep8Naming,PyMethodMayBeStatic
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def splitIntoFibonacci(self, num: str) -> List[int]:
        def backtrace(starting, path, prev_two, k):
            if starting >= len(num):
                if k >= 2:
                    return path
                return []

            for nj in range(starting + 1, len(num) + 1):
                if num[starting] == "0" and nj > starting + 1:
                    break

                next_num = int(num[starting:nj])
                if next_num > 2**31 - 1:
                    break

                if k == 0:
                    fib = backtrace(
                        nj, path + [next_num], (prev_two[-1], next_num), k + 1
                    )
                    if fib:
                        return fib

                elif prev_two[0] + prev_two[1] < next_num:
                    return []

                elif prev_two[0] + prev_two[1] == next_num:
                    fib = backtrace(
                        nj, path + [next_num], (prev_two[-1], next_num), k + 1
                    )
                    if fib:
                        return fib

        for i in range(1, len(num) - 1):
            if num[0] == "0" and i > 1:
                break
            first_num = int(num[:i])
            if first_num > 2**31 - 1:
                break

            fib = backtrace(i, [first_num], (first_num,), 0)
            if fib:
                return fib
        return []


# leetcode submit region end(Prohibit modification and deletion)


_cases = [
    TestCase(args=("0123",), expected=[]),
    TestCase(args=("123",), expected=[1, 2, 3]),
    TestCase(args=("122335",), expected=[12, 23, 35]),
    TestCase(args=("1101111",), expected=[11, 0, 11, 11]),
]


@pytest.mark.parametrize("case", _cases)
def test_solution(case):
    sol = Solution()
    output = sol.splitIntoFibonacci(*case.args)
    assert output == case.expected
