class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n,node = len(points),0
        distances = [float("infinity")] * n
        edges, res = 0,0
        visit = [False] * n
        while edges < n-1:
            visit[node] = True
            nextnode = -1
            for i in range(n):
                if visit[i]:
                    continue
                x,y = points[node]
                x2,y2 = points[i]
                newdist = abs(x-x2) + abs(y-y2)
                distances[i] = min(newdist,distances[i])
                if nextnode == -1 or distances[nextnode] > distances[i]:
                    nextnode = i
            res+=distances[nextnode]
            node=nextnode
            edges+=1
        return res

