class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        def dfs(sub):
            if len(sub) < k:
                return 0

            freq = {}
            for ch in sub:
                freq[ch] = freq.get(ch, 0) + 1

            for ch in freq:
                if freq[ch] < k:
                    return max(dfs(part) for part in sub.split(ch))

            return len(sub)

        return dfs(s)