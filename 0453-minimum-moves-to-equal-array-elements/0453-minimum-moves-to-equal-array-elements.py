class Solution:
    def minMoves(self, nums: List[int]) -> int:
        m = min(nums)
        return sum(x - m for x in nums)