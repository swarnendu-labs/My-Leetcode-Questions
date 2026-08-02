from bisect import bisect_left

class Solution:
    def findRadius(self, houses, heaters):
        heaters.sort()
        ans = 0

        for house in houses:
            i = bisect_left(heaters, house)
            left = house - heaters[i - 1] if i > 0 else float("inf")
            right = heaters[i] - house if i < len(heaters) else float("inf")
            ans = max(ans, min(left, right))

        return ans