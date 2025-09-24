class Solution(object):
    def pivotIndex(self, nums):
        curr_sum = sum(nums)
        left_sum = 0

        for i in range(len(nums)):
            if left_sum == curr_sum - left_sum - nums[i]:
                return i
            left_sum += nums[i]

        return -1 
solution = Solution()
print (solution.pivotIndex([1,7,3,6,5,6]))\