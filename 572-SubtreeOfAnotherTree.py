def isSame(s, t):
    if not(s and t): 
        return s is t
    return s.val == t.val and isSame(s.left, t.left) and isSame(s.right, t.right)

class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        if not(s and t): return
        if isSame(s, t): return True
        else: return self.isSubtree(s.left, t) or self.isSubtree(s.right, t)