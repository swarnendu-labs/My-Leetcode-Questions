class Solution:
    def validIPAddress(self, queryIP: str) -> str:
        if queryIP.count(".") == 3:
            parts = queryIP.split(".")
            for p in parts:
                if not p or (len(p) > 1 and p[0] == "0") or not p.isdigit():
                    return "Neither"
                if not 0 <= int(p) <= 255:
                    return "Neither"
            return "IPv4"

        if queryIP.count(":") == 7:
            parts = queryIP.split(":")
            hexdigits = "0123456789abcdefABCDEF"
            for p in parts:
                if not (1 <= len(p) <= 4):
                    return "Neither"
                if any(c not in hexdigits for c in p):
                    return "Neither"
            return "IPv6"

        return "Neither"