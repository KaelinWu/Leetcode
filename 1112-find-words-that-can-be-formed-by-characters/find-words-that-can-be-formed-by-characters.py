class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        char_dict = Counter(chars)
        res = 0
        for word in words:
            copy = char_dict.copy()
           
            for c in word:
                if c in copy and copy[c] != 0:
                    copy[c] -=1
                else:
                    res-=len(word)
                    break
            
            res+= len(word)
        return res

                
