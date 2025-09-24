class Solution(object):
    def maxVowels(self, s, k):
        vowels = ['a', 'e', 'i', 'o', 'u']
        count_vowels = 0
        temp_vowels = 0
        for i in range(k):
            if s[i] in vowels:
                count_vowels += 1
        temp_vowels = count_vowels
        if count_vowels == k:
           return count_vowels
        for i in range(k, len(s)):
            if s[i-k] in vowels:
                count_vowels -= 1
            if s[i] in vowels:
                count_vowels += 1
            temp_vowels = max(temp_vowels, count_vowels)
        return temp_vowels    
        
solution = Solution()
print (solution.maxVowels("leetcode",3))
