from collections import Counter

class Solution:
    def longestPalindrome(self, s):
        cnt = Counter(s)
        ans = 0
        odd = False
        for v in cnt.values():
            ans += v // 2 * 2
            if v % 2:
                odd = True
        return ans + odd