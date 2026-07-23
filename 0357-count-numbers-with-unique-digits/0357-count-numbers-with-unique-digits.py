class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        if n == 0:
            return 1
        ans = 10
        cur = 9
        avail = 9
        for _ in range(2, min(n, 10) + 1):
            cur *= avail
            ans += cur
            avail -= 1
        return ans