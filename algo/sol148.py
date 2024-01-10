from algo import *


# noinspection PyPep8Naming,PyMethodMayBeStatic
# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head

        p, p2 = head, head.next
        while p2 is not None:
            if p2.next is None:
                break
            p = p.next
            p2 = p2.next.next

        mid_head = p.next
        p.next = None
        return merge(self.sortList(head), self.sortList(mid_head))


def merge(left: Optional[ListNode], right: Optional[ListNode]):
    if not left or not right:
        return left or right

    root = curr = ListNode()
    while left and right:
        if left.val < right.val:
            curr.next = left
            left = left.next
        else:
            curr.next = right
            right = right.next
        curr = curr.next
    if left:
        curr.next = left
    if right:
        curr.next = right
    return root.next


# leetcode submit region end(Prohibit modification and deletion)


_cases = [
    TestCase(args=(ml([2, 1, 3]),), expected=ml([1, 2, 3])),
    TestCase(args=(ml([4, 2, 1, 3]),), expected=ml([1, 2, 3, 4])),
]


@pytest.mark.parametrize("case", _cases)
def test_solution(case):
    sol = Solution()
    output = sol.sortList(*case.args)
    assert output == case.expected
