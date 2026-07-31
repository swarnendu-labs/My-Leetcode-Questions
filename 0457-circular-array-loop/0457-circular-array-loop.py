class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        n = len(nums)

        def nxt(i):
            return (i + nums[i]) % n

        for i in range(n):
            if nums[i] == 0:
                continue
            slow = fast = i
            d = nums[i] > 0
            while True:
                if (nums[slow] > 0) != d:
                    break
                ns = nxt(slow)
                if (nums[fast] > 0) != d:
                    break
                nf = nxt(fast)
                if (nums[nf] > 0) != d:
                    break
                fast = nxt(nf)
                slow = ns
                if slow == fast:
                    if slow == nxt(slow):
                        break
                    return True
            j = i
            while nums[j] != 0 and (nums[j] > 0) == d:
                nj = nxt(j)
                nums[j] = 0
                j = nj
        return False