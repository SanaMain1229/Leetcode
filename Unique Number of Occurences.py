class Solution(object):
    def uniqueOccurrences(self, arr):
        arr_list = []
        curr_count = 0
        for x in set(arr):
            curr_count = arr.count(x)
            if curr_count in arr_list:
                return False
            arr_list.append(curr_count)
        return True

solution = Solution()
print (solution.uniqueOccurrences([1,2,2,1,1,3]))