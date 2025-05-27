class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        indegree = [0] * (len(edges)+1)
        adj = defaultdict(list)
        for src, dst in edges:
            indegree[src]+=1
            indegree[dst]+=1
            adj[dst].append(src)
            adj[src].append(dst)
        que = deque()
        for i in range(1, len(edges)+1):
            if indegree[i] ==1:
                que.append(i)
        while que:
            curr = que.popleft()
            for nei in adj[curr]:
                indegree[nei] -=1
                if indegree[nei] ==1:
                    que.append(nei)
        for u, v in reversed(edges):
            if indegree[u] == 2 and indegree[v] == 2:
                return[u,v]
        return []
