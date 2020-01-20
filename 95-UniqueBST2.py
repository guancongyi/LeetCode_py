'''
Recursively build the left and right sub trees
'''


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def helper(s, e):
    l = []
    if s>e:
        l.append(None)
        return l
    else:
        for i in range(s,e+1):
            left = helper(s, i-1)
            right = helper(i+1, e)

            for j in left:
                for k in right:
                    temp = TreeNode(i)
                    temp.left = j
                    temp.right = k
                    l.append(temp)

        return l


class Solution:
    def generateTrees(self, n: int):
        res = helper(1, n)
        if res[0] == None: return None
        return res

    

