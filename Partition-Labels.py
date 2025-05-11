class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        res = []
        count = defaultdict(str)

        for i in range(len(s)):
            count[s[i]] = i
        
        left = 0
        right = 0
        size = 0
        for i in range(len(s)):
            size+=1
            right = max(right, count[s[i]])
          
            if i == right:
               
                res.append(size)
                prev = res[-1]
                size= 0

        return res