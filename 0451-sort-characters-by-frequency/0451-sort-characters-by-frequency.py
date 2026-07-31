from collections import Counter

class Solution:
    def frequencySort(self, s: str) -> str:
        return "".join(c * f for c, f in sorted(Counter(s).items(), key=lambda x: -x[1]))