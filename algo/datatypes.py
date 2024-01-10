from collections import deque
from typing import List, Optional

__all__ = ["TreeNode", "mt", "ListNode", "ml", "null"]


null = None


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class ListNode:
    def __init__(self, val=0, next_=None):
        self.val = val
        self.next = next_

    def __repr__(self):
        if self.next:
            return f"{self.val}, {repr(self.next)}"
        return f"{self.val}"

    def __eq__(self, other):
        return (
            other is not None
            and isinstance(other, ListNode)
            and self.val == other.val
            and self.next == other.next
        )


def ml(nums: List[int]) -> Optional[ListNode]:
    curr = root = ListNode()
    for num in nums:
        curr.next = ListNode(num)
        curr = curr.next
    return root.next


def mt(nodes: List[Optional[int]]) -> Optional[TreeNode]:
    n = len(nodes)
    if n == 0:
        return None

    root = mn(nodes[0])

    i = 1
    layer = deque([root])

    while layer:
        if i >= n:
            break

        node = layer.popleft()

        left_child = mn(nodes[i])
        right_child = mn(nodes[i + 1])

        if node:
            node.left = left_child
            node.right = right_child

        layer.append(left_child)
        layer.append(right_child)

        i += 2

    return root


def mn(val):
    return val if val is None else TreeNode(val)
