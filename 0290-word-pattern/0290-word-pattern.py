class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()
        if len(pattern) != len(words):
            return False

        p2w = {}
        w2p = {}

        for c, w in zip(pattern, words):
            if c in p2w:
                if p2w[c] != w:
                    return False
            else:
                p2w[c] = w

            if w in w2p:
                if w2p[w] != c:
                    return False
            else:
                w2p[w] = c

        return True