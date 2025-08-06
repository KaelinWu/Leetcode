class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        
        adj = defaultdict(list)
        for src,dst in sorted(tickets,reverse = True):
            adj[src].append(dst)
        res = []
        def dfs(node):
            while adj[node]:
                dfs(adj[node].pop())
            res.append(node)
        dfs("JFK")
        return res[::-1]