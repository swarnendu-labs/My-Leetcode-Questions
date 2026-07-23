from bisect import bisect_left

class SummaryRanges:

    def __init__(self):
        self.intervals = []

    def addNum(self, value: int) -> None:
        a = self.intervals
        i = bisect_left(a, [value, value])

        if i > 0 and a[i - 1][1] >= value:
            return
        if i < len(a) and a[i][0] <= value <= a[i][1]:
            return

        left = i > 0 and a[i - 1][1] + 1 == value
        right = i < len(a) and a[i][0] - 1 == value

        if left and right:
            a[i - 1][1] = a[i][1]
            a.pop(i)
        elif left:
            a[i - 1][1] = value
        elif right:
            a[i][0] = value
        else:
            a.insert(i, [value, value])

    def getIntervals(self):
        return self.intervals
        


# Your SummaryRanges object will be instantiated and called as such:
# obj = SummaryRanges()
# obj.addNum(value)
# param_2 = obj.getIntervals()