class Solution:
    def minCost(self, costs) -> int:
        l = len(costs)
        if l==0: return 0
        if l==1: return min(costs[0][0], min(costs[0][1], costs[0][2]))
        for i in range(1, l):
            costs[i][0] += min(costs[i-1][1],costs[i-1][2])
            costs[i][1] += min(costs[i-1][0],costs[i-1][2])
            costs[i][2] += min(costs[i-1][1],costs[i-1][0])

        return min(costs[l-1][0], min(costs[l-1][1],costs[l-1][2]))
       