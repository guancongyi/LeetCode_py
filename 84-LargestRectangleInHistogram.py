'''
The idea is:
push every element to the stack in ascending order,
every time encounter a smaller height, pop the items
from the stack, and calculate the height of the tallest, 
which is the top item(id = i-1) in the stack. And calculate the area 
of that part:
w = i-1-stk[-1]
area = h(i-1)*w

'''


class Solution:
    def largestRectangleArea(self, heights) -> int:
        stk = [-1]
        heights.append(0)

        res = 0
        for i in range(len(heights)):
            
            while heights[i] < heights[stk[-1]]:
                tp = stk.pop()
                h = heights[tp]
                w = i - 1 - stk[-1]
                res = max(res, w*h)
            
            stk.append(i)
            # print(stk, res)

        return res
