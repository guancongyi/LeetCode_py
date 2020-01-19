'''
Using stack keep track the number of the longest valid parentheses so far
'''


class Solution:
    def longestValidParentheses(self, s) -> int:
        stack = [0]
        longest = 0
        for c in s:
            if c is '(':
                stack.append(0)
            else:
                if len(stack) == 1 and c is ')': stack = [0]
                else:
                    
                    temp = stack[-1]+2
                    stack.pop()
                    longest = max(longest, temp)
                    stack[-1] += temp
                    
                    

        return longest