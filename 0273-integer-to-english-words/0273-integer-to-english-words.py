class Solution:
    def numberToWords(self, num: int) -> str:
        if num == 0:
            return "Zero"

        below20 = [
            "", "One", "Two", "Three", "Four", "Five", "Six", "Seven",
            "Eight", "Nine", "Ten", "Eleven", "Twelve", "Thirteen",
            "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"
        ]
        tens = [
            "", "", "Twenty", "Thirty", "Forty", "Fifty",
            "Sixty", "Seventy", "Eighty", "Ninety"
        ]
        thousands = ["", "Thousand", "Million", "Billion"]

        def helper(n):
            if n == 0:
                return ""
            if n < 20:
                return below20[n] + " "
            if n < 100:
                return tens[n // 10] + " " + helper(n % 10)
            return below20[n // 100] + " Hundred " + helper(n % 100)

        res = ""
        i = 0
        while num > 0:
            if num % 1000:
                res = helper(num % 1000) + thousands[i] + (" " if thousands[i] else "") + res
            num //= 1000
            i += 1

        return res.strip()