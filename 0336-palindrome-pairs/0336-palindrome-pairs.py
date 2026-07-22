from typing import List

class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        pos = {w: i for i, w in enumerate(words)}
        ans = []

        def is_pal(s):
            return s == s[::-1]

        for i, w in enumerate(words):
            m = len(w)
            for j in range(m + 1):
                if is_pal(w[:j]):
                    t = w[j:][::-1]
                    if t in pos and pos[t] != i:
                        ans.append([pos[t], i])
                if j != m and is_pal(w[j:]):
                    t = w[:j][::-1]
                    if t in pos and pos[t] != i:
                        ans.append([i, pos[t]])

        return ans