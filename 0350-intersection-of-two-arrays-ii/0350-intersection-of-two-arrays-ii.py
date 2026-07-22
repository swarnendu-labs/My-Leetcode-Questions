from typing import List
from collections import Counter

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        count = Counter(nums1)
        ans = []

        for x in nums2:
            if count[x] > 0:
                ans.append(x)
                count[x] -= 1

        return ans