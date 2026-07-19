class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        n = len(num)

        def check(a, b, k):
            while k < n:
                c = str(int(a) + int(b))
                if not num.startswith(c, k):
                    return False
                k += len(c)
                a, b = b, c
            return True

        for i in range(1, n):
            if num[0] == "0" and i > 1:
                break
            for j in range(i + 1, n):
                if num[i] == "0" and j - i > 1:
                    break
                if check(num[:i], num[i:j], j):
                    return True
        return False