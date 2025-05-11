class Solution:
    def checkValidString(self, s: str) -> bool:
        dq = []
        stars = []
        for i in range(len(s)):
            char = s[i]
            if char == '(':
                dq.append(i)
            elif char == '*':
                stars.append(i)
            else:
                if not dq and not stars:
                    return False
                elif not dq:
                    stars.pop()
                else:
                    dq.pop()

        if not dq:
            return True
        while stars and dq:
            if stars.pop() < dq.pop():
                return False
        return not dq  
        
        
    
        
            