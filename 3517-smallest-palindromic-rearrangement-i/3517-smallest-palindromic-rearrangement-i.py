from collections import Counter

class Solution:
    def smallestPalindrome(self, s: str) -> str:
        freq = Counter(s)

        left = []
        mid = ""

        for ch in map(chr, range(ord('a'), ord('z') + 1)):
            left.append(ch * (freq[ch] // 2))
            if freq[ch] % 2:
                mid = ch

        left = "".join(left)
        return left + mid + left[::-1]