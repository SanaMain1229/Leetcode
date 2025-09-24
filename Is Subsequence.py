class Solution(object):
    def isSubsequence(self, s, t):
        if len(s) <= 0:
            return t
        
        s = list(s)
        for i in t:
            if s[0] == i:
                s.pop(0)
    
            if len(s) == 0:
                return True
        
        return False

solution = Solution()
print (solution.isSubsequence("", "ahbgdc"))