from algo import *


# noinspection PyPep8Naming,PyMethodMayBeStatic
# leetcode submit region begin(Prohibit modification and deletion)
class MyCalendar:
    def __init__(self):
        self.ranges = []

    def book(self, start: int, end: int) -> bool:
        end -= 1
        l = bisect.bisect_left(self.ranges, start)
        r = bisect.bisect_right(self.ranges, end)
        if l != r or l % 2 == 1:
            return False
        self.ranges[l:l] = [start, end]
        return True


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)
# leetcode submit region end(Prohibit modification and deletion)


def test_solution():
    calender = MyCalendar()
    assert calender.book(10, 20) is True
    assert calender.book(15, 25) is False
    assert calender.book(20, 30) is True
