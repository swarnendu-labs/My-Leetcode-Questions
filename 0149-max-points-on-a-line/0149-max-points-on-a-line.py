from math import gcd

class Solution:
    def maxPoints(self, points):
        n = len(points)

        if n <= 2:
            return n

        answer = 2

        for i in range(n):
            slopes = {}

            for j in range(i + 1, n):
                dx = points[j][0] - points[i][0]
                dy = points[j][1] - points[i][1]

                g = gcd(dx, dy)
                dx //= g
                dy //= g

                if dx < 0:
                    dx = -dx
                    dy = -dy

                if dx == 0:
                    dy = 1

                if dy == 0:
                    dx = 1

                slope = (dy, dx)

                slopes[slope] = slopes.get(slope, 1) + 1
                answer = max(answer, slopes[slope])

        return answer