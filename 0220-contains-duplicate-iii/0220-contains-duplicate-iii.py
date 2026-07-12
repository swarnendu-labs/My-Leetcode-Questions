class Solution:
    def containsNearbyAlmostDuplicate(self, nums, indexDiff, valueDiff):
        if valueDiff < 0:
            return False

        buckets = {}
        w = valueDiff + 1

        for i, x in enumerate(nums):
            b = x // w

            if b in buckets:
                return True
            if b - 1 in buckets and abs(x - buckets[b - 1]) <= valueDiff:
                return True
            if b + 1 in buckets and abs(x - buckets[b + 1]) <= valueDiff:
                return True

            buckets[b] = x

            if i >= indexDiff:
                del buckets[nums[i - indexDiff] // w]

        return False