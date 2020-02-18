class Solution:
    def helper(self, candidates, i, t, temp, res):
        if t < 0: return None
        if t == 0:
            res.append(temp)
            return res
        else:
            for j in range(i, len(candidates)):
                curr = candidates[j]
                
                # temp2 = copy.deepcopy(temp)
                # temp2.append(curr)
                self.helper(candidates, j, t-curr, temp+[curr] ,res )

        
    
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ret = []
        temp = []
        self.helper(candidates, 0, target, temp,  ret)
        # print(ret)
        return ret