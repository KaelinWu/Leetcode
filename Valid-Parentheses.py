class Solution:
    def isValid(self, s: str) -> bool:
        dq = deque()
        vals = {'}':'{',']':'[', ')':'('}
        for char in s:
            if char in vals.values():
                dq.appendleft(char)
            elif char in vals.keys():
                if not dq or vals[char] != dq.popleft():
                    return False

           

        
        return not dq

        