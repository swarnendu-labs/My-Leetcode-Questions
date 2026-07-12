from heapq import heappush, heappop

class Solution:
    def getSkyline(self, buildings):
        events = []
        for l, r, h in buildings:
            events.append((l, -h, r))
            events.append((r, 0, 0))
        events.sort()

        res = []
        heap = [(0, float("inf"))]

        for x, nh, r in events:
            while heap[0][1] <= x:
                heappop(heap)
            if nh:
                heappush(heap, (nh, r))
            h = -heap[0][0]
            if not res or res[-1][1] != h:
                res.append([x, h])

        return res