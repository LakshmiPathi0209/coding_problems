from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:

        max_area = 0
        start = 0
        end = len(height) - 1

        while start < end:

            width = end - start
            level = min(height[start], height[end])

            area = width * level
            max_area = max(area, max_area)
            if height[start] < height[end]:
                start = start + 1
            else:
                end = end - 1
        return max_area

if __name__ == "__main__":
    obj = Solution()
    print(obj.maxArea())



