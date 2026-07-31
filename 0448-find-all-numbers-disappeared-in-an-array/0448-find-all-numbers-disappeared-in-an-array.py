class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        for x in nums:
            i = abs(x) - 1
            if nums[i] > 0:
                nums[i] = -nums[i]
        return [i + 1 for i, x in enumerate(nums) if x > 0]