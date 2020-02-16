dict = {'2': ['a','b','c'],'3': ['d','e','f'],'4': ['g','h','i'],'5': ['j','k','l'],'6': ['m','n','o'],'7': ['p','q','r', 's'],'8': ['t','u','v'],'9': ['w','x','y','z'] }

class Solution:

    def solve(self, res, digits,i,temp):
        if i == len(digits):
            res.append(temp)
            return res
        
        for poss in dict[digits[i]]:
            self.solve(res, digits,i+1, temp+poss)

                
    
    def letterCombinations(self, digits: str) -> List[str]:
        l = []
        if len(digits) == 0: return []
        self.solve( l, digits, 0,  '')
        return l