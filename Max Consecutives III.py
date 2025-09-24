class Solution(object):
    def longestOnes(self, nums, k):
        left = 0
        count = 0
        temp_total = 0
        for right in range(len(nums)):
            if nums[right] == 0:
                count += 1
            while count > k:
                if nums[left] == 0:
                    count -= 1
                left += 1
            temp_total = max(temp_total, right - left + 1)
        return temp_total
solution = Solution()
print (solution.longestOnes([1,1,1,0,0,0,1,1,1,1,0],2))