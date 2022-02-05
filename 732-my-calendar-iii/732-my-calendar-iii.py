import bisect
from sortedcontainers import SortedDict
class MyCalendarThree:

    def __init__(self):
        self.ans = []
        self.counter = SortedDict()

    def book(self, start: int, end: int) -> int:
        self.counter[start] = self.counter.get(start,0) + 1
        self.counter[end] = self.counter.get(end,0) - 1
        res = 0
        active = 0
        for k,v in self.counter.items():
            active += v
            if active > res:
                res = active
        return res


# Your MyCalendarThree object will be instantiated and called as such:
# obj = MyCalendarThree()
# param_1 = obj.book(start,end)