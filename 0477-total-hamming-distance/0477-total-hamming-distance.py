class Solution:
    def totalHammingDistance(self, nums):
        n = len(nums)
        ans = 0
        for b in range(30):
            ones = sum((x >> b) & 1 for x in nums)
            ans += ones * (n - ones)
        return ans