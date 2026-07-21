class Solution:
    def maxActiveSectionsAfterTrade(self, s: str) -> int:
        t = "1" + s + "1"
        runs = []
        i = 0
        while i < len(t):
            j = i
            while j < len(t) and t[j] == t[i]:
                j += 1
            runs.append((t[i], j - i))
            i = j

        zero_lens = []
        zero_id = {}
        for idx, (c, l) in enumerate(runs):
            if c == "0":
                zero_id[idx] = len(zero_lens)
                zero_lens.append(l)

        m = len(zero_lens)
        pre = [0] * m
        suf = [0] * m

        for i in range(m):
            pre[i] = zero_lens[i] if i == 0 else max(pre[i - 1], zero_lens[i])

        for i in range(m - 1, -1, -1):
            suf[i] = zero_lens[i] if i == m - 1 else max(suf[i + 1], zero_lens[i])

        ones = s.count("1")
        ans = ones

        for idx, (c, a) in enumerate(runs):
            if c == "1" and 0 < idx < len(runs) - 1:
                zl = zero_id[idx - 1]
                zr = zero_id[idx + 1]
                merged = zero_lens[zl] + zero_lens[zr]
                other = 0
                if zl > 0:
                    other = max(other, pre[zl - 1])
                if zr < m - 1:
                    other = max(other, suf[zr + 1])
                ans = max(ans, ones + max(merged, other - a))

        return ans