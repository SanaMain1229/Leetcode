class Solution(object):
    def reverseVowels(self, s):
        vowels = set("aeiouAEIOU")
        testing = []
        result = ""
        for i in s:
            if i in vowels:
                testing.append(i)
        testing.reverse()
        count = 0
        for i in s:
            if i in vowels:
                result = result + testing[count]
                count += 1
            else:
                result = result + i
        return result
    
solution = Solution()
print (solution.reverseVowels("IceCreAm"))