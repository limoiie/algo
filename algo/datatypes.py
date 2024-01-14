from collections import deque
from typing import List, Optional

__all__ = ["TreeNode", "mt", "ListNode", "ml", "null"]


null = None


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        if self.left is None and self.right is None:
            return f"({self.val})"
        return f"{self.val}[{repr(self.left)}][{repr(self.right)}]"


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
    if not nodes:
        return None

    nodes.reverse()

    def pop_val():
        return nodes.pop() if nodes else None

    root = mn(pop_val())
    layer = deque([root])

    while nodes:
        node = layer.popleft()

        node.left = mn(pop_val())
        if node.left:
            layer.append(node.left)

        node.right = mn(pop_val())
        if node.right:
            layer.append(node.right)

    return root


def mn(val):
    return val if val is None else TreeNode(val)
