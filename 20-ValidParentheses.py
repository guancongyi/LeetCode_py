'''
use stack
'''

class Solution:
    def isValid(self, s: str) -> bool:
        dict = {'(':')', '[':']', '{':'}'}
        stack = []
        for c in s:
            if c == '(' or c == '[' or c == '{':
                stack.append(c)
            else:
                if len(stack) == 0: return False
                
                temp = stack[-1]
                if dict[temp] == c: stack.pop()
                else: return False
            
        if len(stack) != 0: return False
        return True
                