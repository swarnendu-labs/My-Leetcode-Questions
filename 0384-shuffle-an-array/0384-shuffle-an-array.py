from typing import List
import random

class Solution:

    def __init__(self, nums: List[int]):
        self.original = nums[:]

    def reset(self) -> List[int]:
        return self.original[:]

    def shuffle(self) -> List[int]:
        arr = self.original[:]
        n = len(arr)
        for i in range(n):
            j = random.randrange(i, n)
            arr[i], arr[j] = arr[j], arr[i]
        return arr
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()