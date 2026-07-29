from collections import Counter
from math import comb

class Solution:
    def smallestPalindrome(self, s: str, k: int) -> str:
        freq = Counter(s)

        mid = ""
        half = []
        for ch in sorted(freq):
            if freq[ch] & 1:
                mid = ch
            half.append(freq[ch] // 2)

        ways = 1
        rem = 0
        for c in half:
            ways *= comb(rem + c, c)
            rem += c

        if ways < k:
            return ""

        cnt = [0] * 26
        for ch, f in freq.items():
            cnt[ord(ch) - ord('a')] = f // 2

        left = []
        rem = sum(cnt)

        while rem:
            for i in range(26):
                if cnt[i] == 0:
                    continue

                cur = ways * cnt[i] // rem

                if k > cur:
                    k -= cur
                else:
                    left.append(chr(i + ord('a')))
                    ways = cur
                    cnt[i] -= 1
                    rem -= 1
                    break

        left = "".join(left)
        return left + mid + left[::-1]