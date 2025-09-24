class Solution(object):
    def moveZeroes(self, nums):
        curcount = nums.count(0)
        i = 0

        while i < len(nums):
            if nums[i] == 0:
                nums.pop(i)
            else:
                i += 1
        nums.extend([0] * curcount)

solution = Solution()
print (solution.moveZeroes([0,1,0,3,12]))