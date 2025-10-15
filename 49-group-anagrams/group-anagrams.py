class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        words = defaultdict(list)
        for i in range(len(strs)):
            word = "".join(sorted(strs[i]))
            words[word].append(i)
        res = []
        for word,index in words.items():
            st = []
            for i in index:
                st.append(strs[i])
            res.append(st)
        return res

            