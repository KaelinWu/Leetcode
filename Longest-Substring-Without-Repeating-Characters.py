class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_length = 0
        left = 0

        chars = set()
       
        for right in range(len(s)):
            if s[right] not in chars:
        
                chars.add(s[right])
                max_length = max(max_length, right-left+1)
            else:
                while s[right] in chars:
                    chars.remove(s[left])
                    left+=1
                chars.add(s[right])
        return max_length


        abcdafgh
             
            
        