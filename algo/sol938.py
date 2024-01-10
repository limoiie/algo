from . import *


# noinspection PyPep8Naming,PyMethodMayBeStatic
# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        return self.dfs(root, low, high)

    def dfs(self, root: Optional[TreeNode], low: int, high: int):
        if root is None:
            return 0
        if root.val > high:
            return self.dfs(root.left, low, high)
        if root.val < low:
            return self.dfs(root.right, low, high)
        return (
            root.val
            + self.dfs(root.left, low, root.val)
            + self.dfs(root.right, root.val, high)
        )


# leetcode submit region end(Prohibit modification and deletion)


_cases = [
    TestCase(args=(...,), expected=...),
]


@pytest.mark.parametrize("case", _cases)
def test_solution(case):
    sol = Solution()
    output = sol.rangeSumBST(*case.args)
    assert output == case.expected
