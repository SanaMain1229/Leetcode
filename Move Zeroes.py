class Solution(object):
    def moveZeroes(self, nums):
        curcount = nums.count(0)
        new_nums = [x for x in nums if x != 0] + [0 for x in range(curcount)]
        return str(new_nums).replace(", ", ",")

solution = Solution()
print (solution.moveZeroes([0,1,0,3,12]))