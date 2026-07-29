from collections import deque
from typing import List

class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        bank = set(bank)

        if endGene not in bank:
            return -1

        q = deque([(startGene, 0)])
        visited = {startGene}
        genes = ['A', 'C', 'G', 'T']

        while q:
            curr, steps = q.popleft()

            if curr == endGene:
                return steps

            curr = list(curr)

            for i in range(8):
                original = curr[i]

                for ch in genes:
                    if ch == original:
                        continue

                    curr[i] = ch
                    nxt = "".join(curr)

                    if nxt in bank and nxt not in visited:
                        visited.add(nxt)
                        q.append((nxt, steps + 1))

                curr[i] = original

        return -1