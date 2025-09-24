class Solution(object):
    def maxArea(self, height):
        left, right = 0, len(height) - 1
        water = 0

        while left < right:
            curr_area = min(height[left], height[right]) * (right - left)
            water = max(water, curr_area)

            if height[left] < height[right]:
                left += 1
            else:
                right -=1
        
        return water

solution = Solution()
print (solution.maxArea([1,8,6,2,5,4,8,3,7]))