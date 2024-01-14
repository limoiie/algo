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
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        dp = [[], [TreeNode(1)]]
        for i in range(2, n + 1):
            dp.append(list(generate_trees(dp, i)))
        return dp[n]


def copy_tree(root: Optional[TreeNode]):
    if root:
        return TreeNode(
            root.val,
            left=copy_tree(root.left),
            right=copy_tree(root.right),
        )
    return None


def insert_top(root: Optional[TreeNode], val: int):
    return TreeNode(val, left=root)


def insert_right(root: TreeNode, node: TreeNode, val: int):
    new = TreeNode(val, left=node.right)

    node.right = new
    yield copy_tree(root)
    node.right = new.left

    if node.right:
        yield from insert_right(root, node.right, val)


def generate_trees(dp, i):
    for root in dp[i - 1]:
        yield insert_top(root, i)
        yield from insert_right(root, root, i)


def fibonacci(n):
    return n * fibonacci(n - 1) if n > 1 else 1


# leetcode submit region end(Prohibit modification and deletion)


_cases = [
    TestCase(args=(...,), expected=...),
]


@pytest.mark.parametrize("case", _cases)
def test_solution(case):
    sol = Solution()
    output = sol.generateTrees(*case.args)
    assert output == case.expected
