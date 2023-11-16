#https://leetcode.com/problems/container-with-most-water/


class Solution:
    def maxArea(self, height: List[int]) -> int:
        arrLength = len(height)

        start = 0
        end = arrLength - 1

        result = []
        max_area = 0
        while start < end:
            area = min(height[start], height[end]) * (end - start)

            if area > max_area:
                max_area = area
            

            if height[start] > height[end]:
                end -= 1
            elif height[start] < height[end]:
                start += 1
            else:
                end -= 1
                start += 1
                
        return max_area