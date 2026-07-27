class Solution:
    def splitArray(self, nums, k):
        def check(limit):
            cnt = 1
            cur = 0
            for x in nums:
                if cur + x <= limit:
                    cur += x
                else:
                    cnt += 1
                    cur = x
            return cnt <= k

        left, right = max(nums), sum(nums)
        while left < right:
            mid = (left + right) // 2
            if check(mid):
                right = mid
            else:
                left = mid + 1
        return left