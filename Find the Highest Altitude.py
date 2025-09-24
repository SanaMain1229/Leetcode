class Solution(object):
    def largestAltitude(self, gain):
        altitude = [0]
        temp_alt = 0
        for x in gain:
            temp_alt = temp_alt + x
            altitude.append(temp_alt)

        return max(altitude)
solution = Solution()
print (solution.largestAltitude([-5,1,5,0,-7]))