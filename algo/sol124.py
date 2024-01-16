from algo import *


# noinspection PyPep8Naming,PyMethodMayBeStatic
# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        ans = -math.inf

        def dfs(node: Optional[TreeNode]):
            left = dfs(node.left) if node.left else -math.inf
            right = dfs(node.right) if node.right else -math.inf

            nonlocal ans
            ans = max(
                ans,
                node.val + left + right,
                node.val + left,
                node.val + right,
                node.val,
            )

            return max(node.val, node.val + left, node.val + right)

        dfs(root)
        return ans


# leetcode submit region end(Prohibit modification and deletion)


_cases = [
    TestCase(args=(mt([-3]),), expected=-3),
    TestCase(args=(mt([1, 2, 3]),), expected=6),
    TestCase(args=(mt([-10, 9, 20, null, null, 15, 7]),), expected=42),
    TestCase(args=(mt([1, -2, -3, 1, 3, -2, null, -1]),), expected=3),
]


@pytest.mark.parametrize("case", _cases)
def test_solution(case):
    sol = Solution()
    output = sol.maxPathSum(*case.args)
    assert output == case.expected
