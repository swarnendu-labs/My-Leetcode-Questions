from collections import Counter

class Solution:
    def findAnagrams(self, s, p):
        m, n = len(p), len(s)
        if m > n:
            return []

        need = Counter(p)
        window = Counter(s[:m])
        ans = []

        if window == need:
            ans.append(0)

        for i in range(m, n):
            window[s[i]] += 1
            window[s[i - m]] -= 1
            if window[s[i - m]] == 0:
                del window[s[i - m]]
            if window == need:
                ans.append(i - m + 1)

        return ans