from heapq import heappush, heappop

class DualHeap:
    def __init__(self, k):
        self.small = []
        self.large = []
        self.delayed = {}
        self.small_size = 0
        self.large_size = 0
        self.k = k

    def prune(self, heap):
        while heap:
            num = -heap[0] if heap is self.small else heap[0]
            if num in self.delayed:
                self.delayed[num] -= 1
                if self.delayed[num] == 0:
                    del self.delayed[num]
                heappop(heap)
            else:
                break

    def balance(self):
        if self.small_size > self.large_size + 1:
            heappush(self.large, -heappop(self.small))
            self.small_size -= 1
            self.large_size += 1
            self.prune(self.small)
        elif self.small_size < self.large_size:
            heappush(self.small, -heappop(self.large))
            self.small_size += 1
            self.large_size -= 1
            self.prune(self.large)

    def insert(self, num):
        if not self.small or num <= -self.small[0]:
            heappush(self.small, -num)
            self.small_size += 1
        else:
            heappush(self.large, num)
            self.large_size += 1
        self.balance()

    def erase(self, num):
        self.delayed[num] = self.delayed.get(num, 0) + 1
        if num <= -self.small[0]:
            self.small_size -= 1
            if num == -self.small[0]:
                self.prune(self.small)
        else:
            self.large_size -= 1
            if self.large and num == self.large[0]:
                self.prune(self.large)
        self.balance()

    def median(self):
        if self.k & 1:
            return float(-self.small[0])
        return (-self.small[0] + self.large[0]) / 2.0


class Solution:
    def medianSlidingWindow(self, nums, k):
        dh = DualHeap(k)
        for i in range(k):
            dh.insert(nums[i])
        ans = [dh.median()]
        for i in range(k, len(nums)):
            dh.insert(nums[i])
            dh.erase(nums[i - k])
            ans.append(dh.median())
        return ans