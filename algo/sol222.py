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
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        left = root
        leftmost, h = 0, 0
        while True:
            if left.left is None and left.right is None:
                leftmost = 1 << h
                break
            left = left.left
            h += 1

        def check(val):
            cur = TreeNode(right=root)
            for i in range(h + 1)[::-1]:
                cur = cur.right if (val >> i) & 1 else cur.left
                if cur is None:
                    return False
            return True

        l, r = leftmost, leftmost << 1
        while l < r:
            mid = (l + r) >> 1
            if check(mid):
                if l == mid:
                    break
                l = mid
            else:
                r = mid
        return l


# leetcode submit region end(Prohibit modification and deletion)


_cases = [
    TestCase(args=(mt([1]),), expected=1),
    TestCase(args=(mt([1, 2, 3, 4, 5]),), expected=5),
    TestCase(args=(mt([1, 2, 3, 4, 5, 6]),), expected=6),
    TestCase(args=(mt([4, 4, 4, 4, 4, 4]),), expected=6),
]


@pytest.mark.parametrize("case", _cases)
def test_solution(case):
    sol = Solution()
    output = sol.countNodes(*case.args)
    assert output == case.expected
