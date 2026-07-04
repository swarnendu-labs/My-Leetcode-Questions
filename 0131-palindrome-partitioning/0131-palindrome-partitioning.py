from typing import List

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        ans = []
        path = []

        def isPalindrome(word):
            return word == word[::-1]

        def backtrack(start):
            if start == len(s):
                ans.append(path[:])
                return

            for end in range(start + 1, len(s) + 1):
                part = s[start:end]

                if isPalindrome(part):
                    path.append(part)
                    backtrack(end)
                    path.pop()

        backtrack(0)
        return ans