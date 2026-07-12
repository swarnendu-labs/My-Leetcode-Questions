class Solution:
    def findKthLargest(self, nums, k):
        offset = 10000
        cnt = [0] * 20001
        for x in nums:
            cnt[x + offset] += 1
        for i in range(20000, -1, -1):
            k -= cnt[i]
            if k <= 0:
                return i - offset