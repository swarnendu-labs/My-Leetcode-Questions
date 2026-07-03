from typing import List
from collections import deque


class Solution:
    def findMaxPathScore(
        self,
        edges: List[List[int]],
        online: List[bool],
        k: int
    ) -> int:

        n = len(online)

        graph = [[] for _ in range(n)]
        indegree = [0] * n

        for u, v, cost in edges:
            graph[u].append((v, cost))
            indegree[v] += 1

        queue = deque()

        for i in range(n):
            if indegree[i] == 0:
                queue.append(i)

        topo = []

        while queue:
            u = queue.popleft()
            topo.append(u)

            for v, cost in graph[u]:
                indegree[v] -= 1

                if indegree[v] == 0:
                    queue.append(v)

        costs = sorted(set(cost for _, _, cost in edges))

        if not costs:
            return -1

        INF = 10**30

        def can_reach(min_score):
            dist = [INF] * n
            dist[0] = 0

            for u in topo:
                if dist[u] == INF:
                    continue

                for v, cost in graph[u]:

                    if cost < min_score:
                        continue

                    if v != n - 1 and not online[v]:
                        continue

                    new_cost = dist[u] + cost

                    if new_cost < dist[v]:
                        dist[v] = new_cost

            return dist[n - 1] <= k

   
        if not can_reach(0):
            return -1

        left = 0
        right = len(costs) - 1
        answer = 0

        while left <= right:
            mid = (left + right) // 2

            if can_reach(costs[mid]):
                answer = costs[mid]
                left = mid + 1
            else:
                right = mid - 1

        return answer