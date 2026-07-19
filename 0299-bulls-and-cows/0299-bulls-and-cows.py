from collections import Counter

class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        bulls = 0
        s = []
        g = []
        for a, b in zip(secret, guess):
            if a == b:
                bulls += 1
            else:
                s.append(a)
                g.append(b)
        cows = sum((Counter(s) & Counter(g)).values())
        return f"{bulls}A{cows}B"