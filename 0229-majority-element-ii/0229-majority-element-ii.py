class Solution:
    def majorityElement(self, nums):
        c1 = c2 = None
        v1 = v2 = 0

        for x in nums:
            if c1 == x:
                v1 += 1
            elif c2 == x:
                v2 += 1
            elif v1 == 0:
                c1 = x
                v1 = 1
            elif v2 == 0:
                c2 = x
                v2 = 1
            else:
                v1 -= 1
                v2 -= 1

        res = []
        if nums.count(c1) > len(nums) // 3:
            res.append(c1)
        if c2 != c1 and nums.count(c2) > len(nums) // 3:
            res.append(c2)

        return res