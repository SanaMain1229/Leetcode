from collections import Counter

class Solution(object):
    def closeStrings(self, word1, word2):
        if set(word1) != set(word2):
            return False

        freq1 = sorted(Counter(word1).values())
        freq2 = sorted(Counter(word2).values())

        return freq1 == freq2

solution = Solution()
print (solution.closeStrings("cabbba", "aabbss"))