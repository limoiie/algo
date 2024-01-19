from algo import *


# noinspection PyPep8Naming,PyMethodMayBeStatic
# leetcode submit region begin(Prohibit modification and deletion)
class MyCalendarTwo:
    def __init__(self):
        self.s = []
        self.e = []

    def book(self, start: int, end: int) -> bool:
        max_occurrence = 1

        i = bisect.bisect_right(self.s, start)
        j = bisect.bisect_right(self.e, start)

        if i - j > max_occurrence:
            return False

        while i < len(self.s) and self.s[i] < end:
            while j < len(self.e) and self.e[j] <= self.s[i]:
                j += 1
            i += 1
            if i - j > max_occurrence:
                return False

        bisect.insort(self.s, start)
        bisect.insort(self.e, end)
        return True


# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(start,end)
# leetcode submit region end(Prohibit modification and deletion)


class SlowMyCalendarTwo:
    def __init__(self):
        self.once = []
        self.twice = []

    def book(self, start: int, end: int) -> bool:
        l2 = bisect.bisect_right(self.twice, start)
        r2 = bisect.bisect_left(self.twice, end)
        if l2 != r2 or l2 % 2 == 1:
            return False

        l1 = bisect.bisect_right(self.once, start)
        r1 = bisect.bisect_left(self.once, end)
        if l1 == r1:
            if l1 % 2 == 0:
                self.once[l1:l1] = [start, end]
            else:
                self.once[l1:l1] = [start, end]
                self.twice[l2:l2] = [start, end]
        else:
            l2_point = [start] if l1 % 2 == 1 else []
            r2_point = [end] if r1 % 2 == 1 else []
            self.twice[l2:l2] = l2_point + self.once[l1:r1] + r2_point
            self.once[l1:r1] = [start] + self.once[l1:r1] + [end]

            i = len(self.once) - 2
            while i >= 0:
                if self.once[i] == self.once[i + 1]:
                    self.once.pop(i)
                    self.once.pop(i)
                    i -= 2
                else:
                    i -= 1
        return True


class Test:
    def test_solution1(self):
        calender = MyCalendarTwo()
        assert calender.book(10, 20) is True
        assert calender.book(50, 60) is True
        assert calender.book(10, 40) is True
        assert calender.book(5, 15) is False
        assert calender.book(5, 10) is True
        assert calender.book(25, 55) is True

    def test_solution2(self):
        calender = MyCalendarTwo()
        assert calender.book(26, 35) is True
        assert calender.book(26, 32) is True
        assert calender.book(25, 32) is False
        assert calender.book(18, 26) is True
        assert calender.book(40, 45) is True
        assert calender.book(19, 26) is True
        assert calender.book(48, 50) is True
        assert calender.book(1, 6) is True
        assert calender.book(46, 50) is True
        assert calender.book(11, 18) is True

    def test_solution3(self):
        calendar = MyCalendarTwo()
        assert calendar.book(36, 41) is True
        assert calendar.book(28, 34) is True
        assert calendar.book(40, 46) is True
        assert calendar.book(10, 18) is True
        assert calendar.book(4, 11) is True
        assert calendar.book(25, 34) is True
        assert calendar.book(36, 44) is False
        assert calendar.book(32, 40) is False
        assert calendar.book(34, 39) is True
        assert calendar.book(40, 49) is False
