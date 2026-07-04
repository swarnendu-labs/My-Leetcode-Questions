from typing import List

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        total = 0
        tank = 0
        start = 0

        for i in range(len(gas)):
            fuel = gas[i] - cost[i]

            total += fuel
            tank += fuel

            if tank < 0:
                start = i + 1
                tank = 0

        if total < 0:
            return -1

        return start