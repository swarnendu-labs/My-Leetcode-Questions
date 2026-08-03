class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        t = s.replace("-", "").upper()
        first = len(t) % k
        res = []
        i = 0
        if first:
            res.append(t[:first])
            i = first
        while i < len(t):
            res.append(t[i:i + k])
            i += k
        return "-".join(res)