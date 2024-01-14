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
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        return list(backtrace(root, []))


def backtrace(node, path):
    if node is None:
        return

    path.append(str(node.val))
    if node.left is None and node.right is None:
        yield "->".join(path)
    else:
        yield from backtrace(node.left, path)
        yield from backtrace(node.right, path)
    path.pop()


# leetcode submit region end(Prohibit modification and deletion)


_cases = [
    TestCase(args=(mt([1, 2, 3, null, 5]),), expected=["1->2->5", "1->3"]),
]


@pytest.mark.parametrize("case", _cases)
def test_solution(case):
    sol = Solution()
    output = sol.binaryTreePaths(*case.args)
    assert output == case.expected
