import random
import bisect
from typing import List

class Solution:

    def __init__(self, rects: List[List[int]]):
        self.rects = rects
        self.prefix = []
        total = 0

        for x1, y1, x2, y2 in rects:
            total += (x2 - x1 + 1) * (y2 - y1 + 1)
            self.prefix.append(total)

    def pick(self) -> List[int]:
        k = random.randint(1, self.prefix[-1])
        idx = bisect.bisect_left(self.prefix, k)

        x1, y1, x2, y2 = self.rects[idx]
        x = random.randint(x1, x2)
        y = random.randint(y1, y2)

        return [x, y]


# Your Solution object will be instantiated and called as such:
# obj = Solution(rects)
# param_1 = obj.pick()