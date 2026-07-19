class NumArray:

    def __init__(self, nums: List[int]):
        self.n = len(nums)
        self.bit = [0] * (self.n + 1)
        self.nums = nums[:]
        for i, v in enumerate(nums):
            self._add(i + 1, v)

    def _add(self, i, delta):
        while i <= self.n:
            self.bit[i] += delta
            i += i & -i

    def _sum(self, i):
        s = 0
        while i:
            s += self.bit[i]
            i -= i & -i
        return s

    def update(self, index: int, val: int) -> None:
        self._add(index + 1, val - self.nums[index])
        self.nums[index] = val

    def sumRange(self, left: int, right: int) -> int:
        return self._sum(right + 1) - self._sum(left)
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)