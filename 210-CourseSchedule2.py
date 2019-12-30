import queue

class Solution:
    def findOrder(self, numCourses, prerequisites):
        # create DAG and topo 
        g = {k:[] for k in range(0,numCourses)}
        topo = {k:0 for k in range(0,numCourses)}
        for p in prerequisites:
            topo[p[0]]+=1
            g[p[1]].append(p[0])
            if p[1] in g[p[0]]: return []
            
        if len(prerequisites) == 0: return [k for k in range(0, numCourses)]
        # BFS remove edges
        res = []
        q = queue.Queue()
        start = min(topo, key=topo.get)
        if topo[start] > 0: return []
        q.put(start)
        topo.pop(start)
        while not q.empty():
            cur = q.get()
            res.append(cur)
            if len(res) == numCourses: break
            for child in g[cur]:
                topo[child]-=1
            
            id = min(topo, key=topo.get)
            q.put(id)
            if topo[id] > 0: return []
            if topo[id] == 0: topo.pop(id)
            
                
        return res

s = Solution()
s.findOrder(2, [[1,0]])