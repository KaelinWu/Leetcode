class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        char_dict = Counter(chars)
        res = 0
        for word in words:
            word_count = Counter(word)
            match = True
            for c, freq in word_count.items():
                if freq > char_dict[c]:
                    match = False
                    break
            if match:
                res+=len(word)

        return res

                
