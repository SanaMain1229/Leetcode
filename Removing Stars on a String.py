class Solution(object):
    def removeStars(self, s):
        newS = ""
        count = 0

        for i in range(1,len(s)+1):
            if s[-i] == "*":
                count += 1

            if count == 0:
                newS = newS + s[-i]
                print (newS)
            
            if s[-i] != "*" and count != 0:
                count -=1


        return newS[::-1]

solution = Solution()
print (solution.removeStars("Leet**cod*e"))