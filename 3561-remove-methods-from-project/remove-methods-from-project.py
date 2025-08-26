class Solution:
    def remainingMethods(self, n: int, k: int, invocations: List[List[int]]) -> List[int]:
        adj = defaultdict(list)
        for src,dst in invocations:
            adj[src].append(dst)
        
        sus = set()
        stack = [k]

        while stack:
            curr = stack.pop()
            if curr in sus:
                continue
            sus.add(curr)
            for nei in adj[curr]:
                if nei in sus:
                    continue
                stack.append(nei)
        res = []
        for i in range(n):
            if i in sus:
                continue
            for nei in adj[i]:
                if nei in sus:
                    return list(range(n))
            res.append(i)
        return res