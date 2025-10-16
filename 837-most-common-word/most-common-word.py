class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        
        banned = set(banned)
        clean = ""
        for char in paragraph:
            if char.isalpha() or char == '':
                clean += char
            else:
                clean += ' '
        words = clean.split()
        
        w_dict = defaultdict(int)
        for w in words:
            w = w.lower()
            if w in banned:
                continue
            w_dict[w]+=1
        max_word = None
        max_freq = 0
        print(w_dict)
        for w, freq in w_dict.items():
            if freq > max_freq:
                max_freq = freq
                max_word = w
        return max_word