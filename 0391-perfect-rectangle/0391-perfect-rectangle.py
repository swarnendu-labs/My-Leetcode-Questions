class Solution:
    def isRectangleCover(self, rectangles: list[list[int]]) -> bool:
        area = 0
        min_x = float('inf')
        min_y = float('inf')
        max_a = float('-inf')
        max_b = float('-inf')
        corners = set()
        
        for x, y, a, b in rectangles:
            min_x = min(min_x, x)
            min_y = min(min_y, y)
            max_a = max(max_a, a)
            max_b = max(max_b, b)
            
            area += (a - x) * (b - y)
            
            for point in [(x, y), (x, b), (a, y), (a, b)]:
                if point in corners:
                    corners.remove(point)
                else:
                    corners.add(point)
                    
        expected_area = (max_a - min_x) * (max_b - min_y)
        if area != expected_area:
            return False
            
        expected_corners = {(min_x, min_y), (min_x, max_b), (max_a, min_y), (max_a, max_b)}
        return corners == expected_corners