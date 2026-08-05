from typing import List

class Solution:
    def findMinMoves(self, machines: List[int]) -> int:
        total = sum(machines)
        n = len(machines)

        if total % n:
            return -1

        target = total // n
        ans = 0
        balance = 0

        for x in machines:
            diff = x - target
            balance += diff
            ans = max(ans, abs(balance), diff)

        return ans