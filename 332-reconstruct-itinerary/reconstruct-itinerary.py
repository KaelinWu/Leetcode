class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = defaultdict(list)
        for src, dst in sorted(tickets, reverse=True):
            adj[src].append(dst)
        
        stack = ["JFK"]
        print(stack)
        res = []
        while stack:
            curr = stack[-1]
            
            if adj[curr]:
                stack.append(adj[curr].pop())
            else:
                res.append(stack.pop())
        return res[::-1]
