class Solution:
    def sumAndMultiply(self, n: int) -> int:
        x = 0
        digit_sum = 0

        for d in str(n):
            if d != '0':
                digit = int(d)
                x = x * 10 + digit
                digit_sum += digit

        return x * digit_sum