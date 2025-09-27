class Solution(object):
    def decodeString(self, s):
        stack = []
        current_str = ""
        current_num = 0
        
        for char in s:
            if char.isdigit():
                current_num = current_num * 10 + int(char)
            elif char == '[':
                stack.append((current_str, current_num))
                current_str = ""
                current_num = 0
            elif char == ']':
                prev_str, num = stack.pop()
                current_str = prev_str + current_str * num
            else:
                current_str += char
        
        return current_str

solution = Solution()
print(solution.decodeString("10[a]"))
print(solution.decodeString("3[a]2[bc]"))
print(solution.decodeString("2[abc]3[cd]ef"))