class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        distances = [float("infinity")] * n
        visited = [False] * n
        edges,res = 0,0
        node = 0
        while edges < n-1:
            nextnode = -1
            visited[node] = True
            for i in range(n):
                if visited[i]:
                    continue
                x,y = points[node]
                x2,y2 = points[i]
                newdist = abs(x-x2) + abs(y-y2)
                distances[i] = min(distances[i],newdist)
                if nextnode == -1 or distances[nextnode] > distances[i]:
                    nextnode = i
            res+= distances[nextnode]
            edges+=1
            node = nextnode
        return res
