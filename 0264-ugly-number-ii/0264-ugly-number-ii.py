class Solution:
    def nthUglyNumber(self, n: int) -> int:
        ugly = [1] * n
        i2 = i3 = i5 = 0

        for i in range(1, n):
            a = ugly[i2] * 2
            b = ugly[i3] * 3
            c = ugly[i5] * 5
            ugly[i] = min(a, b, c)

            if ugly[i] == a:
                i2 += 1
            if ugly[i] == b:
                i3 += 1
            if ugly[i] == c:
                i5 += 1

        return ugly[-1]