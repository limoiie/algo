from . import *
from math import *


# noinspection PyPep8Naming,PyMethodMayBeStatic
# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        root, size = self.list_to_vine(head)
        self.vine_to_tree(root, size)
        return root.right

    def list_to_vine(self, head):
        size = 0
        curr = root = TreeNode()
        while head:
            curr.right = TreeNode(head.val)
            curr = curr.right
            head = head.next
            size += 1
        return root, size

    def vine_to_tree(self, root, size):
        leaves = size + 1 - (1 << int(log2(size + 1)))
        self.compress(root, leaves)
        size -= leaves
        while size > 1:
            size //= 2
            self.compress(root, size)

    def compress(self, root, cnt):
        curr = root
        for _ in range(cnt):
            child = curr.right
            curr.right = child.right
            curr = curr.right

            child.right = curr.left
            curr.left = child


# leetcode submit region end(Prohibit modification and deletion)


_cases = [
    TestCase(args=(...,), expected=...),
]


@pytest.mark.parametrize("case", _cases)
def test_solution(case):
    sol = Solution()
    output = sol.sortedListToBST(*case.args)
    assert output == case.expected
