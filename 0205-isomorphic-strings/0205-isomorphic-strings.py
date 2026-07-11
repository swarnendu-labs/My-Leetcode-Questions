class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        m1 = {}
        m2 = {}

        for a, b in zip(s, t):
            if a in m1:
                if m1[a] != b:
                    return False
            else:
                m1[a] = b

            if b in m2:
                if m2[b] != a:
                    return False
            else:
                m2[b] = a

        return True