class Solution(object):
    def findDifference(self, nums1, nums2):
        return [list(set(filter(lambda x: x not in nums2, nums1))), list(set(filter(lambda x: x not in nums1, nums2)))]
        
        
solution = Solution()
print (solution.findDifference([1,2,3,3], [1,1,2,2]))