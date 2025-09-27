class Solution(object):
    def asteroidCollision(self, asteroids):
        result = []
        for x in asteroids:
            if x > 0:
                result.append(x)
            else:
                while result and result[-1] > 0:
                    if result[-1] < abs(x):
                        result.pop()
                        continue
                    elif result[-1] == abs(x):
                        result.pop()
                    break
                else:
                    result.append(x)
        return result  
        
solution = Solution()
print (solution.asteroidCollision([-2,-1,1,2]))
