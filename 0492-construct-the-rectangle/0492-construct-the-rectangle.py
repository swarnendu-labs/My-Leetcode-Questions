import math

class Solution:
    def constructRectangle(self, area: int):
        w = int(math.isqrt(area))
        while area % w:
            w -= 1
        return [area // w, w]