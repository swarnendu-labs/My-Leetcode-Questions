class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()

        while n != 1 and n not in seen:
            seen.add(n)
            s = 0
            while n:
                d = n % 10
                s += d * d
                n //= 10
            n = s

        return n == 1