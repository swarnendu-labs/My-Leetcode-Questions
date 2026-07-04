class Solution:
    def minCut(self, s: str) -> int:
        n = len(s)

        # dp[i] = minimum cuts needed for s[0:i+1]
        dp = list(range(n))

        for center in range(n):

            # Odd-length palindrome
            left = right = center

            while left >= 0 and right < n and s[left] == s[right]:
                if left == 0:
                    dp[right] = 0
                else:
                    dp[right] = min(dp[right], dp[left - 1] + 1)

                left -= 1
                right += 1

            # Even-length palindrome
            left = center - 1
            right = center

            while left >= 0 and right < n and s[left] == s[right]:
                if left == 0:
                    dp[right] = 0
                else:
                    dp[right] = min(dp[right], dp[left - 1] + 1)

                left -= 1
                right += 1

        return dp[n - 1]