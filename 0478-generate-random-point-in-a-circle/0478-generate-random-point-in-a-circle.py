import random
import math

class Solution:

    def __init__(self, radius: float, x_center: float, y_center: float):
        self.r = radius
        self.x = x_center
        self.y = y_center

    def randPoint(self):
        theta = random.random() * 2 * math.pi
        d = self.r * math.sqrt(random.random())
        return [self.x + d * math.cos(theta), self.y + d * math.sin(theta)]


# Your Solution object will be instantiated and called as such:
# obj = Solution(radius, x_center, y_center)
# param_1 = obj.randPoint()