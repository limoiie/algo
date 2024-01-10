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
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        left_leaves, right_leaves = [], []
        self.leaves(root1, left_leaves)
        self.leaves(root2, right_leaves)
        print(left_leaves, right_leaves)
        return left_leaves == right_leaves

    def leaves(self, root: Optional[TreeNode], leafs: List[int]):
        if root is None:
            return
        if root.left is None and root.right is None:
            leafs.append(root.val)
            return
        self.leaves(root.left, leafs)
        self.leaves(root.right, leafs)


# leetcode submit region end(Prohibit modification and deletion)


_cases = [
    TestCase(
        args=(
            mt([3, 5, 1, 6, 2, 9, 8, null, null, 7, 4]),
            mt([3, 5, 1, 6, 7, 4, 2, null, null, null, null, null, null, 9, 8]),
        ),
        expected=True,
    ),
    TestCase(args=(mt([1, 2, 3]), mt([1, 3, 2])), expected=False),
]


@pytest.mark.parametrize("case", _cases)
def test_solution(case):
    sol = Solution()
    output = sol.leafSimilar(*case.args)
    assert output == case.expected
