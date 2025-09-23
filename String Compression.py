import json

class Solution(object):
    def compress(self, chars):
        if len(chars) <= 1:
            return len(chars)

        write_idx = 0
        read_idx = 0

        while read_idx < len(chars):
            current_char = chars[read_idx]
            count = 0
        
            while read_idx < len(chars) and chars[read_idx] == current_char:
                read_idx += 1
                count += 1
            
            chars[write_idx] = current_char
            write_idx += 1

            if count > 1:
                count_str = str(count)
                for digits in count_str:
                    chars[write_idx] = digits
                    write_idx += 1
        
        return write_idx
    
solution = Solution()
print (solution.compress(["a","a","b","b","c","c","c"]))