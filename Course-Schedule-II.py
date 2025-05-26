class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indegree = [0] * numCourses
        adj = defaultdict(list)
        for clas, pre in prerequisites:
            indegree[clas]+=1
            adj[pre].append(clas)
        que = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                que.append(i)\\
        
        res = []
        while que:
            curr = que.popleft()
            res.append(curr)
            for nei in adj[curr]:
                indegree[nei]-=1
                if indegree[nei] == 0:
                    que.append(nei)
        if len(res) == numCourses:
            return res
        return []