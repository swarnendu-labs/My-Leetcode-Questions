class Solution:
    def smallestGoodBase(self, n: str) -> str:
        N = int(n)
        max_m = N.bit_length() - 1

        for m in range(max_m, 1, -1):
            k = int(N ** (1.0 / m))
            if k < 2:
                continue
            s = 1
            cur = 1
            for _ in range(m):
                cur *= k
                s += cur
            if s == N:
                return str(k)

        return str(N - 1)