class Solution(object):
    def longestSubarray(self, nums):
        limit = 1
        j = 0

        for i in range(len(nums)):
            if nums[i] == 0:
                limit-=1
            if limit<0:
                if nums[j] == 0:
                    limit += 1
                j += 1
        return i-j

solution = Solution()
print (solution.longestSubarray([0,1,1,1,0,1,1,0,1]))
