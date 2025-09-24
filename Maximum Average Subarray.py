class Solution(object):
    def findMaxAverage(self, nums, k):
        curr_sum = sum(nums[:k])
        max_sum = curr_sum

        for i in range(k, len(nums)):
            curr_sum = curr_sum - nums[i-k] + nums[i]
            max_sum = max(max_sum, curr_sum)
        
        return max_sum/float(k)

solution = Solution()
print (solution.findMaxAverage([1,12,-5,-6,50,3], 4))