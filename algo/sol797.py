from algo import *


# noinspection PyPep8Naming,PyMethodMayBeStatic
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        n = len(graph)

        def backtrace(i, path):
            if i == n - 1:
                ans.append(path[:])
                return

            for j in graph[i]:
                if not visited[j]:
                    visited[j] = True
                    path.append(j)
                    backtrace(j, path)
                    path.pop()
                    visited[j] = False

        ans = []
        visited = [False] * n
        visited[0] = True
        backtrace(0, [0])
        return ans


# leetcode submit region end(Prohibit modification and deletion)


_cases = [
    TestCase(args=([[1, 2], [3], [3], [1]],), expected=[[0, 1, 3], [0, 2, 3]]),
]


@pytest.mark.parametrize("case", _cases)
def test_solution(case):
    sol = Solution()
    output = sol.allPathsSourceTarget(*case.args)
    assert output == case.expected
