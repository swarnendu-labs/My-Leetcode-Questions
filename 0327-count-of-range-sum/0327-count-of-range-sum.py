class Solution:
    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        prefix = [0]
        for x in nums:
            prefix.append(prefix[-1] + x)

        def sort(lo, hi):
            if hi - lo <= 1:
                return 0
            mid = (lo + hi) // 2
            count = sort(lo, mid) + sort(mid, hi)
            j = k = mid
            temp = []
            r = mid
            for left in prefix[lo:mid]:
                while k < hi and prefix[k] - left < lower:
                    k += 1
                while j < hi and prefix[j] - left <= upper:
                    j += 1
                count += j - k
            l, r = lo, mid
            while l < mid and r < hi:
                if prefix[l] <= prefix[r]:
                    temp.append(prefix[l])
                    l += 1
                else:
                    temp.append(prefix[r])
                    r += 1
            temp.extend(prefix[l:mid])
            temp.extend(prefix[r:hi])
            prefix[lo:hi] = temp
            return count

        return sort(0, len(prefix))