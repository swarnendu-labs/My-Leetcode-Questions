class Solution:
    def largestRectangleArea(self, heights):
        stack = []
        maxArea = 0
        heights.append(0)  # Sentinel to empty the stack

        for i in range(len(heights)):
            while stack and heights[stack[-1]] > heights[i]:
                h = heights[stack.pop()]

                if stack:
                    width = i - stack[-1] - 1
                else:
                    width = i

                maxArea = max(maxArea, h * width)

            stack.append(i)

        heights.pop()  # Restore original list
        return maxArea