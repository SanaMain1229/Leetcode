from collections import Counter
class Solution(object):
    def maxOperations(self, nums, k):
        count = Counter(nums)
        return sum(min(count[num], count[k - num]) for num in count) // 2
        
solution = Solution()
print (solution.maxOperations([3,1,3,4,3], 6))
#print (solution.maxOperations([1,2,3,4], 5))