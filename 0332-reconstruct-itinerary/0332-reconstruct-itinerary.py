from collections import defaultdict
import heapq

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = defaultdict(list)
        for a, b in tickets:
            heapq.heappush(graph[a], b)

        ans = []

        def dfs(node):
            while graph[node]:
                dfs(heapq.heappop(graph[node]))
            ans.append(node)

        dfs("JFK")
        return ans[::-1]