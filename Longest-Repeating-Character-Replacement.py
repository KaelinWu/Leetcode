class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left  = 0
        max_repeat = 0
        letters = defaultdict(int)
        count = 0
        for right in range(len(s)):

            
            letters[s[right]] +=1
            
          
            print(count, right, max_repeat)
            if right-left - letters[s[left]] > k-1:
                
                letters[s[left]]-=1
                left+=1
                
            
            max_repeat = max(max_repeat,letters[s[right]])
            
            #print(max_repeat)
        
        #max_repeat = max(letters.values())
        return min(max_repeat + k, len(s))
#k=3
#aabbdaffffffaaabbbabbeaf
