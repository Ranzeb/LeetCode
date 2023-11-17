#https://leetcode.com/problems/valid-parentheses/

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for i in range(0, len(s)):
            current_char = s[i]

            if current_char == '(':
                stack.append(')')
            elif current_char == '[':
                stack.append(']')
            elif current_char == '{':
                stack.append('}')
            else:
                last_char = stack[-1]
                if last_char == current_char:
                    stack.pop()
                else:
                    return False
        return True