class Solution(object):
    def equalPairs(self, grid):
        count = 0
        for x in range(len(grid)):
            new_list = list(map(lambda y: y[x], grid))
            if new_list in grid:
                count = count + grid.count(new_list)
        return count
solution = Solution()
print (solution.equalPairs([[3,1,2,2],[1,4,4,5],[2,4,2,2],[2,4,2,2]]))