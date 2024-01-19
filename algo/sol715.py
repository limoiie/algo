from algo import *


# noinspection PyPep8Naming,PyMethodMayBeStatic
# leetcode submit region begin(Prohibit modification and deletion)
class RangeModule:
    def __init__(self):
        self.ranges = []

    def addRange(self, left: int, right: int) -> None:
        bl = bisect.bisect_left(self.ranges, left)
        br = bisect.bisect_right(self.ranges, right)
        lr = self.ranges[:bl] if bl % 2 else (self.ranges[:bl] + [left])
        rr = self.ranges[br:] if br % 2 else ([right] + self.ranges[br:])
        self.ranges = lr + rr

    def queryRange(self, left: int, right: int) -> bool:
        bl = bisect.bisect_right(self.ranges, left)
        br = bisect.bisect_left(self.ranges, right)
        return bl == br and bl % 2 == 1

    def removeRange(self, left: int, right: int) -> None:
        bl = bisect.bisect_left(self.ranges, left)
        br = bisect.bisect_right(self.ranges, right)
        lr = (self.ranges[:bl] + [left]) if bl % 2 else self.ranges[:bl]
        rr = ([right] + self.ranges[br:]) if br % 2 else self.ranges[br:]
        self.ranges = lr + rr


# Your RangeModule object will be instantiated and called as such:
# obj = RangeModule()
# obj.addRange(left,right)
# param_2 = obj.queryRange(left,right)
# obj.removeRange(left,right)
# leetcode submit region end(Prohibit modification and deletion)
