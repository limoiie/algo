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
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        return list(backtrace(root, [], 0, targetSum))


def backtrace(node, path, acc, target):
    if node is None:
        return

    path.append(node.val)
    acc += node.val
    if acc == target:
        if node.left is None and node.right is None:
            yield path[:]

    yield from backtrace(node.left, path, acc, target)
    yield from backtrace(node.right, path, acc, target)
    path.pop()


# leetcode submit region end(Prohibit modification and deletion)


_cases = [
    TestCase(
        args=(mt([5, 4, 8, 11, null, 13, 4, 7, 2, null, null, 5, 1]), 22),
        expected=[[5, 4, 11, 2], [5, 8, 4, 5]],
    ),
    TestCase(
        args=(mt([1, 2]), 1),
        expected=[],
    ),
    TestCase(
        args=(mt([1, 2, 3]), 5),
        expected=[],
    ),
    TestCase(
        args=(mt([1, -2, -3, 1, 3, -2, null, -1]), -1),
        expected=[[1, -2, 1, -1]],
    ),
]


@pytest.mark.parametrize("case", _cases)
def test_solution(case):
    sol = Solution()
    output = sol.pathSum(*case.args)
    assert output == case.expected
