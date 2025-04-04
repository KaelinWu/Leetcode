class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map = defaultdict(list)
        
        for name in strs:
            word = ''.join(sorted(name))
            map[word].append(name)

        return list(map.values())
            
        
        
    
        