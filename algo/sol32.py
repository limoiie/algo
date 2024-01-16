from algo import *


# noinspection PyPep8Naming,PyMethodMayBeStatic
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        n = len(s)
        stack = []
        for i in range(n):
            if s[i] == "(":
                stack.append(i)
            elif stack and s[stack[-1]] == "(":
                stack.pop()
            else:
                stack.append(i)

        if not stack:
            return n

        ans = 0
        prev = n
        while stack:
            curr = stack.pop()
            ans = max(ans, prev - curr - 1)
            prev = curr
        return max(ans, prev)


# leetcode submit region end(Prohibit modification and deletion)


def dp_but_tol(s: str):
    n = len(s)
    dp = [[None] * n for _ in range(n)]

    ans = 0
    for i in range(n):
        dp[i][i - 1] = True
        for j in range(i - 1, -1, -2):
            if s[j] == "(" and s[i] == ")":
                for k in range(j, i, 2):
                    if dp[j + 1][k] and dp[k + 1][i - 1]:
                        ans = max(ans, i - j + 1)
                        dp[j][i] = True
                        break

            if not dp[j][i]:
                for k in range(j + 1, i - 1, 2):
                    if dp[j][k] and dp[k + 1][i]:
                        ans = max(ans, i - j + 1)
                        dp[j][i] = True
                        break
    return ans


_cases = [
    TestCase(args=(")()())",), expected=4),
    TestCase(args=("(()",), expected=2),
    TestCase(
        args=(
            "())()()(())((()(()()(((()))((((())((()(())()())(()((((()))()(()))(())()(())(()(((((())((((((()())())(()(()((())()))(()))))))()(()))((((())()()()))()()()(((()(()())(()()(()(()()(((()))))))()()))())())((()()))))))((()))(((()((())()(()()))((())))()()())))))))()))))(()))))()))()))()((())))((()))(()))))))(((()))))))))()(()()()(())((())()))()()(())))()()))(()())()))(((()())()))((())((((()))(()(()(()()()(((())()(((((()))((()(((((())(()()))((((((((()(()(()(()(())))(())(()())())(()((((()(())((()(())))(())))()(((((()(()()(())))))))())(())(())(()()(((())))((()))(((((()))))())))()((()))()))))())))))((())(((((()()))((((())))(((()(()(())())(((()(()(()()()())))())()))((()((())())()()()(((())(((((()((((((()((()())))((((())((()(((((((()(()((()()()(()(()())(()(()()((((())))()(((()())))(()()))()(()()()()(((((())(()))))((()))())))()((((((()))())))()(()))(())))((((()())(((((()()())(((((())(()())(()))))()(()()))()))))))())))(((())(()(()()))(()))()(((())))())((((()(((()))))))()(()(()))()()(()()))))))))((()))))))(())((()((()))()))((((((()())))))(()((())((((()))))(()(()()()()(()))()()(()(()))(()()(((((((()())(())(()())((())())()(()())((())()())())(()())))())))(())())())(())((()())(((()()))()))()()))()(()(())((((((((())))()((())((()((((((((((()))))(()(((((())(()(()())())))((())())))))()))(()((()()))((()((())()()()((()(())())((())())(()()(((())))))())()()(()))()())(()(()((())))((((()()(())))())(())(()(()(())())())(()()())()(())())))(()()(((())))((()()(((())()()(()())((((()()(()())(()((((()(()()(()(()(((()((()())(()()))(()((((()(((((()))))()()))(((()((((((()(()()()()())()))(()(())))))((()(((()())())))(((()()))(()(()(((((((()()))(()(())))())()(())())(())(()))(())(()))()()(()()())))))()))()((())(((()((((((((())()()))())))((()())(",
        ),
        expected=310,
    ),
]


@pytest.mark.parametrize("case", _cases)
def test_solution(case):
    sol = Solution()
    output = sol.longestValidParentheses(*case.args)
    assert output == case.expected